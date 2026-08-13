import customtkinter as ctk

from app.views.compras.compras_view import ComprasView
from app.controllers.compra_controller import CompraController
from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts

class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        # ==============================
        # CONFIGURAÇÃO DA JANELA
        # ==============================

        self.title("ARYN - Controle de Estoque")
        self.geometry("1700x900")
        self.minsize(1200, 700)

        self.configure(
            fg_color="#F5F5F5"
        )

        # ==============================
        # CONFIGURAÇÃO DA GRID
        # ==============================

        self.grid_columnconfigure(
            0,
            weight=0
        )

        self.grid_columnconfigure(
            1,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        # ==============================
        # VARIÁVEL DA TELA ATUAL
        # ==============================

        self.tela_atual = None

        # ==============================
        # CONTROLLERS
        # ==============================

        self.compra_controller = CompraController()

        # ==============================
        # CRIA INTERFACE
        # ==============================

        self.criar_sidebar()
        self.criar_area_conteudo()

        # ==============================
        # ABRE DASHBOARD INICIAL
        # ==============================

        self.mostrar_dashboard()

# SIDEBAR
    def criar_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=250,
            corner_radius=0,
            fg_color="#111111"
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        # --------------------------------
        # LOGO / NOME
        # --------------------------------

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="ARYN",
            font=ctk.CTkFont(
                size=32,
                weight="bold"
            ),
            text_color="#FFFFFF"
        )

        self.logo.pack(
            pady=(35, 5)
        )

        self.logo_subtitulo = ctk.CTkLabel(
            self.sidebar,
            text="CONTROLE DE ESTOQUE",
            font=ctk.CTkFont(
                size=11,
                weight="bold"
            ),
            text_color="#888888"
        )

        self.logo_subtitulo.pack(
            pady=(0, 35)
        )

        # --------------------------------
        # BOTÕES
        # --------------------------------

        self.criar_botao_menu(
            "Dashboard",
            self.mostrar_dashboard
        )

        self.criar_botao_menu(
            "Produtos",
            self.mostrar_produtos
        )

        self.criar_botao_menu(
            "Clientes",
            self.mostrar_clientes
        )

        self.criar_botao_menu(
            "Fornecedores",
            self.mostrar_fornecedores
        )

        self.criar_botao_menu(
            "Compras",
            self.mostrar_compras
        )

        self.criar_botao_menu(
            "Entradas",
            self.mostrar_entradas
        )

        self.criar_botao_menu(
            "Saídas",
            self.mostrar_saidas
        )

        self.criar_botao_menu(
            "Usuários",
            self.mostrar_usuarios
        )

    # ==========================================================
    # BOTÃO DO MENU
    # ==========================================================

    def criar_botao_menu(
        self,
        texto,
        comando
    ):

        botao = ctk.CTkButton(
            self.sidebar,
            text=texto,
            command=comando,
            height=45,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#2A2A2A",
            text_color="#FFFFFF",
            anchor="w"
        )

        botao.pack(
            fill="x",
            padx=15,
            pady=4
        )

# ÁREA DE CONTEÚDO
    def criar_area_conteudo(self):

        self.area_conteudo = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="#F5F5F5"
        )

        self.area_conteudo.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.area_conteudo.grid_rowconfigure(
            0,
            weight=1
        )

        self.area_conteudo.grid_columnconfigure(
            0,
            weight=1
        )

# LIMPAR ÁREA DE CONTEÚDO
    def limpar_conteudo(self):

        if self.tela_atual is not None:

            self.tela_atual.destroy()

            self.tela_atual = None
    
# DASHBOARD
    def mostrar_dashboard(self):

        self.limpar_conteudo()

        self.tela_atual = ctk.CTkFrame(
            self.area_conteudo,
            fg_color="transparent"
        )

        self.tela_atual.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=30
        )

        titulo = ctk.CTkLabel(
            self.tela_atual,
            text="Dashboard",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            ),
            text_color="#111111"
        )

        titulo.pack(
            anchor="w"
        )

        subtitulo = ctk.CTkLabel(
            self.tela_atual,
            text="Visão geral do controle de estoque.",
            font=ctk.CTkFont(
                size=15
            ),
            text_color="#666666"
        )

        subtitulo.pack(
            anchor="w",
            pady=(5, 30)
        )

# PRODUTOS
    def mostrar_produtos(self):

        self.limpar_conteudo()

        self.tela_atual = ctk.CTkFrame(
            self.area_conteudo,
            fg_color="transparent"
        )

        self.tela_atual.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=30
        )

        titulo = ctk.CTkLabel(
            self.tela_atual,
            text="Produtos",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            ),
            text_color="#111111"
        )

        titulo.pack(
            anchor="w"
        )

# CLIENTES
    def mostrar_clientes(self):

        self.limpar_conteudo()

        self.tela_atual = ctk.CTkFrame(
            self.area_conteudo,
            fg_color="transparent"
        )

        self.tela_atual.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=30
        )

        titulo = ctk.CTkLabel(
            self.tela_atual,
            text="Clientes",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            ),
            text_color="#111111"
        )

        titulo.pack(
            anchor="w"
        )
    
# FORNECEDORES
    def mostrar_fornecedores(self):

        self.limpar_conteudo()

        self.tela_atual = ctk.CTkFrame(
            self.area_conteudo,
            fg_color="transparent"
        )

        self.tela_atual.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=30
        )

        titulo = ctk.CTkLabel(
            self.tela_atual,
            text="Fornecedores",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            ),
            text_color="#111111"
        )

        titulo.pack(
            anchor="w"
        )

    # ==========================================================
    # COMPRAS
    # ==========================================================

    def mostrar_compras(self):

        self.limpar_conteudo()

        self.tela_atual = ComprasView(
            self.area_conteudo,
            controller=self.compra_controller
        )

        self.tela_atual.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # ==========================================================
    # ENTRADAS
    # ==========================================================

    def mostrar_entradas(self):

        self.limpar_conteudo()

        self.tela_atual = ctk.CTkFrame(
            self.area_conteudo,
            fg_color="transparent"
        )

        self.tela_atual.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=30
        )

        titulo = ctk.CTkLabel(
            self.tela_atual,
            text="Entradas",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            ),
            text_color="#111111"
        )

        titulo.pack(
            anchor="w"
        )

    # ==========================================================
    # SAÍDAS
    # ==========================================================

    def mostrar_saidas(self):

        self.limpar_conteudo()

        self.tela_atual = ctk.CTkFrame(
            self.area_conteudo,
            fg_color="transparent"
        )

        self.tela_atual.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=30
        )

        titulo = ctk.CTkLabel(
            self.tela_atual,
            text="Saídas",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            ),
            text_color="#111111"
        )

        titulo.pack(
            anchor="w"
        )

    # ==========================================================
    # USUÁRIOS
    # ==========================================================

    def mostrar_usuarios(self):

        self.limpar_conteudo()

        self.tela_atual = ctk.CTkFrame(
            self.area_conteudo,
            fg_color="transparent"
        )

        self.tela_atual.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=30
        )

        titulo = ctk.CTkLabel(
            self.tela_atual,
            text="Usuários",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            ),
            text_color="#111111"
        )

        titulo.pack(
            anchor="w"
        )