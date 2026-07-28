# Modelo de inspiração da NavBar

#┌─────────────────────────────────────────────────────┐
#    1       2         3                 6       7
#  LOGO | TÍTULO | PESQUISA | AÇÕES | USUÁRIO | HORA
#
#└─────────────────────────────────────────────────────┘

# importação de bibliotecas
import customtkinter as ctk
from datetime import datetime

# importação de classes
from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts
from app.theme.dimensions import Dimensions
from app.theme.spacing import Spacing

# Criação da NavBar
class Navbar(ctk.CTkFrame):

    def __init__(self, master):

        self.colors = ThemeManager.colors()

        super().__init__(
            master,
            height=Dimensions.NAVBAR_HEIGHT,
            fg_color=self.colors.NAVBAR,
            corner_radius=0
        )

        self.grid_columnconfigure(2, weight=1)

        self.create_widgets()

        self.update_clock()

    # Área 1 — Logo
        self.logo = ctk.CTkLabel(
            self,
            text="🧥",
            font=("Segoe UI Emoji", 28)
        )

        self.logo.grid(
            row=0,
            column=0,
            padx=(20, 10),
            pady=15
        )
    
    # Área 2 — Nome do Sistema
        self.system_name = ctk.CTkLabel(
            self,
            text="Controle de Estoque",
            font=Fonts.H2,
            text_color="white"
        )

        self.system_name.grid(
            row=0,
            column=1,
            sticky="w"
        )

    # Área 3 — Barra de Pesquisa Global
        self.search = ctk.CTkEntry(
            self,
            width=350,
            height=38,
            placeholder_text="Pesquisar produtos, clientes...",
            font=Fonts.INPUT
        )

        self.search.grid(
            row=0,
            column=2,
            padx=30,
            sticky="ew"
        )

    # Área 4 — Notificações
        self.notification_button = ctk.CTkButton(
            self,
            text="🔔",
            width=40,
            height=40,
            fg_color="transparent",
            hover_color=self.colors.PRIMARY
        )

        self.notification_button.grid(
            row=0,
            column=3,
            padx=5
        )

    # Área 5 — Tema
        self.theme_button = ctk.CTkButton(
            self,
            text="🌙",
            width=40,
            height=40,
            fg_color="transparent",
            hover_color=self.colors.PRIMARY,
            command=self.toggle_theme
        )

        self.theme_button.grid(
            row=0,
            column=4,
            padx=5
        )

        # Função para alterar o tema
        def toggle_theme(self):

            ThemeManager.toggle()

            self.colors = ThemeManager.colors()

            self.configure(
                fg_color=self.colors.NAVBAR
            )

    # Área 6 — Usuário
        self.user_label = ctk.CTkLabel(
            self,
            text="Arthur",
            font=Fonts.BODY,
            text_color="white"
        )

        self.user_label.grid(
            row=0,
            column=5,
            padx=(20, 10)
        )

    # Área 7 — Relógio
        self.clock = ctk.CTkLabel(
            self,
            text="",
            font=Fonts.BODY,
            text_color="white"
        )

        self.clock.grid(
            row=0,
            column=6,
            padx=(10, 20)
        )

        # Atualização Automática do Relógio
        def update_clock(self):
            now = datetime.now().strftime("%d/%m/%Y  %H:%M")
            self.clock.configure(text=now)
            self.after(1000, self.update_clock)