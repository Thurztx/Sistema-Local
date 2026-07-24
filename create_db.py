    # importação de bibliotecas
from config.database import base, engine

# Importa todos os modelos
from models.produto import Produto

# Cria todas as tabelas
base.metadata.create_all(bind=engine)

print("Banco criado com sucesso!")