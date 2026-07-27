from config.database import base, engine

# Importe todas as models
from models.produto import *
from models.categoria import *
from models.cliente import *
from models.entrada import *
from models.fornecedor import *
from models.movimentacao import *
from models.saida import *
from models.usuario import *

base.metadata.create_all(bind=engine)

print("Banco criado com sucesso!")