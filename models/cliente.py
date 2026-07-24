# importação de bibliotecas
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
class Cliente(base):

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)

    nome = Column(String(100), 
                  nullable=False,
                  index=True
                  )

    cpf = Column(String(14), 
                 unique=True,
                 index=True
                 )

    telefone = Column(String(20))

    email = Column(String(100))

    cidade = Column(String(50))

    estado = Column(String(2))

    ativo = Column(Boolean, default=True)

    # Relacionamentos
saidas = relationship(
    "Saida",
    back_populates="cliente"
)