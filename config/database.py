from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# ==========================================
# DIRETÓRIO PRINCIPAL DO PROJETO
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# BANCO DE DADOS
# ==========================================

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(
    exist_ok=True
)

DATABASE_PATH = DATA_DIR / "estoque.db"


DATABASE_URL = (
    f"sqlite:///{DATABASE_PATH}"
)


# ==========================================
# ENGINE
# ==========================================

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={
        "check_same_thread": False
    }
)


# ==========================================
# SESSÃO
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==========================================
# BASE DOS MODELS
# ==========================================

base = declarative_base()