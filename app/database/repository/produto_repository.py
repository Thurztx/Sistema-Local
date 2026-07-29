# Importação da Model
from models.produto import Produto
from config.database import SessionLocal


class ProdutoRepository:

    # Método 1 — Cadastrar Produto
    def cadastrar(self, produto):

        with SessionLocal() as session:

            session.add(produto)

            session.commit()

            session.refresh(produto)

            return produto
        
    # Método 2 — Listar Produtos
    def listar(self):

        with SessionLocal() as session:

            return session.query(Produto).all()
        
    # Método 3 — Buscar por ID
    def buscar_por_id(self, produto_id):

        with SessionLocal() as session:

            return session.query(Produto).filter(
                Produto.id == produto_id
            ).first()
        
    # Método 4 — Atualizar Produto
    def atualizar(self, produto):

        with SessionLocal() as session:

            session.merge(produto)

            session.commit()

            return produto
        
    # Método 5 — Excluir Produto
    def excluir(self, produto_id):

        with SessionLocal() as session:

            produto = session.query(Produto).filter(
            Produto.id == produto_id
            ).first()

            if produto:

                session.delete(produto)

                session.commit()

                return True

            return False