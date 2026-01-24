# PostgreSQL Service

Management and access layer for the shared PostgreSQL cluster.

## Architecture

This service wraps the core `src.modules.database` for consistent access across the codebase.

## Usage

### Using the Client

```python
from services.postgres import get_postgres_client

# Connect to the default 'postgres' database
with get_postgres_client() as db:
    df = db.read_sql("SELECT version()")
    print(df)

# Connect to the 'datascience' database
with get_postgres_client(database="datascience") as db:
    db.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY)")
```

### Direct Access

You can also use the established module directly:

```python
from modules.database import get_datascience_db

with get_datascience_db() as db:
    df = db.read_sql("SELECT * FROM ai_news LIMIT 5")
```

## Management

For interactive management, use **pgAdmin**:
- URL: `https://pgadmin.hugomoreira.eu`

For local CLI access (e.g. `psql`), start the tunnel:
```bash
cloudflared access tcp --hostname postgres.hugomoreira.eu --url localhost:5432
```
