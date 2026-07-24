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
class Fornecedor(base):
        # nome da tabela
    __tablename__ = "fornecedores"
        # ID produto
    id = Column(Integer, primary_key=True)
        # nome
    nome = Column(String(100), 
                  nullable=False,
                  index=True
                  )
        # CNPJ
    cnpj = Column(String(18), 
                  unique=True,
                  index=True
                  )
        # telefone
    telefone = Column(String(20))
        # e-mail
    email = Column(String(100))
        # cidade
    cidade = Column(String(50))
        # estado
    estado = Column(String(2))
        # status
    status = Column(Boolean, default=True)

    # Relacionamentos
entradas = relationship(
    "Entrada",
    back_populates="fornecedor"
)