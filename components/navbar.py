import customtkinter as ctk

from datetime import datetime

from app.theme.theme_manager import ThemeManager

from app.theme.fonts import Fonts

from app.theme.dimensions import Dimensions


class Navbar(ctk.CTkFrame):

    def __init__(self, master):

        colors = ThemeManager.colors()

        super().__init__(
            master,
            height=Dimensions.NAVBAR_HEIGHT,
            fg_color=colors.NAVBAR,
            corner_radius=0
        )

        self.grid_columnconfigure(1, weight=1)

        self.create_widgets()

        ctk.CTkLabel(

            self,

            text="🧥",

            font=("Segoe UI Emoji", 28)

        ).grid(row=0, column=0, padx=20)

        ctk.CTkLabel(

            self,

            text="Controle de Estoque",

            font=Fonts.H2

        ).grid(
            row=0,
            column=1,
            sticky="w"
        )

        ctk.CTkEntry(

            self,

            width=350,

            placeholder_text="Pesquisar..."

        )