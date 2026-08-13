import customtkinter as ctk

from datetime import datetime

import customtkinter as ctk

from datetime import datetime

from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts

from app.views.produtos.produto_form import ProdutoForm


class ProdutosView(ctk.CTkFrame):

    def __init__(self, master, controller=None):

        super().__init__(master)

        self.controller = controller

        self.colors = ThemeManager.colors()

        self.configure(
            fg_color=self.colors.BACKGROUND
        )

        self.create_header()

        self.create_search()

        self.create_filters()

        self.create_table()

        self.create_pagination()

    # ==========================================================
    # CABEÇALHO
    # ==========================================================

    def create_header(self):

        self.header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=30,
            pady=(25, 15)
        )

        self.header.grid_columnconfigure(
            0,
            weight=1
        )

        # ==========================================
        # ESQUERDA
        # ==========================================

        left = ctk.CTkFrame(
            self.header,
            fg_color="transparent"
        )

        left.grid(
            row=0,
            column=0,
            sticky="w"
        )

        titulo = ctk.CTkLabel(
            left,
            text="Produtos",
            font=Fonts.title(),
            text_color=self.colors.TEXT
        )

        titulo.pack(
            anchor="w"
        )

        descricao = ctk.CTkLabel(
            left,
            text="Gerencie todos os produtos cadastrados.",
            font=Fonts.body(),
            text_color=self.colors.TEXT_SECONDARY
        )

        descricao.pack(
            anchor="w",
            pady=(5, 0)
        )

        # ==========================================
        # DIREITA
        # ==========================================

        right = ctk.CTkFrame(
            self.header,
            fg_color="transparent"
        )

        right.grid(
            row=0,
            column=1,
            sticky="e"
        )

        self.lbl_update = ctk.CTkLabel(
            right,
            text=(
                "Última atualização: "
                f"{datetime.now().strftime('%d/%m/%Y %H:%M')}"
            ),
            font=Fonts.small(),
            text_color=self.colors.TEXT_SECONDARY
        )

        self.lbl_update.pack(
            anchor="e",
            pady=(0, 10)
        )

        buttons = ctk.CTkFrame(
            right,
            fg_color="transparent"
        )

        buttons.pack(
            anchor="e"
        )

        self.btn_refresh = ctk.CTkButton(
            buttons,
            text="🔄 Atualizar",
            width=140,
            height=38,
            font=Fonts.button(),
            command=self.refresh_products
        )

        self.btn_refresh.pack(
            side="left",
            padx=(0, 10)
        )

        self.btn_new = ctk.CTkButton(
            buttons,
            text="➕ Novo Produto",
            width=170,
            height=38,
            font=Fonts.button(),
            command=self.new_product
        )

        self.btn_new.pack(
            side="left"
        )

    # ==========================================================
    # PESQUISA
    # ==========================================================

    def create_search(self):

        self.search_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.search_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=30,
            pady=(0, 15)
        )

        self.search_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.search_entry = ctk.CTkEntry(
            self.search_frame,
            height=40,
            placeholder_text=(
                "Pesquisar por código, nome, categoria ou marca..."
            )
        )

        self.search_entry.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        self.search_entry.bind(
            "<Return>",
            lambda event: self.search_products()
        )

        self.btn_search = ctk.CTkButton(
            self.search_frame,
            text="Pesquisar",
            width=120,
            height=40,
            command=self.search_products
        )

        self.btn_search.grid(
            row=0,
            column=1,
            padx=(10, 0)
        )

    # ==========================================================
    # TABELA
    # ==========================================================

    def create_table(self):

        self.table_container = ctk.CTkFrame(
            self,
            fg_color=self.colors.SURFACE,
            corner_radius=10
        )

        self.table_container.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=30,
            pady=(0, 15)
        )

        self.table_container.grid_rowconfigure(
            1,
            weight=1
        )

        self.table_container.grid_columnconfigure(
            0,
            weight=1
        )

        # ==========================================
        # CABEÇALHO DA TABELA
        # ==========================================

        self.table_header = ctk.CTkFrame(
            self.table_container,
            fg_color=self.colors.TABLE_HEADER,
            corner_radius=8
        )

        self.table_header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=10,
            pady=10
        )

        columns = [
            "Código",
            "Produto",
            "Categoria",
            "Tamanho",
            "Estoque",
            "Custo",
            "Venda",
            "Status"
        ]

        for index, column in enumerate(columns):

            self.table_header.grid_columnconfigure(
                index,
                weight=1
            )

            label = ctk.CTkLabel(
                self.table_header,
                text=column,
                font=Fonts.label(),
                text_color=self.colors.TEXT_SECONDARY
            )

            label.grid(
                row=0,
                column=index,
                sticky="ew",
                padx=5,
                pady=12
            )

        # ==========================================
        # CORPO
        # ==========================================

        self.table_body = ctk.CTkScrollableFrame(
            self.table_container,
            fg_color="transparent"
        )

        self.table_body.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=(0, 10)
        )

    # ==========================================================
    # RODAPÉ
    # ==========================================================

    def create_footer(self):

        self.footer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.footer.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=30,
            pady=(0, 20)
        )

        self.total_label = ctk.CTkLabel(
            self.footer,
            text="0 produtos encontrados",
            font=Fonts.body(),
            text_color=self.colors.TEXT_SECONDARY
        )

        self.total_label.pack(
            side="left"
        )

    # ==========================================================
    # CARREGAR PRODUTOS
    # ==========================================================

    def load_products(self):

        if self.controller is None:

            self.show_empty_state(
                "Controller de produtos não configurado."
            )

            return

        try:

            self.produtos = (
                self.controller.get_products()
            )

            self.update_table(
                self.produtos
            )

            self.update_last_update()

        except Exception as erro:

            print(
                f"Erro ao carregar produtos: {erro}"
            )

            self.show_empty_state(
                "Não foi possível carregar os produtos."
            )

    # ==========================================================
    # ATUALIZAR TABELA
    # ==========================================================

    def update_table(
        self,
        produtos
    ):

        for widget in self.table_body.winfo_children():

            widget.destroy()

        self.total_label.configure(
            text=f"{len(produtos)} produtos encontrados"
        )

        if not produtos:

            self.show_empty_state()

            return

        for produto in produtos:

            self.create_product_row(
                produto
            )

    # ==========================================================
    # LINHA DO PRODUTO
    # ==========================================================

    def create_product_row(
        self,
        produto
    ):

        row = ctk.CTkFrame(
            self.table_body,
            fg_color=self.colors.TABLE_ROW,
            corner_radius=6
        )

        row.pack(
            fill="x",
            pady=3
        )

        # ------------------------------------------
        # Recuperar valor
        # ------------------------------------------

        def get_value(
            key,
            default="-"
        ):

            if isinstance(produto, dict):

                return produto.get(
                    key,
                    default
                )

            return getattr(
                produto,
                key,
                default
            )

        # ------------------------------------------
        # Valores
        # ------------------------------------------

        codigo = get_value(
            "codigo"
        )

        nome = get_value(
            "nome"
        )

        categoria = get_value(
            "categoria"
        )

        tamanho = get_value(
            "tamanho"
        )

        quantidade = get_value(
            "quantidade",
            0
        )

        preco_custo = get_value(
            "preco_custo",
            0
        )

        preco_venda = get_value(
            "preco_venda",
            0
        )

        status = get_value(
            "status",
            "Ativo"
        )

        valores = [
            codigo,
            nome,
            categoria,
            tamanho,
            quantidade,
            self.format_currency(preco_custo),
            self.format_currency(preco_venda),
            status
        ]

        # ------------------------------------------
        # Criar colunas
        # ------------------------------------------

        for index, valor in enumerate(valores):

            label = ctk.CTkLabel(
                row,
                text=str(valor),
                font=Fonts.body(),
                text_color=self.colors.TEXT,
                anchor="w"
            )

            label.pack(
                side="left",
                expand=True,
                fill="x",
                padx=8,
                pady=12
            )

            label.bind(
                "<Double-Button-1>",
                lambda event,
                p=produto:
                self.edit_product(p)
            )

        # ------------------------------------------
        # Clique na linha
        # ------------------------------------------

        row.bind(
            "<Double-Button-1>",
            lambda event:
            self.edit_product(produto)
        )

    # ==========================================================
    # ESTADO VAZIO
    # ==========================================================

    def show_empty_state(
        self,
        mensagem="Nenhum produto cadastrado."
    ):

        for widget in self.table_body.winfo_children():

            widget.destroy()

        label = ctk.CTkLabel(
            self.table_body,
            text=mensagem,
            font=Fonts.body(),
            text_color=self.colors.TEXT_SECONDARY
        )

        label.pack(
            pady=60
        )

        self.total_label.configure(
            text="0 produtos encontrados"
        )

    # ==========================================================
    # NOVO PRODUTO
    # ==========================================================

    def new_product(self):

        ProdutoForm(
            self.winfo_toplevel(),
            controller=self.controller
        )

    # ==========================================================
    # EDITAR PRODUTO
    # ==========================================================

    def edit_product(
        self,
        produto
    ):

        ProdutoForm(
            self.winfo_toplevel(),
            controller=self.controller,
            produto=produto
        )

    # ==========================================================
    # PESQUISAR
    # ==========================================================

    def search_products(self):

        if self.controller is None:

            return

        texto = (
            self.search_entry
            .get()
            .strip()
        )

        if not texto:

            self.load_products()

            return

        try:

            produtos = (
                self.controller.search_products(
                    texto
                )
            )

            self.update_table(
                produtos
            )

        except Exception as erro:

            print(
                f"Erro ao pesquisar produtos: {erro}"
            )

    # ==========================================================
    # ATUALIZAR
    # ==========================================================

    def refresh_products(self):

        self.load_products()

    # ==========================================================
    # DATA DA ATUALIZAÇÃO
    # ==========================================================

    def update_last_update(self):

        self.lbl_update.configure(
            text=(
                "Última atualização: "
                f"{datetime.now().strftime('%d/%m/%Y %H:%M')}"
            )
        )

    # ==========================================================
    # FORMATAR MOEDA
    # ==========================================================

    def format_currency(
        self,
        value
    ):

        try:

            value = float(value)

        except (
            TypeError,
            ValueError
        ):

            value = 0

        return (
            f"R$ {value:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )