
#┌──────────────────────────────────────────────────────────────────────────────────────────────┐
#│ Produtos                                                                       Atualizar 🔄 │
#├──────────────────────────────────────────────────────────────────────────────────────────────┤
#│ 🔍 Pesquisar... │ Categoria ▼ │ Marca ▼ │ Status ▼ │ Tamanho ▼ │ Cor ▼ │ Limpar Filtros             │
#├──────────────────────────────────────────────────────────────────────────────────────────────┤
#│ Novo Produto │ Importar │ Exportar │ Atualizar                                                      │
#├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
#│ Código │ Produto            │ Categoria│ Marca│ Cor   │ Tam │ Qtde │ Custo │ Venda │ Status │ Ações │
#│-----------------------------------------------------------------------------------------------------│
#│ 0001   │ Camiseta Oversized │ Camisetas│ Nike │ Preto │ G   │ 25   │ R$ 50 │ R$ 89 │    ✔   │ ✏ 🗑  │
#│ 0002   │ Moletom Premium    │ Moletons │ Puma │ Cinza │ M   │ 08   │ R$120 │ R$199 │    ⚠   │ ✏ 🗑  │
#└─────────────────────────────────────────────────────────────────────────────────────────────────────┘

# Classe
class ProdutosView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.create_header()
        self.create_filters()
        self.create_toolbar()
        self.create_table()