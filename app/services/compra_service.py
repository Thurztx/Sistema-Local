class CompraService:

    def __init__(self, repository):

        self.repository = repository

    # ==========================================
    # CRIAR
    # ==========================================

    def create(self, compra, itens):

        self.validate_purchase(
            compra,
            itens
        )

        return self.repository.create(
            compra,
            itens
        )

    # ==========================================
    # BUSCAR
    # ==========================================

    def get_by_id(self, compra_id):

        return self.repository.get_by_id(
            compra_id
        )

    def get_all(self):

        return self.repository.get_all()

    def get_items(self, compra_id):

        return self.repository.get_items(
            compra_id
        )

    # ==========================================
    # ATUALIZAR
    # ==========================================

    def update(
        self,
        compra_id,
        compra,
        itens
    ):

        self.validate_purchase(
            compra,
            itens
        )

        return self.repository.update(
            compra_id,
            compra,
            itens
        )

    # ==========================================
    # EXCLUIR
    # ==========================================

    def delete(self, compra_id):

        return self.repository.delete(
            compra_id
        )

    # ==========================================
    # PESQUISA
    # ==========================================

    def search(self, search_text):

        if not search_text:
            return self.repository.get_all()

        return self.repository.search(
            search_text
        )

    # ==========================================
    # FILTRO
    # ==========================================

    def get_by_period(
        self,
        start_date,
        end_date
    ):

        return self.repository.get_by_period(
            start_date,
            end_date
        )

    # ==========================================
    # VALIDAÇÃO
    # ==========================================

    def validate_purchase(
        self,
        compra,
        itens
    ):

        if not compra.get("fornecedor_id"):
            raise ValueError(
                "O fornecedor é obrigatório."
            )

        if not itens:
            raise ValueError(
                "A compra precisa possuir pelo menos um produto."
            )

        for item in itens:

            if not item.get("produto_id"):
                raise ValueError(
                    "Todos os itens precisam possuir um produto."
                )

            if item.get("quantidade", 0) <= 0:
                raise ValueError(
                    "A quantidade deve ser maior que zero."
                )

            if item.get("valor_unitario", 0) < 0:
                raise ValueError(
                    "O valor unitário não pode ser negativo."
                )