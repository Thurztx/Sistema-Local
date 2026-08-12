from app.repositories.compra_repository import CompraRepository
from app.services.compra_service import CompraService


class CompraController:

    def __init__(self):

        # ==========================================
        # REPOSITORY
        # ==========================================

        self.repository = CompraRepository()

        # ==========================================
        # SERVICE
        # ==========================================

        self.service = CompraService(
            self.repository
        )

    # ==========================================
    # CRIAR
    # ==========================================

    def create_purchase(
        self,
        compra,
        itens
    ):

        return self.service.create(
            compra,
            itens
        )

    # ==========================================
    # BUSCAR POR ID
    # ==========================================

    def get_purchase(
        self,
        compra_id
    ):

        return self.service.get_by_id(
            compra_id
        )

    # ==========================================
    # LISTAR
    # ==========================================

    def get_purchases(self):

        return self.service.get_all()

    # ==========================================
    # BUSCAR ITENS
    # ==========================================

    def get_purchase_items(
        self,
        compra_id
    ):

        return self.service.get_items(
            compra_id
        )

    # ==========================================
    # ATUALIZAR
    # ==========================================

    def update_purchase(
        self,
        compra_id,
        compra,
        itens
    ):

        return self.service.update(
            compra_id,
            compra,
            itens
        )

    # ==========================================
    # EXCLUIR
    # ==========================================

    def delete_purchase(
        self,
        compra_id
    ):

        return self.service.delete(
            compra_id
        )

    # ==========================================
    # PESQUISAR
    # ==========================================

    def search_purchases(
        self,
        search_text
    ):

        return self.service.search(
            search_text
        )

    # ==========================================
    # FILTRAR POR PERÍODO
    # ==========================================

    def filter_purchases(
        self,
        start_date,
        end_date
    ):

        return self.service.get_by_period(
            start_date,
            end_date
        )