import customtkinter as ctk


class ProdutoView(ctk.CTkFrame):

    # ================================================================
    # CORES ARYN
    # ================================================================

    RED = "#C8102E"
    RED_DARK = "#A50D25"
    RED_LIGHT = "#FCE7EB"

    BLACK = "#0A0A0A"
    WHITE = "#FFFFFF"

    BACKGROUND = "#F5F5F5"

    TEXT = "#111111"
    TEXT_SECONDARY = "#666666"

    BORDER = "#E5E5E5"

    # ================================================================
    # CONSTRUTOR
    # ================================================================

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            fg_color=self.BACKGROUND,
            corner_radius=0,
            **kwargs
        )

        # Configuração do Grid
        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            2,
            weight=1
        )

        # Criar componentes
        self.create_header()
        self.create_summary()
        self.create_products_area()

    # ================================================================
    # CABEÇALHO
    # ================================================================

    def create_header(self):

        self.header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=35,
            pady=(30, 15)
        )

        self.header.grid_columnconfigure(
            0,
            weight=1
        )

        # Título

        self.title = ctk.CTkLabel(
            self.header,
            text="Produtos",
            font=ctk.CTkFont(
                family="Arial",
                size=30,
                weight="bold"
            ),
            text_color=self.TEXT
        )

        self.title.grid(
            row=0,
            column=0,
            sticky="w"
        )

        # Subtítulo

        self.subtitle = ctk.CTkLabel(
            self.header,
            text="Gerencie os produtos cadastrados no estoque",
            font=ctk.CTkFont(
                size=13
            ),
            text_color=self.TEXT_SECONDARY
        )

        self.subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            pady=(3, 0)
        )

        # ============================================================
        # BOTÃO NOVO PRODUTO
        # ============================================================

        self.new_product_button = ctk.CTkButton(
            self.header,
            text="+  Novo Produto",
            width=150,
            height=42,
            corner_radius=8,
            fg_color=self.RED,
            hover_color=self.RED_DARK,
            text_color=self.WHITE,
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),
            command=self.new_product
        )

        self.new_product_button.grid(
            row=0,
            column=1,
            rowspan=2,
            padx=(20, 0)
        )

    # ================================================================
    # RESUMO
    # ================================================================

    def create_summary(self):

        self.summary = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.summary.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=35,
            pady=(5, 20)
        )

        for column in range(3):

            self.summary.grid_columnconfigure(
                column,
                weight=1
            )

        # Total

        self.create_summary_card(
            self.summary,
            0,
            "Total de Produtos",
            "1.248"
        )

        # Ativos

        self.create_summary_card(
            self.summary,
            1,
            "Produtos Ativos",
            "1.216"
        )

        # Estoque baixo

        self.create_summary_card(
            self.summary,
            2,
            "Estoque Baixo",
            "32"
        )

    # ================================================================
    # CARD DE RESUMO
    # ================================================================

    def create_summary_card(
        self,
        parent,
        column,
        title,
        value
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=self.WHITE,
            corner_radius=10,
            border_width=1,
            border_color=self.BORDER,
            height=85
        )

        card.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=5
        )

        card.grid_propagate(False)

        card.grid_columnconfigure(
            0,
            weight=1
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(
                size=11,
                weight="bold"
            ),
            text_color=self.TEXT_SECONDARY
        )

        title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=(12, 0)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            ),
            text_color=self.TEXT
        )

        value_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=15,
            pady=(0, 10)
        )

    # ================================================================
    # ÁREA DE PRODUTOS
    # ================================================================

    def create_products_area(self):

        self.products_area = ctk.CTkFrame(
            self,
            fg_color=self.WHITE,
            corner_radius=12,
            border_width=1,
            border_color=self.BORDER
        )

        self.products_area.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=35,
            pady=(0, 25)
        )

        self.products_area.grid_columnconfigure(
            0,
            weight=1
        )

        self.products_area.grid_rowconfigure(
            2,
            weight=1
        )

        # ============================================================
        # BARRA SUPERIOR
        # ============================================================

        self.toolbar = ctk.CTkFrame(
            self.products_area,
            fg_color="transparent"
        )

        self.toolbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=20
        )

        self.toolbar.grid_columnconfigure(
            0,
            weight=1
        )

        # Busca

        self.search_entry = ctk.CTkEntry(
            self.toolbar,
            placeholder_text="Pesquisar produto...",
            height=40,
            width=350,
            corner_radius=8,
            border_width=1,
            border_color=self.BORDER
        )

        self.search_entry.grid(
            row=0,
            column=0,
            sticky="w"
        )

        # Filtro

        self.category_filter = ctk.CTkComboBox(
            self.toolbar,
            values=[
                "Todas as categorias",
                "Camisetas",
                "Calças",
                "Moletons",
                "Bonés",
                "Acessórios"
            ],
            width=180,
            height=40,
            corner_radius=8,
            border_width=1,
            border_color=self.BORDER,
            button_color=self.RED,
            button_hover_color=self.RED_DARK
        )

        self.category_filter.grid(
            row=0,
            column=1,
            padx=10
        )

        self.category_filter.set(
            "Todas as categorias"
        )

        # Botão pesquisar

        self.search_button = ctk.CTkButton(
            self.toolbar,
            text="Pesquisar",
            width=110,
            height=40,
            corner_radius=8,
            fg_color=self.BLACK,
            hover_color="#222222",
            text_color=self.WHITE,
            command=self.search_products
        )

        self.search_button.grid(
            row=0,
            column=2
        )

        # ============================================================
        # CABEÇALHO DA TABELA
        # ============================================================

        self.table_header = ctk.CTkFrame(
            self.products_area,
            fg_color="#FAFAFA",
            height=42,
            corner_radius=0
        )

        self.table_header.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=1
        )

        columns = [
            ("Código", 0),
            ("Produto", 1),
            ("Categoria", 2),
            ("Preço", 3),
            ("Estoque", 4),
            ("Status", 5),
            ("Ações", 6)
        ]

        column_weights = [
            1,
            3,
            2,
            1,
            1,
            1,
            2
        ]

        for index, weight in enumerate(column_weights):

            self.table_header.grid_columnconfigure(
                index,
                weight=weight
            )

        for text, column in columns:

            label = ctk.CTkLabel(
                self.table_header,
                text=text,
                font=ctk.CTkFont(
                    size=10,
                    weight="bold"
                ),
                text_color="#777777"
            )

            label.grid(
                row=0,
                column=column,
                sticky="w",
                padx=12,
                pady=10
            )

        # ============================================================
        # TABELA
        # ============================================================

        self.table = ctk.CTkScrollableFrame(
            self.products_area,
            fg_color=self.WHITE,
            corner_radius=0
        )

        self.table.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=1,
            pady=1
        )

        self.create_product_rows()

    # ================================================================
    # PRODUTOS TEMPORÁRIOS
    # ================================================================

    def create_product_rows(self):

        products = [

            (
                "001",
                "Camiseta Oversized Preta",
                "Camisetas",
                "R$ 89,90",
                "35",
                "Disponível"
            ),

            (
                "002",
                "Camiseta Básica Branca",
                "Camisetas",
                "R$ 59,90",
                "12",
                "Disponível"
            ),

            (
                "003",
                "Calça Cargo Bege",
                "Calças",
                "R$ 149,90",
                "8",
                "Estoque baixo"
            ),

            (
                "004",
                "Moletom ARYN Preto",
                "Moletons",
                "R$ 179,90",
                "0",
                "Sem estoque"
            ),

            (
                "005",
                "Boné ARYN",
                "Bonés",
                "R$ 79,90",
                "24",
                "Disponível"
            ),

            (
                "006",
                "Calça Cargo Preta",
                "Calças",
                "R$ 149,90",
                "3",
                "Estoque baixo"
            ),

            (
                "007",
                "Moletom Cinza ARYN",
                "Moletons",
                "R$ 179,90",
                "15",
                "Disponível"
            )
        ]

        for row, product in enumerate(products):

            self.create_product_row(
                row,
                product
            )

    # ================================================================
    # LINHA DE PRODUTO
    # ================================================================

    def create_product_row(
        self,
        row,
        product
    ):

        code, name, category, price, stock, status = product

        frame = ctk.CTkFrame(
            self.table,
            fg_color=self.WHITE,
            corner_radius=0,
            height=55
        )

        frame.pack(
            fill="x",
            padx=0,
            pady=0
        )

        for column, weight in enumerate(
            [1, 3, 2, 1, 1, 1, 2]
        ):

            frame.grid_columnconfigure(
                column,
                weight=weight
            )

        # Código

        self.create_table_label(
            frame,
            code,
            0
        )

        # Produto

        self.create_table_label(
            frame,
            name,
            1,
            bold=True
        )

        # Categoria

        self.create_table_label(
            frame,
            category,
            2
        )

        # Preço

        self.create_table_label(
            frame,
            price,
            3
        )

        # Estoque

        stock_color = self.TEXT

        if int(stock) == 0:
            stock_color = self.RED

        elif int(stock) <= 5:
            stock_color = self.RED

        stock_label = ctk.CTkLabel(
            frame,
            text=stock,
            font=ctk.CTkFont(
                size=11,
                weight="bold"
            ),
            text_color=stock_color
        )

        stock_label.grid(
            row=0,
            column=4,
            sticky="w",
            padx=12,
            pady=8
        )

        # Status

        if status == "Disponível":

            status_color = "#198754"

        else:

            status_color = self.RED

        status_label = ctk.CTkLabel(
            frame,
            text=status,
            font=ctk.CTkFont(
                size=10,
                weight="bold"
            ),
            text_color=status_color
        )

        status_label.grid(
            row=0,
            column=5,
            sticky="w",
            padx=12
        )

        # ============================================================
        # AÇÕES
        # ============================================================

        actions_frame = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        actions_frame.grid(
            row=0,
            column=6,
            sticky="w",
            padx=8
        )

        edit_button = ctk.CTkButton(
            actions_frame,
            text="Editar",
            width=60,
            height=30,
            corner_radius=6,
            fg_color=self.BLACK,
            hover_color="#222222",
            font=ctk.CTkFont(
                size=10,
                weight="bold"
            ),
            command=lambda: self.edit_product(code)
        )

        edit_button.pack(
            side="left",
            padx=2
        )

        delete_button = ctk.CTkButton(
            actions_frame,
            text="Excluir",
            width=60,
            height=30,
            corner_radius=6,
            fg_color=self.RED,
            hover_color=self.RED_DARK,
            font=ctk.CTkFont(
                size=10,
                weight="bold"
            ),
            command=lambda: self.delete_product(code)
        )

        delete_button.pack(
            side="left",
            padx=2
        )

    # ================================================================
    # LABEL DA TABELA
    # ================================================================

    def create_table_label(
        self,
        parent,
        text,
        column,
        bold=False
    ):

        label = ctk.CTkLabel(
            parent,
            text=text,
            font=ctk.CTkFont(
                size=11,
                weight="bold" if bold else "normal"
            ),
            text_color=self.TEXT
        )

        label.grid(
            row=0,
            column=column,
            sticky="w",
            padx=12,
            pady=8
        )

    # ================================================================
    # NOVO PRODUTO
    # ================================================================

    def new_product(self):

        print("Novo produto")

    # ================================================================
    # PESQUISAR
    # ================================================================

    def search_products(self):

        search = self.search_entry.get()

        category = self.category_filter.get()

        print(
            "Pesquisar:",
            search,
            "| Categoria:",
            category
        )

    # ================================================================
    # EDITAR PRODUTO
    # ================================================================

    def edit_product(self, code):

        print(
            "Editar produto:",
            code
        )

    # ================================================================
    # EXCLUIR PRODUTO
    # ================================================================

    def delete_product(self, code):

        print(
            "Excluir produto:",
            code
        )