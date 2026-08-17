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

class Compra(base):

    __tablename__ = "compras"

    id = Column(Integer, primary_key=True)

    fornecedor_id = Column(
        Integer,
        ForeignKey("fornecedores.id"),
        nullable=False,
        index=True
    )

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False,
        index=True
    )

    numero = Column(
        String(50),
        unique=True,
        index=True
    )

    data_compra = Column(
        DateTime,
        default=datetime.now,
        index=True
    )

    data_previsao = Column(DateTime)

    data_recebimento = Column(DateTime)

    subtotal = Column(
        Float,
        default=0
    )

    desconto = Column(
        Float,
        default=0
    )

    frete = Column(
        Float,
        default=0
    )

    total = Column(
        Float,
        default=0
    )

    status = Column(
        String(30),
        default="Pendente",
        index=True
    )

    observacao = Column(Text)

    fornecedor = relationship(
        "Fornecedor",
        back_populates="compras"
    )

    usuario = relationship(
        "Usuario",
        back_populates="compras"
    )

    itens = relationship(
        "ItemCompra",
        back_populates="compra",
        cascade="all, delete-orphan"
    )