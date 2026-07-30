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

# classe
class Categoria(base):
        # nome da tabela
    __tablename__ = "categorias"
        # ID da tabela com Primary Key
    id = Column(Integer, primary_key=True)
        # Coluna com nome da categoria
    nome = Column(String(80), nullable=False)
        # Coluna para descrição da categoria
    descricao = Column(String(200))