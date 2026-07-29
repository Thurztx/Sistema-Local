import customtkinter as ctk
from datetime import datetime

from app.theme.theme_manager import ThemeManager
from app.theme.colors import Colors
from app.theme.fonts import Fonts
from app.theme.spacing import Spacing
from app.theme.dimensions import Dimensions

# Classe
class ProdutosView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.create_header()
        self.create_filters()
        self.create_toolbar()
        self.create_table()

    # Método Header (Cabeçalho)
    def create_header(self):

        colors = ThemeManager.colors()

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20,10)
        )

        header.grid_columnconfigure(0, weight=1)
        self.create_header_left(header)
        self.create_header_right(header)

    # Lado Esquerdo 
    def create_header_left(self, parent):

        colors = ThemeManager.colors()

        left = ctk.CTkFrame(
            parent,
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
            text_color=colors.TEXT
        )

        titulo.pack(anchor="w")

        descricao = ctk.CTkLabel(
            left,
            text="Gerencie todos os produtos cadastrados.",
            font=Fonts.BODY,
            text_color=colors.TEXT_SECONDARY
        )

        descricao.pack(anchor="w", pady=(5,0))

    # Lado Direito
    def create_header_right(self, parent):

        colors = ThemeManager.colors()

        right = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        right.grid(
            row=0,
            column=1,
            sticky="e"
        )

    # Ultima atualização
    ultima = ctk.CTkLabel(
        right,
        text=f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        font=Fonts.SMALL,
        text_color=colors.TEXT_SECONDARY
    )

    ultima.pack(anchor="e")

    # Botões
    buttons = ctk.CTkFrame(
        right,
        fg_color="transparent"
    )

    buttons.pack(
        anchor="e",
        pady=(10,0)
    )