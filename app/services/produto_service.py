class ProdutoService:

    def __init__(self, repository):

        self.repository = repository

    # ==========================================
    # CRIAR
    # ==========================================

    def create(self, produto):

        if not produto:
            raise ValueError(
                "Os dados do produto são obrigatórios."
            )

        if not produto.get("nome"):
            raise ValueError(
                "O nome do produto é obrigatório."
            )

        if produto.get("preco_custo") is None:
            raise ValueError(
                "O preço de custo é obrigatório."
            )

        if produto.get("preco_venda") is None:
            raise ValueError(
                "O preço de venda é obrigatório."
            )

        return self.repository.create(
            produto
        )

    # ==========================================
    # BUSCAR POR ID
    # ==========================================

    def get_by_id(self, produto_id):

        if not produto_id:
            return None

        return self.repository.get_by_id(
            produto_id
        )

    # ==========================================
    # LISTAR
    # ==========================================

    def get_all(self):

        return self.repository.get_all()

    # ==========================================
    # ATUALIZAR
    # ==========================================

    def update(self, produto_id, produto):

        if not produto_id:
            raise ValueError(
                "O ID do produto é obrigatório."
            )

        if not produto:
            raise ValueError(
                "Os dados do produto são obrigatórios."
            )

        return self.repository.update(
            produto_id,
            produto
        )

    # ==========================================
    # EXCLUIR
    # ==========================================

    def delete(self, produto_id):

        if not produto_id:
            raise ValueError(
                "O ID do produto é obrigatório."
            )

        return self.repository.delete(
            produto_id
        )

    # ==========================================
    # PESQUISAR
    # ==========================================

    def search(self, search_text):

        if not search_text:
            return self.get_all()

        return self.repository.search(
            search_text
        )