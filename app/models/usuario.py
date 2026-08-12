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


# Classe
class Usuario(base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)

    nome = Column(String(100), 
                  nullable=False,
                  index=True
                  )

    email = Column(String(100), 
                   unique=True,
                   index=True
                   )

    senha = Column(String(255), nullable=False)

    nivel = Column(String(20), default="Funcionário")

    ativo = Column(Boolean, 
                   default=True,
                   index=True
                   )

    # RELACIONAMENTO ENTRE TABELAS
entradas = relationship(
    "Entrada",
    back_populates="usuario"
)

saidas = relationship(
    "Saida",
    back_populates="usuario"
)

movimentacoes = relationship(
    "Movimentacao",
    back_populates="usuario"
)

compras = relationship(
    "Compra",
    back_populates="usuario"
)