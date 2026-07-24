from config.database import SessionLocal
from models.produto import Produto

session = SessionLocal()

produtos = session.query(Produto).all()

for produto in produtos:
    print(produto.id)
    print(produto.nome)
    print(produto.quantidade)

session.close()