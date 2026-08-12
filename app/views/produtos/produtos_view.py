import customtkinter as ctk
from datetime import datetime

from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts

# Componentes reutilizáveis (adicione conforme for criando)
from components.search_bar import SearchBar
from components.filter_bar import FilterBar
from components.data_table import DataTable
from components.toolbar import Toolbar
from components.pagination import Pagination

class ProdutosView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.create_header()

        self.create_search()

        self.create_filters()

        self.create_table()

        self.create_pagination()

    # Criação do Cabeçalho
    def create_header(self):

        self.header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 15)
        )

        self.header.grid_columnconfigure(0, weight=1)
        self.create_header_left()
        self.create_header_right()

    # cabeçalho esquerdo
    def create_header_left(self):

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
            font=Fonts.H1,
            text_color=self.colors.TEXT
        )

        titulo.pack(anchor="w")

        descricao = ctk.CTkLabel(
            left,
            text="Gerencie todos os produtos cadastrados.",
            font=Fonts.BODY,
            text_color=self.colors.TEXT_SECONDARY
        )

        descricao.pack(
            anchor="w",
            pady=(4,0)
        )

    # cabeçalho direito
    def create_header_right(self):

        right = ctk.CTkFrame(
            self.header,
            fg_color="transparent"
        )

        right.grid(
            row=0,
            column=1,
            sticky="e"
        )

        self.create_last_update(right)
        self.create_header_buttons(right)


# última atualização
    # importação de biblioteca
    from datetime import datetime

    def create_last_update(self, parent):

        self.lbl_update = ctk.CTkLabel(

            parent,

            text=f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            font=Fonts.SMALL,
            text_color=self.colors.TEXT_SECONDARY
        )

        self.lbl_update.pack(
            anchor="e"
        )

    # Frame dos botões
    def create_header_buttons(self, parent):

        frame = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )   

        frame.pack(
            anchor="e",
            pady=(10,0)
        )

        self.create_refresh_button(frame)
        self.create_new_button(frame)

    # Botão atualizar
    def create_refresh_button(self, parent):

        button = ctk.CTkButton(

            parent,

            text="🔄 Atualizar",
            width=140,
            height=38,
            font=Fonts.BUTTON,
            command=self.refresh_products

        )

        button.pack(
            side="left",
            padx=(0,10)
        )

    # Botão "Novo Produto"
    def create_new_button(self, parent):

        button = ctk.CTkButton(

            parent,

            text="➕ Novo Produto",

            width=170,

            height=38,

            font=Fonts.BUTTON,

            command=self.new_product

        )

        button.pack(
            side="left"
        )

    # Métodos Temporários
    def refresh_products(self):

        self.lbl_update.configure(
            text=f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )

        print("Atualizando produtos...")

    def new_product(self):

        print("Abrir tela de cadastro.")