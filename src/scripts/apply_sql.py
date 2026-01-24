
import os
import glob
import hashlib
from datetime import datetime
from src.modules.database import get_datascience_db
from sqlalchemy import text

def get_file_hash(filepath: str) -> str:
    """Calcula o hash SHA256 do conteúdo do ficheiro."""
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def setup_migration_table(db):
    """Cria a tabela de controlo de migrações se não existir."""
    query = """
    CREATE TABLE IF NOT EXISTS _sql_migrations (
        filename TEXT PRIMARY KEY,
        hash TEXT NOT NULL,
        executed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    """
    db.execute(query)

def list_sql_files(directory: str):
    """Lista todos os ficheiros .sql recursivamente."""
    return sorted(glob.glob(os.path.join(directory, "**/*.sql"), recursive=True))

def apply_sql_files(base_dir: str):
    """
    Lê e executa ficheiros .sql apenas se ainda não foram executados 
    ou se o conteúdo (hash) mudou.
    """
    sql_files = list_sql_files(base_dir)
    
    if not sql_files:
        print(f"Nenhum ficheiro SQL encontrado em {base_dir}")
        return

    with get_datascience_db() as db:
        setup_migration_table(db)
        
        # Obter estado atual das migrações
        results = db.read_sql("SELECT filename, hash FROM _sql_migrations")
        executed_migrations = dict(zip(results['filename'], results['hash']))

        for sql_path in sql_files:
            # Usamos o caminho relativo como identificador para ser consistente entre máquinas
            rel_path = os.path.relpath(sql_path, base_dir)
            current_hash = get_file_hash(sql_path)
            
            stored_hash = executed_migrations.get(rel_path)
            
            if stored_hash == current_hash:
                # Comentado para não encher o log, descomenta se quiseres ver o skip
                # print(f"→ {rel_path} já está atualizado. Skip.")
                continue

            action = "Aplicando" if stored_hash is None else "Atualizando"
            print(f"{action} {rel_path}...")
            
            with open(sql_path, "r") as f:
                sql_query = f.read()
            
            try:
                db.execute(sql_query)
                
                # Gravar/Atualizar registo de migração
                upsert_query = """
                INSERT INTO _sql_migrations (filename, hash, executed_at)
                VALUES (:filename, :hash, CURRENT_TIMESTAMP)
                ON CONFLICT (filename) DO UPDATE SET 
                    hash = EXCLUDED.hash,
                    executed_at = CURRENT_TIMESTAMP;
                """
                db.execute(upsert_query, params={"filename": rel_path, "hash": current_hash})
                print(f"✓ {rel_path} aplicado com sucesso.")
            except Exception as e:
                print(f"✗ Erro ao aplicar {rel_path}: {e}")
                # Interrompemos para evitar inconsistências se um script depender de outro
                break

if __name__ == "__main__":
    base_sql_dir = "src/database/sql"
    apply_sql_files(base_sql_dir)
