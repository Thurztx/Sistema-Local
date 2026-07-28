
#┌────────────────────────────────────────────────────────────────────────────────────────┐
#│ Dashboard                                                                              │
#├────────────────────────────────────────────────────────────────────────────────────────┤
#│ 📦 Produtos │ 💰 Valor Estoque │ ⚠ Estoque Baixo │ 🛒 Vendas Hoje                    │
#├───────────────────────────────────────────────────────┬────────────────────────────────┤
#│ Entradas e Saídas                                     │ Produtos Mais Vendidos         │
#│                                                       │                                │
#│                                                       │                                │
#│                                                       │                                │
#├───────────────────────────────────────────────────────┼────────────────────────────────┤
#│ Últimas Movimentações                                 │ Estoque Baixo                  │
#└───────────────────────────────────────────────────────┴────────────────────────────────┘

# Importação de bibliotecas
import customtkinter as ctk

# Importação de temas 
from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts

# importação de widgets
from views.dashboard.widgets.stat_card import StatCard
from views.dashboard.widgets.section_header import SectionHeader

# Classe Dashboard
class DashboardView(ctk.CTkFrame):

    def __init__(self, master):

        colors = ThemeManager.colors()

        super().__init__(
            master,
            fg_color=colors.BACKGROUND
        )

        self.grid_columnconfigure((0,1,2,3), weight=1)

        self.grid_rowconfigure(2, weight=1)

        self.create_widgets()

    # Cabeçalho
        def create_widgets(self):

            colors = ThemeManager.colors()

            titulo = ctk.CTkLabel(
                self,
                text="Dashboard",
                font=Fonts.H1,
                text_color=colors.TEXT
            )

            titulo.grid(
                row=0,
                column=0,
                sticky="w",
                padx=10,
                pady=(10,20)
            )

    # CARDS
        cards = [

            ("📦", "Produtos", "0"),

            ("💰", "Valor do Estoque", "R$ 0,00"),

            ("⚠", "Estoque Baixo", "0"),

            ("🛒", "Vendas Hoje", "R$ 0,00")

        ]

        for coluna, card in enumerate(cards):

            StatCard(
                self,
                *card
            ).grid(
                row=1,
                column=coluna,
                padx=10,
                pady=10,
                sticky="nsew"
            )

    # Área Central
        SectionHeader(
            self,
            "Entradas e Saídas"
        ).grid(
            row=2,
            column=0,
            columnspan=3,
            sticky="w",
            padx=10,
            pady=(30,10)
        )
        
        # Gráfico
        grafico = ctk.CTkFrame(
            self,
            height=300,
            corner_radius=12
        )

        grafico.grid(
            row=3,
            column=0,
            columnspan=3,
            sticky="nsew",
            padx=10
        )

    # Produtos Mais Vendidos
        SectionHeader(
            self,
            "Produtos Mais Vendidos"
        ).grid(
            row=2,
            column=3,
            padx=10,
            sticky="w"
        )

        mais_vendidos = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        mais_vendidos.grid(
            row=3,
            column=3,
            sticky="nsew",
            padx=10
        )