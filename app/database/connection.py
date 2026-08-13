import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"

DATABASE_PATH = DATA_DIR / "estoque.db"


# ==========================================
# CONEXÃO COM O BANCO
# ==========================================

def conectar():

    DATA_DIR.mkdir(
        exist_ok=True
    )

    conexao = sqlite3.connect(
        DATABASE_PATH
    )

    conexao.row_factory = sqlite3.Row

    return conexao


# ==========================================
# GET CONNECTION
# ==========================================

def get_connection():

    return conectar()


# ==========================================
# INICIALIZAR BANCO
# ==========================================

def inicializar_banco():

    DATA_DIR.mkdir(
        exist_ok=True
    )

    conexao = sqlite3.connect(
        DATABASE_PATH
    )

    try:

        cursor = conexao.cursor()

        # As tabelas serão criadas aqui
        # ou através dos scripts de criação do banco.

        conexao.commit()

    finally:

        conexao.close()