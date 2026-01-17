"""
Modules package for ainews-clustering.

Available modules:
- database: PostgreSQL connection and query utilities
"""

from src.modules.database import (
    DatabaseManager,
    get_datascience_db,
    get_engine,
    get_session,
    query,
)

__all__ = [
    "DatabaseManager",
    "get_datascience_db",
    "get_engine",
    "get_session",
    "query",
]
