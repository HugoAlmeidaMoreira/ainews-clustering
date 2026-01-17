#!/usr/bin/env python3
"""
Test PostgreSQL connection module.

Run: uv run python src/scripts/test_db_connection.py

Before running, ensure the cloudflared tunnel is active:
    cloudflared access tcp --hostname postgres.hugomoreira.eu --url localhost:5432
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.database import DatabaseManager


def main() -> None:
    """Test database connection and list tables."""
    print("🔗 A testar ligação ao PostgreSQL...")
    print("   (Certifica-te que o túnel cloudflared está ativo!)")
    print()

    try:
        with DatabaseManager() as db:
            if db.test_connection():
                print("✅ Ligação bem sucedida!")
                print()

                # Lista tabelas
                tables = db.list_tables()
                if tables:
                    print(f"📋 Tabelas encontradas ({len(tables)}):")
                    for t in tables[:10]:
                        print(f"   - {t}")
                    if len(tables) > 10:
                        print(f"   ... e mais {len(tables) - 10} tabelas")
                else:
                    print("📋 Nenhuma tabela encontrada (base de dados vazia)")

    except Exception as e:
        print(f"❌ Erro na ligação: {e}")
        print()
        print("💡 Dica: Inicia o túnel primeiro com:")
        print("   cloudflared access tcp --hostname postgres.hugomoreira.eu --url localhost:5432")


if __name__ == "__main__":
    main()
