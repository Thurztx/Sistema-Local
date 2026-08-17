from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Text
)

from sqlalchemy.orm import relationship

from config.database import base


class Produto(base):

    __tablename__ = "produtos"

    # ==========================================
    # ID
    # ==========================================

    id = Column(
        Integer,
        primary_key=True
    )

    # ==========================================
    # DADOS DO PRODUTO
    # ==========================================

    nome = Column(
        String(150),
        nullable=False
    )

    descricao = Column(
        Text
    )

    marca = Column(
        String(50)
    )

    modelo = Column(
        String(50)
    )

    cor = Column(
        String(30)
    )

    tamanho = Column(
        String(10)
    )

    # ==========================================
    # VALORES
    # ==========================================

    preco_custo = Column(
        Float,
        nullable=False
    )

    preco_venda = Column(
        Float,
        nullable=False
    )

    # ==========================================
    # ESTOQUE
    # ==========================================

    quantidade = Column(
        Integer,
        default=0
    )

    estoque_minimo = Column(
        Integer,
        default=5
    )

    # ==========================================
    # IDENTIFICAÇÃO
    # ==========================================

    codigo_barras = Column(
        String(50),
        unique=True
    )

    # ==========================================
    # STATUS
    # ==========================================

    status = Column(
        Boolean,
        default=True
    )

    # ==========================================
    # RELACIONAMENTOS
    # ==========================================

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

    itens_compra = relationship(
        "ItemCompra",
        back_populates="produto"
    )