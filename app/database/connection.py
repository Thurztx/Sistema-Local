import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "estoque.db"


def conectar():
    DATA_DIR.mkdir(exist_ok=True)

    return sqlite3.connect(DATABASE_PATH)


def inicializar_banco():
    DATA_DIR.mkdir(exist_ok=True)

    conexao = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = conexao.cursor()

        # As tabelas serão criadas aqui
        # ou através dos scripts de criação do banco.

        conexao.commit()

    finally:
        conexao.close()