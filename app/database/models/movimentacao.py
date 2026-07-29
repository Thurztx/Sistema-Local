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


# class
class Movimentacao(base):

    __tablename__ = "movimentacoes"

    id = Column(Integer, primary_key=True)

    produto_id = Column(Integer, 
                        ForeignKey("produtos.id"),
                        index=True
                        )

    usuario_id = Column(Integer, 
                        ForeignKey("usuarios.id"),
                        index=True
                        )

    tipo = Column(String(20), nullable=False)

    quantidade = Column(Integer, nullable=False)

    observacao = Column(Text)

    data = Column(DateTime, 
                  default=datetime.now,
                  index=True
                  )

    # Relacionamentos
produto = relationship(
    "Produto",
    back_populates="movimentacoes"
)

usuario = relationship(
    "Usuario",
    back_populates="movimentacoes"
)