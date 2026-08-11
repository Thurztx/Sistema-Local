import customtkinter as ctk

from theme.theme_manager import ThemeManager
from theme.fonts import Fonts


class ComprasView(ctk.CTkFrame):

    def __init__(self, 
                 master, 
                 controller=None
    ):

        super().__init__(master)

        self.controller = controller

        self.colors = ThemeManager.colors()

        self.configure(
            fg_color=self.colors["background"]
        )

        self.create_widgets()

    def create_widgets(self):

        self.create_header()

        self.create_action_bar()

        self.create_purchase_list()

        self.create_footer()

# CABEÇALHO
    def create_header(self):

        self.header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.header.pack(
            fill="x",
            padx=30,
            pady=(25, 10)
        )

        self.title = ctk.CTkLabel(
            self.header,
            text="Compras",
            font=Fonts.title(),
            text_color=self.colors["text"]
        )

        self.title.pack(
            anchor="w"
        )

        self.subtitle = ctk.CTkLabel(
            self.header,
            text="Controle de compras e entradas de produtos",
            font=Fonts.body(),
            text_color=self.colors["text_secondary"]
        )

        self.subtitle.pack(
            anchor="w",
            pady=(5, 0)
        )

# BARRA DE AÇÕES
    def create_action_bar(self):

        self.action_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.action_bar.pack(
            fill="x",
            padx=30,
            pady=(10, 15)
        )

        self.btn_nova_compra = ctk.CTkButton(
            self.action_bar,
            text="+ Nova Compra",
            font=Fonts.button(),
            height=40,
            command=self.open_purchase_form
        )

        self.btn_nova_compra.pack(
            side="left"
        )

        open_purchase_form()

        self.search_entry = ctk.CTkEntry(
            self.action_bar,
            width=280,
            height=40,
            placeholder_text="Pesquisar compra..."
        )

        self.search_entry.pack(
            side="right",
            padx=(10, 0)
        )

        self.btn_search = ctk.CTkButton(
            self.action_bar,
            text="Pesquisar",
            width=100,
            height=40,
            command=self.search_purchases
        )

        self.btn_search.pack(
            side="right",
            padx=(10, 0)
        )

        self.filter_menu = ctk.CTkOptionMenu(
            self.action_bar,
            values=[
                "Todas",
                "Hoje",
                "Últimos 7 dias",
                "Últimos 30 dias"
            ],
            width=150,
            height=40,
            command=self.filter_purchases
        )

        self.filter_menu.set("Todas")

        self.filter_menu.pack(
            side="right",
            padx=(10, 0)
        )

# LISTA DE COMPRAS
    def create_purchase_list(self):

        self.list_container = ctk.CTkFrame(
            self,
            fg_color=self.colors["surface"],
            corner_radius=10
        )

        self.list_container.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 15)
        )

        self.table_header = ctk.CTkFrame(
            self.list_container,
            fg_color=self.colors["surface"]
        )

        self.table_header.pack(
            fill="x",
            padx=15,
            pady=15
        )

        columns = [
            "Data",
            "Fornecedor",
            "Nº Compra",
            "Produtos",
            "Pagamento",
            "Total",
            "Status"
        ]

        for column in columns:

            label = ctk.CTkLabel(
                self.table_header,
                text=column,
                font=Fonts.label(),
                text_color=self.colors["text_secondary"]
            )

            label.pack(
                side="left",
                expand=True,
                fill="x"
            )

        self.table_body = ctk.CTkScrollableFrame(
            self.list_container,
            fg_color="transparent"
        )

        self.table_body.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

# MÉTODO CARREGAR COMPRAS
    def load_purchases(self):

        if self.controller is None:
            return

        try:

            purchases = self.controller.get_purchases()

            self.update_purchase_list(
                purchases
            )

        except Exception as erro:

            print(
                f"Erro ao carregar compras: {erro}"
            )

# ATUALIUZAR A LISTA DE COMPRAS
    def update_purchase_list(self, purchases):

        for widget in self.table_body.winfo_children():

            widget.destroy()

        for purchase in purchases:

            self.create_purchase_row(
                purchase
            )