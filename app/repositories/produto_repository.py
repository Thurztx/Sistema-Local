from config.database import SessionLocal
from app.models.produto import Produto


class ProdutoRepository:

    # ==========================================
    # CRIAR
    # ==========================================

    def create(self, produto):

        db = SessionLocal()

        try:

            novo_produto = Produto(
                nome=produto.get("nome"),
                descricao=produto.get("descricao"),
                marca=produto.get("marca"),
                modelo=produto.get("modelo"),
                cor=produto.get("cor"),
                tamanho=produto.get("tamanho"),
                preco_custo=produto.get("preco_custo"),
                preco_venda=produto.get("preco_venda"),
                quantidade=produto.get("quantidade", 0),
                estoque_minimo=produto.get("estoque_minimo", 5),
                codigo_barras=produto.get("codigo_barras"),
                status=produto.get("status", True)
            )

            db.add(novo_produto)
            db.commit()
            db.refresh(novo_produto)

            return novo_produto

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    # ==========================================
    # BUSCAR POR ID
    # ==========================================

    def get_by_id(self, produto_id):

        db = SessionLocal()

        try:

            return db.query(Produto).filter(
                Produto.id == produto_id
            ).first()

        finally:

            db.close()

    # ==========================================
    # LISTAR TODOS
    # ==========================================

    def get_all(self):

        db = SessionLocal()

        try:

            return db.query(Produto).order_by(
                Produto.id.desc()
            ).all()

        finally:

            db.close()

    # ==========================================
    # ATUALIZAR
    # ==========================================

    def update(self, produto_id, dados):

        db = SessionLocal()

        try:

            produto = db.query(Produto).filter(
                Produto.id == produto_id
            ).first()

            if produto is None:
                return None

            for campo, valor in dados.items():

                if hasattr(produto, campo):

                    setattr(
                        produto,
                        campo,
                        valor
                    )

            db.commit()
            db.refresh(produto)

            return produto

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    # ==========================================
    # EXCLUIR
    # ==========================================

    def delete(self, produto_id):

        db = SessionLocal()

        try:

            produto = db.query(Produto).filter(
                Produto.id == produto_id
            ).first()

            if produto is None:
                return False

            db.delete(produto)
            db.commit()

            return True

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()

    # ==========================================
    # PESQUISAR
    # ==========================================

    def search(self, texto):

        db = SessionLocal()

        try:

            texto = f"%{texto}%"

            return db.query(Produto).filter(
                (Produto.nome.ilike(texto)) |
                (Produto.marca.ilike(texto)) |
                (Produto.modelo.ilike(texto)) |
                (Produto.codigo_barras.ilike(texto))
            ).order_by(
                Produto.nome
            ).all()

        finally:

            db.close()