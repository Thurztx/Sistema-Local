import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    # ================================================================
    # CORES ARYN
    # ================================================================

    RED = "#C8102E"
    RED_DARK = "#A50D25"
    RED_LIGHT = "#FCE7EB"

    WHITE = "#FFFFFF"
    BACKGROUND = "#F5F5F5"

    BLACK = "#0A0A0A"

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

        # Configuração do Grid da Dashboard
        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            2,
            weight=1
        )

        # Criação dos componentes
        self.create_header()
        self.create_cards()
        self.create_main_area()
        self.create_footer()

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
            text="Dashboard",
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
            text="Visão geral do seu estoque",
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
        # STATUS DO SISTEMA
        # ============================================================

        self.status = ctk.CTkFrame(
            self.header,
            fg_color=self.WHITE,
            corner_radius=8,
            border_width=1,
            border_color=self.BORDER
        )

        self.status.grid(
            row=0,
            column=1,
            rowspan=2,
            padx=(20, 0)
        )

        self.status_dot = ctk.CTkLabel(
            self.status,
            text="●",
            font=ctk.CTkFont(
                size=12
            ),
            text_color=self.RED
        )

        self.status_dot.pack(
            side="left",
            padx=(12, 4),
            pady=8
        )

        self.status_text = ctk.CTkLabel(
            self.status,
            text="Sistema online",
            font=ctk.CTkFont(
                size=11,
                weight="bold"
            ),
            text_color=self.TEXT
        )

        self.status_text.pack(
            side="left",
            padx=(0, 12)
        )

    # ================================================================
    # CARDS
    # ================================================================

    def create_cards(self):

        self.cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.cards_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=35,
            pady=(5, 20)
        )

        # 4 colunas
        for column in range(4):

            self.cards_frame.grid_columnconfigure(
                column,
                weight=1
            )

        # Card 1
        self.create_card(
            self.cards_frame,
            0,
            "Total de Produtos",
            "1.248",
            "Produtos cadastrados",
            "▣"
        )

        # Card 2
        self.create_card(
            self.cards_frame,
            1,
            "Estoque Baixo",
            "32",
            "Precisam de reposição",
            "!"
        )

        # Card 3
        self.create_card(
            self.cards_frame,
            2,
            "Sem Estoque",
            "8",
            "Produtos esgotados",
            "×"
        )

        # Card 4
        self.create_card(
            self.cards_frame,
            3,
            "Valor do Estoque",
            "R$ 84.560,00",
            "Valor total estimado",
            "$"
        )

    # ================================================================
    # ÁREA PRINCIPAL
    # ================================================================

    def create_main_area(self):

        self.main_area = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.main_area.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=35,
            pady=(0, 15)
        )

        # Coluna de movimentações
        self.main_area.grid_columnconfigure(
            0,
            weight=2
        )

        # Coluna de alertas
        self.main_area.grid_columnconfigure(
            1,
            weight=1
        )

        self.main_area.grid_rowconfigure(
            0,
            weight=1
        )

        self.create_movements()
        self.create_alerts()

    # ================================================================
    # MOVIMENTAÇÕES
    # ================================================================

    def create_movements(self):

        self.movements_frame = ctk.CTkFrame(
            self.main_area,
            fg_color=self.WHITE,
            corner_radius=12,
            border_width=1,
            border_color=self.BORDER
        )

        self.movements_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        self.movements_frame.grid_columnconfigure(
            0,
            weight=2
        )

        self.movements_frame.grid_columnconfigure(
            1,
            weight=1
        )

        self.movements_frame.grid_columnconfigure(
            2,
            weight=1
        )

        self.movements_frame.grid_columnconfigure(
            3,
            weight=1
        )

        # Título
        self.movements_title = ctk.CTkLabel(
            self.movements_frame,
            text="Movimentações recentes",
            font=ctk.CTkFont(
                size=17,
                weight="bold"
            ),
            text_color=self.TEXT
        )

        self.movements_title.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            padx=20,
            pady=(18, 15)
        )

        # Cabeçalho da tabela
        headers = [
            ("Produto", 0),
            ("Tipo", 1),
            ("Quantidade", 2),
            ("Data", 3)
        ]

        for text, column in headers:

            label = ctk.CTkLabel(
                self.movements_frame,
                text=text,
                font=ctk.CTkFont(
                    size=10,
                    weight="bold"
                ),
                text_color="#888888"
            )

            label.grid(
                row=1,
                column=column,
                sticky="w",
                padx=15,
                pady=(0, 8)
            )

        # Dados temporários
        movements = [
            (
                "Camiseta Oversized Preta",
                "Entrada",
                "+50",
                "Hoje"
            ),
            (
                "Calça Cargo Bege",
                "Saída",
                "-12",
                "Hoje"
            ),
            (
                "Moletom ARYN",
                "Entrada",
                "+25",
                "Ontem"
            ),
            (
                "Camiseta Básica Branca",
                "Saída",
                "-8",
                "Ontem"
            ),
            (
                "Boné ARYN",
                "Entrada",
                "+30",
                "18/08"
            )
        ]

        # Linhas
        for row, movement in enumerate(
            movements,
            start=2
        ):

            for column, value in enumerate(movement):

                text_color = self.TEXT

                # Entrada = vermelho
                if column == 1:

                    if value == "Entrada":
                        text_color = self.RED

                    elif value == "Saída":
                        text_color = self.BLACK

                label = ctk.CTkLabel(
                    self.movements_frame,
                    text=value,
                    font=ctk.CTkFont(
                        size=11,
                        weight="bold" if column == 1 else "normal"
                    ),
                    text_color=text_color
                )

                label.grid(
                    row=row,
                    column=column,
                    sticky="w",
                    padx=15,
                    pady=8
                )

    # ================================================================
    # ALERTAS
    # ================================================================

    def create_alerts(self):

        self.alerts_frame = ctk.CTkFrame(
            self.main_area,
            fg_color=self.WHITE,
            corner_radius=12,
            border_width=1,
            border_color=self.BORDER
        )

        self.alerts_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        # Título
        self.alerts_title = ctk.CTkLabel(
            self.alerts_frame,
            text="Alertas de estoque",
            font=ctk.CTkFont(
                size=17,
                weight="bold"
            ),
            text_color=self.TEXT
        )

        self.alerts_title.pack(
            anchor="w",
            padx=20,
            pady=(18, 15)
        )

        # Alertas
        self.create_alert(
            "Camiseta Oversized Preta",
            "Apenas 3 unidades",
            "ESTOQUE BAIXO"
        )

        self.create_alert(
            "Calça Cargo Preta",
            "Apenas 2 unidades",
            "ESTOQUE BAIXO"
        )

        self.create_alert(
            "Moletom Cinza ARYN",
            "Produto esgotado",
            "SEM ESTOQUE"
        )

    # ================================================================
    # CRIAR CARD
    # ================================================================

    def create_card(
        self,
        parent,
        column,
        title,
        value,
        description,
        icon
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=self.WHITE,
            corner_radius=12,
            border_width=1,
            border_color=self.BORDER,
            height=130
        )

        card.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=6
        )

        card.grid_propagate(False)

        card.grid_columnconfigure(
            0,
            weight=1
        )

        # Ícone
        icon_label = ctk.CTkLabel(
            card,
            text=icon,
            width=40,
            height=40,
            corner_radius=10,
            fg_color=self.RED_LIGHT,
            text_color=self.RED,
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        icon_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        # Título
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
            row=1,
            column=0,
            sticky="w",
            padx=15
        )

        # Valor
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
            row=0,
            column=1,
            rowspan=2,
            padx=(5, 15),
            sticky="e"
        )

        # Descrição
        description_label = ctk.CTkLabel(
            card,
            text=description,
            font=ctk.CTkFont(
                size=10
            ),
            text_color="#999999"
        )

        description_label.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            padx=15,
            pady=(2, 10)
        )

    # ================================================================
    # CRIAR ALERTA
    # ================================================================

    def create_alert(
        self,
        product,
        description,
        status
    ):

        frame = ctk.CTkFrame(
            self.alerts_frame,
            fg_color="#FAFAFA",
            corner_radius=8,
            border_width=1,
            border_color=self.BORDER
        )

        frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        # Produto
        product_label = ctk.CTkLabel(
            frame,
            text=product,
            font=ctk.CTkFont(
                size=11,
                weight="bold"
            ),
            text_color=self.TEXT
        )

        product_label.pack(
            anchor="w",
            padx=12,
            pady=(9, 0)
        )

        # Descrição
        description_label = ctk.CTkLabel(
            frame,
            text=description,
            font=ctk.CTkFont(
                size=10
            ),
            text_color=self.TEXT_SECONDARY
        )

        description_label.pack(
            anchor="w",
            padx=12,
            pady=(2, 0)
        )

        # Status
        status_label = ctk.CTkLabel(
            frame,
            text=status,
            font=ctk.CTkFont(
                size=9,
                weight="bold"
            ),
            text_color=self.RED
        )

        status_label.pack(
            anchor="w",
            padx=12,
            pady=(2, 9)
        )

    # ================================================================
    # RODAPÉ
    # ================================================================

    def create_footer(self):

        self.footer = ctk.CTkLabel(
            self,
            text="ARYN • Sistema de Controle de Estoque",
            font=ctk.CTkFont(
                size=10
            ),
            text_color="#999999"
        )

        self.footer.grid(
            row=3,
            column=0,
            sticky="e",
            padx=35,
            pady=(0, 12)
        )