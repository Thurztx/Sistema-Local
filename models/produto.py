# Importação de bibliotecas
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship

from datetime import datetime

from config.database import base

# Classe "produto"
class Produto(base):
        # nome da tabela 
    __tablename__ = "produtos"
        # ID do produto
    id = Column(Integer, primary_key=True)
        # Nome do produto
    nome = Column(String(150), nullable=False)
        # descrição do produto
    descricao = Column(Text)
        # marca do produto
    marca = Column(String(50))
        # modelo do produto
    modelo = Column(String(50))
        # cor
    cor = Column(String(30))
        # tamanho 
    tamanho = Column(String(10))
        # Preço de custo fabricação/compra
    preco_custo = Column(Float, nullable=False)
        # Preço de venda
    preco_venda = Column(Float, nullable=False)
        # quantidade
    quantidade = Column(Integer, default=0)
        # Estoque minímo
    estoque_minimo = Column(Integer, default=5)
        # Cód de barras
    codigo_barras = Column(String(50), unique=True)
        # Status
    status = Column(Boolean, default=True)

    # Relacionamentos

entradas = relationship(
    "Entrada",
    back_populates="produto"
)

saidas = relationship(
    "Saida",
    back_populates="produto"
)

movimentacoes = relationship(
    "Movimentacao",
    back_populates="produto"
)