# importação de bibliotecas 
import customtkinter as ctk

# importação de classes
from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts
from app.theme.dimensions import Dimensions
from app.theme.spacing import Spacing

# Sidebar Lateral esquerda
class Sidebar(ctk.CTkFrame):

    def __init__(self, master, on_menu_click=None):

        self.colors = ThemeManager.colors()

        super().__init__(
            master,
            width=Dimensions.SIDEBAR_WIDTH,
            fg_color=self.colors.SIDEBAR,
            corner_radius=0
        )

        self.on_menu_click = on_menu_click

        self.buttons = {}

        self.selected_button = None

        self.grid_propagate(False)

        self.create_layout()

        # Menus
        self.menu_items = [

            ("dashboard", "🏠", "Dashboard"),

            ("produtos", "📦", "Produtos"),

            ("categorias", "🏷", "Categorias"),

            ("fornecedores", "🚚", "Fornecedores"),

            ("clientes", "👥", "Clientes"),

            ("compras", "🛒", "Compras"),

            ("vendas", "💳", "Vendas"),

            ("estoque", "📈", "Estoque"),

            ("relatorios", "📄", "Relatórios"),

            ("configuracoes", "⚙", "Configurações"),
        ]

        # Logo
        logo = ctk.CTkLabel(

            self,

            text="🧥",

            font=("Segoe UI Emoji", 34)

        )

        logo.pack(pady=(25, 5))

        # Titulo no cabeçalho
        titulo = ctk.CTkLabel(

            self,

            text="ARYN - Controle de Estoque",

            font=Fonts.H3,

            text_color="white"

        )

        titulo.pack()

        # Subtitulo no cabeçalho
        subtitulo = ctk.CTkLabel(

            self,

            text="Sistema Desktop",

            font=Fonts.SMALL,

            text_color="#D1D5DB"

        )

        subtitulo.pack(pady=(0, 25))

        # Botões
        for key, icon, text in self.menu_items:

            button = ctk.CTkButton(

            self,

            text=f"{icon}   {text}",

            anchor="w",

            height=46,

            corner_radius=8,

            fg_color="transparent",

            hover_color="#1F2937",

            font=Fonts.BODY,

            command=lambda k=key: self.select_menu(k)

        )

        button.pack(
            fill="x",
            padx=15,
            pady=3
        )

        self.buttons[key] = button

        # Botão selecionado
        def select_menu(self, menu):

            colors = ThemeManager.colors()

            for key, button in self.buttons.items():

                if key == menu:
                    button.configure(
                    fg_color=colors.PRIMARY,
                    hover_color=colors.PRIMARY_HOVER,
                    text_color="white"
                    )

                else:

                    button.configure(
                        fg_color="transparent",
                        hover_color="#1F2937",
                        text_color="#E5E7EB"
                    )

                if self.on_menu_click:
                    self.on_menu_click(menu)

        # separador entre os menus e o botão "sair"
        separator = ctk.CTkFrame(
            self,
            height=1,
            fg_color="#374151"

        )

        separator.pack(
            fill="x",
            padx=15,
            pady=20
        )

        # Botão Logout (SAIR)
        logout = ctk.CTkButton(
            self,
            text="🚪   Sair",
            anchor="w",
            fg_color="transparent",
            hover_color="#7F1D1D",
            command=self.logout
        )

        logout.pack(
            fill="x",
            padx=15,
            pady=15
        )

        # Metódo Logout
        def logout(self):

            print("Logout")