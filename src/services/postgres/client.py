from src.modules.database import (
    DatabaseManager,
    get_engine,
    get_session,
    get_datascience_db,
    query
)

class PostgresClient:
    """
    Service client for PostgreSQL.
    Wraps the database module for consistency with other services.
    """
    
    def __init__(self, database: str = "postgres"):
        self.database = database
        self._manager = None

    def __enter__(self):
        self._manager = DatabaseManager(database=self.database)
        return self._manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._manager:
            self._manager.close()

def get_postgres_client(database: str = "postgres") -> PostgresClient:
    """Factory function to get a Postgres client."""
    return PostgresClient(database=database)
