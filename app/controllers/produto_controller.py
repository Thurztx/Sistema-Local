from app.repositories.produto_repository import ProdutoRepository
from app.services.produto_service import ProdutoService


class ProdutoController:

    def __init__(self):

        # ==========================================
        # REPOSITORY
        # ==========================================

        self.repository = ProdutoRepository()

        # ==========================================
        # SERVICE
        # ==========================================

        self.service = ProdutoService(
            self.repository
        )

    # ==========================================
    # CRIAR
    # ==========================================

    def create_product(self, produto):

        return self.service.create(
            produto
        )

    # ==========================================
    # BUSCAR POR ID
    # ==========================================

    def get_product(self, produto_id):

        return self.service.get_by_id(
            produto_id
        )

    # ==========================================
    # LISTAR
    # ==========================================

    def get_products(self):

        return self.service.get_all()

    # ==========================================
    # ATUALIZAR
    # ==========================================

    def update_product(
        self,
        produto_id,
        produto
    ):

        return self.service.update(
            produto_id,
            produto
        )

    # ==========================================
    # EXCLUIR
    # ==========================================

    def delete_product(self, produto_id):

        return self.service.delete(
            produto_id
        )

    # ==========================================
    # PESQUISAR
    # ==========================================

    def search_products(self, search_text):

        return self.service.search(
            search_text
        )