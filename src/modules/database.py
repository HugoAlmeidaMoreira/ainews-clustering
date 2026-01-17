"""
PostgreSQL Database Connection Module
======================================

Este módulo fornece uma interface para conectar ao PostgreSQL,
tanto para desenvolvimento local (via cloudflared tunnel) como
para acesso interno no cluster Kubernetes.

Uso:
----
    from src.modules.database import get_engine, get_session, DatabaseManager
    from src.modules.database import get_datascience_db  # Para database datascience

    # Opção 1: Usar o engine diretamente com pandas
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM my_table", engine)

    # Opção 2: Usar sessão para queries
    with get_session() as session:
        result = session.execute(text("SELECT 1"))
        print(result.scalar())

    # Opção 3: Usar o DatabaseManager (recomendado)
    with DatabaseManager() as db:
        df = db.read_sql("SELECT * FROM my_table")
        db.execute("INSERT INTO my_table VALUES (1, 'test')")

    # Opção 4: Ligar direto à database datascience (atalho)
    with get_datascience_db() as db:
        df = db.read_sql("SELECT * FROM ai_news LIMIT 10")

Configuração:
-------------
Requer um ficheiro .env com:
    POSTGRES_URL=postgresql://user:pass@localhost:5432/dbname

Para desenvolvimento local, inicia primeiro o túnel cloudflared:
    cloudflared access tcp --hostname postgres.hugomoreira.eu --url localhost:5432
"""

import os
from contextlib import contextmanager
from typing import Any, Generator

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import Session, sessionmaker


# Load environment variables from .env file
load_dotenv()


def get_database_url(internal: bool = False, database: str | None = None) -> str:
    """
    Get the PostgreSQL connection URL from environment variables.

    Args:
        internal: If True, use the internal Kubernetes URL.
                  If False, use the local development URL (default).
        database: Optional database name ('datascience', 'postgres', etc.).
                  If 'datascience', uses POSTGRES_DATASCIENCE_URL.
                  If None, uses default POSTGRES_URL.

    Returns:
        The PostgreSQL connection URL.

    Raises:
        ValueError: If the required environment variable is not set.
    """
    # Determine which environment variable to use
    if database == "datascience":
        env_var = "POSTGRES_DATASCIENCE_URL"
    elif internal:
        env_var = "POSTGRES_URL_INTERNAL"
    else:
        env_var = "POSTGRES_URL"

    url = os.getenv(env_var)

    if not url:
        raise ValueError(
            f"Environment variable {env_var} is not set. "
            "Please check your .env file."
        )

    return url


def get_engine(
    internal: bool = False,
    database: str | None = None,
    **kwargs: Any
) -> Engine:
    """
    Create a SQLAlchemy engine for PostgreSQL.

    Args:
        internal: If True, connect to internal Kubernetes PostgreSQL.
                  If False, connect via localhost (cloudflared tunnel).
        database: Optional database name ('datascience', 'postgres', etc.).
        **kwargs: Additional arguments passed to create_engine.

    Returns:
        SQLAlchemy Engine instance.

    Example:
        >>> engine = get_engine()
        >>> df = pd.read_sql("SELECT * FROM news", engine)
        >>> # Or connect to datascience database
        >>> engine = get_engine(database="datascience")
    """
    url = get_database_url(internal=internal, database=database)

    # Default engine settings optimized for data science workloads
    default_kwargs = {
        "pool_size": 5,
        "max_overflow": 10,
        "pool_timeout": 30,
        "pool_recycle": 1800,  # Recycle connections after 30 minutes
        "echo": False,  # Set to True for SQL debugging
    }
    default_kwargs.update(kwargs)

    return create_engine(url, **default_kwargs)


@contextmanager
def get_session(internal: bool = False) -> Generator[Session, None, None]:
    """
    Context manager for database sessions.

    Args:
        internal: If True, connect to internal Kubernetes PostgreSQL.

    Yields:
        SQLAlchemy Session instance.

    Example:
        >>> with get_session() as session:
        ...     result = session.execute(text("SELECT version()"))
        ...     print(result.scalar())
    """
    engine = get_engine(internal=internal)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class DatabaseManager:
    """
    High-level database manager for data science workflows.

    This class provides a convenient interface for common database
    operations, with built-in connection management.

    Example:
        >>> with DatabaseManager() as db:
        ...     # Read data into DataFrame
        ...     df = db.read_sql("SELECT * FROM news LIMIT 100")
        ...
        ...     # Write DataFrame to database
        ...     db.to_sql(df, "news_processed", if_exists="replace")
        ...
        ...     # Execute raw SQL
        ...     db.execute("CREATE INDEX idx_title ON news(title)")
    """

    def __init__(
        self,
        internal: bool = False,
        database: str | None = None,
        **engine_kwargs: Any
    ):
        """
        Initialize the DatabaseManager.

        Args:
            internal: If True, connect to internal Kubernetes PostgreSQL.
            database: Optional database name ('datascience', 'postgres', etc.).
            **engine_kwargs: Additional arguments passed to create_engine.
        """
        self.internal = internal
        self.database = database
        self.engine_kwargs = engine_kwargs
        self._engine: Engine | None = None

    @property
    def engine(self) -> Engine:
        """Get or create the SQLAlchemy engine."""
        if self._engine is None:
            self._engine = get_engine(
                internal=self.internal,
                database=self.database,
                **self.engine_kwargs
            )
        return self._engine

    def __enter__(self) -> "DatabaseManager":
        """Enter context manager."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exit context manager and dispose engine."""
        self.close()

    def close(self) -> None:
        """Close all connections and dispose the engine."""
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None

    def test_connection(self) -> bool:
        """
        Test the database connection.

        Returns:
            True if connection is successful.

        Raises:
            Exception: If connection fails.
        """
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return result.scalar() == 1

    def read_sql(
        self,
        query: str,
        params: dict[str, Any] | None = None,
        **kwargs: Any
    ) -> pd.DataFrame:
        """
        Execute a SQL query and return results as a DataFrame.

        Args:
            query: SQL query string.
            params: Optional parameters for parameterized queries.
            **kwargs: Additional arguments passed to pd.read_sql.

        Returns:
            DataFrame with query results.

        Example:
            >>> df = db.read_sql(
            ...     "SELECT * FROM news WHERE category = :cat",
            ...     params={"cat": "technology"}
            ... )
        """
        return pd.read_sql(query, self.engine, params=params, **kwargs)

    def to_sql(
        self,
        df: pd.DataFrame,
        table_name: str,
        if_exists: str = "append",
        index: bool = False,
        **kwargs: Any
    ) -> int | None:
        """
        Write DataFrame to PostgreSQL table.

        Args:
            df: DataFrame to write.
            table_name: Name of the target table.
            if_exists: What to do if table exists ('fail', 'replace', 'append').
            index: Whether to write DataFrame index as a column.
            **kwargs: Additional arguments passed to DataFrame.to_sql.

        Returns:
            Number of rows affected (if available).

        Example:
            >>> db.to_sql(df, "news_embeddings", if_exists="replace")
        """
        return df.to_sql(
            table_name,
            self.engine,
            if_exists=if_exists,
            index=index,
            **kwargs
        )

    def execute(self, query: str, params: dict[str, Any] | None = None) -> Any:
        """
        Execute a SQL statement.

        Args:
            query: SQL statement to execute.
            params: Optional parameters for parameterized queries.

        Returns:
            Result of the execution.

        Example:
            >>> db.execute("DROP TABLE IF EXISTS temp_table")
            >>> db.execute(
            ...     "UPDATE news SET processed = :val WHERE id = :id",
            ...     params={"val": True, "id": 123}
            ... )
        """
        with self.engine.connect() as conn:
            if params:
                result = conn.execute(text(query), params)
            else:
                result = conn.execute(text(query))
            conn.commit()
            return result

    def list_tables(self) -> list[str]:
        """
        List all tables in the public schema.

        Returns:
            List of table names.
        """
        query = """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name
        """
        df = self.read_sql(query)
        return df["table_name"].tolist()

    def table_info(self, table_name: str) -> pd.DataFrame:
        """
        Get column information for a table.

        Args:
            table_name: Name of the table.

        Returns:
            DataFrame with column names, types, and nullable info.
        """
        query = """
            SELECT
                column_name,
                data_type,
                is_nullable,
                column_default
            FROM information_schema.columns
            WHERE table_schema = 'public'
              AND table_name = :table_name
            ORDER BY ordinal_position
        """
        return self.read_sql(query, params={"table_name": table_name})


# Convenience function for quick one-off queries
def query(
    sql: str,
    internal: bool = False,
    database: str | None = None,
    **kwargs: Any
) -> pd.DataFrame:
    """
    Execute a quick query and return results as DataFrame.

    This is a convenience function for one-off queries that automatically
    manages the connection.

    Args:
        sql: SQL query string.
        internal: If True, use internal Kubernetes connection.
        database: Optional database name ('datascience', 'postgres', etc.).
        **kwargs: Additional arguments passed to pd.read_sql.

    Returns:
        DataFrame with query results.

    Example:
        >>> from src.modules.database import query
        >>> df = query("SELECT * FROM news LIMIT 10")
        >>> # Or query datascience database
        >>> df = query("SELECT * FROM ai_news LIMIT 10", database="datascience")
    """
    with DatabaseManager(internal=internal, database=database) as db:
        return db.read_sql(sql, **kwargs)


def get_datascience_db(**engine_kwargs: Any) -> DatabaseManager:
    """
    Get a DatabaseManager connected to the datascience database.

    This is a convenience function for working with the datascience database.

    Args:
        **engine_kwargs: Additional arguments passed to create_engine.

    Returns:
        DatabaseManager instance connected to datascience database.

    Example:
        >>> from src.modules.database import get_datascience_db
        >>> with get_datascience_db() as db:
        ...     df = db.read_sql("SELECT * FROM ai_news LIMIT 10")
        ...     print(df.shape)
    """
    return DatabaseManager(database="datascience", **engine_kwargs)
