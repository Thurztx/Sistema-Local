# impotações de biblioteca 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# caminho para o banco SQLite
DATABASE_URL = "sqlite:///database/estoque.db"

# conexão com o banco 
engine = create_engine(
    DATABASE_URL,
    echo=False
)

# cria a fábrica de sessões
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# classe base para todos os modelos
base = declarative_base()