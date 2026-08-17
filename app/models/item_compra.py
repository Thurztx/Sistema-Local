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

class ItemCompra(base):

    __tablename__ = "itens_compra"

    id = Column(Integer, primary_key=True)

    compra_id = Column(
        Integer,
        ForeignKey("compras.id"),
        nullable=False,
        index=True
    )

    produto_id = Column(
        Integer,
        ForeignKey("produtos.id"),
        nullable=False,
        index=True
    )

    quantidade = Column(
        Integer,
        nullable=False
    )

    valor_unitario = Column(
        Float,
        nullable=False
    )

    desconto = Column(
        Float,
        default=0
    )

    subtotal = Column(
        Float,
        default=0
    )

    compra = relationship(
        "Compra",
        back_populates="itens"
    )

    produto = relationship(
        "Produto",
        back_populates="itens_compra"
    )