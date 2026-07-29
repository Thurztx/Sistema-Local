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
class Entrada(base):

    __tablename__ = "entradas"

    id = Column(Integer, primary_key=True)

    produto_id = Column(Integer, 
                        ForeignKey("produtos.id"),
                        index=True
                        )

    fornecedor_id = Column(Integer, 
                           ForeignKey("fornecedores.id"),
                           index=True
                           )

    usuario_id = Column(Integer, 
                        ForeignKey("usuarios.id"),
                        index=True
                        )

    quantidade = Column(Integer, nullable=False)

    valor_unitario = Column(Float)

    data_entrada = Column(DateTime, 
                          default=datetime.now,
                          index=True
                          )

    # Relacionamentos
produto = relationship(
    "Produto",
    back_populates="entradas"
)

fornecedor = relationship(
    "Fornecedor",
    back_populates="entradas"
)

usuario = relationship(
    "Usuario",
    back_populates="entradas"
)