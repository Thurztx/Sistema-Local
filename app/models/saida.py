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
class Saida(base):

    __tablename__ = "saidas"

    id = Column(Integer, primary_key=True)

    produto_id = Column(Integer, 
                        ForeignKey("produtos.id"),
                        index=True
                        )

    usuario_id = Column(Integer, 
                        ForeignKey("usuarios.id"),
                        index=True
                        )

    cliente_id = Column(Integer, 
                        ForeignKey("clientes.id"), 
                        nullable=True,
                        index=True
                        )

    quantidade = Column(Integer, nullable=False)

    tipo = Column(String(30))

    motivo = Column(Text)

    data_saida = Column(DateTime, 
                        default=datetime.now,
                        index=True
                        )

    # Relacionamentos
produto = relationship(
    "Produto",
    back_populates="saidas"
)

usuario = relationship(
    "Usuario",
    back_populates="saidas"
)

cliente = relationship(
    "Cliente",
    back_populates="saidas"
)