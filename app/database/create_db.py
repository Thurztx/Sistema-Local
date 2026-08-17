from config.database import base, engine

# Importe todas as models
from app.models.produto import *
from app.models.categoria import *
from app.models.cliente import *
from app.models.entrada import *
from app.models.fornecedor import *
from app.models.movimentacao import *
from app.models.saida import *
from app.models.usuario import *
from app.models.compra import *
from app.models.item_compra import *


base.metadata.create_all(
    bind=engine
)

print("Banco criado com sucesso!")