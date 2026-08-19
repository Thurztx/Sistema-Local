import customtkinter as ctk

from app.views.components.sidebar import Sidebar
from app.views.dashboard.dashboard_view import Dashboard
from app.views.produtos.produto_view import ProdutoView


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ============================================================
        # CONFIGURAÇÕES
        # ============================================================

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.title("ARYN - Controle de Estoque")
        self.geometry("1700x900")
        self.minsize(1200, 700)

        # ============================================================
        # GRID PRINCIPAL
        # ============================================================

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ============================================================
        # SIDEBAR
        # ============================================================

        self.sidebar = Sidebar(
            self,

            on_dashboard=self.show_dashboard,
            on_products=self.open_products,
            on_categories=self.open_categories,
            on_suppliers=self.open_suppliers,
            on_purchases=self.open_purchases,
            on_sales=self.open_sales,
            on_reports=self.open_reports,
            on_settings=self.open_settings
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # ============================================================
        # ÁREA DE CONTEÚDO
        # ============================================================

        self.content = ctk.CTkFrame(
            self,
            fg_color="#F5F5F5",
            corner_radius=0
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.content.grid_rowconfigure(
            0,
            weight=1
        )

        self.content.grid_columnconfigure(
            0,
            weight=1
        )

        # ============================================================
        # ABRIR DASHBOARD INICIALMENTE
        # ============================================================

        self.show_dashboard()

    # ================================================================
    # LIMPAR CONTEÚDO
    # ================================================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ================================================================
    # DASHBOARD
    # ================================================================

    def show_dashboard(self):

        self.clear_content()

        dashboard = Dashboard(
            self.content
        )

        dashboard.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.set_active(
            self.sidebar.dashboard_button
        )

    # ================================================================
    # PRODUTOS
    # ================================================================

    def open_products(self):

        self.clear_content()

        produto_view = ProdutoView(
            self.content
        )

        produto_view.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.set_active(
            self.sidebar.products_button
        )

    # ================================================================
    # CATEGORIAS
    # ================================================================

    def open_categories(self):

        self.clear_content()

        self.sidebar.set_active(
            self.sidebar.categories_button
        )

        self.show_placeholder(
            "Categorias",
            "Gerenciamento de categorias"
        )

    # ================================================================
    # FORNECEDORES
    # ================================================================

    def open_suppliers(self):

        self.clear_content()

        self.sidebar.set_active(
            self.sidebar.suppliers_button
        )

        self.show_placeholder(
            "Fornecedores",
            "Gerenciamento de fornecedores"
        )

    # ================================================================
    # COMPRAS
    # ================================================================

    def open_purchases(self):

        self.clear_content()

        self.sidebar.set_active(
            self.sidebar.purchases_button
        )

        self.show_placeholder(
            "Compras",
            "Gerenciamento de compras"
        )

    # ================================================================
    # VENDAS
    # ================================================================

    def open_sales(self):

        self.clear_content()

        self.sidebar.set_active(
            self.sidebar.sales_button
        )

        self.show_placeholder(
            "Vendas",
            "Gerenciamento de vendas"
        )

    # ================================================================
    # RELATÓRIOS
    # ================================================================

    def open_reports(self):

        self.clear_content()

        self.sidebar.set_active(
            self.sidebar.reports_button
        )

        self.show_placeholder(
            "Relatórios",
            "Relatórios do sistema"
        )

    # ================================================================
    # CONFIGURAÇÕES
    # ================================================================

    def open_settings(self):

        self.clear_content()

        self.sidebar.set_active(
            self.sidebar.settings_button
        )

        self.show_placeholder(
            "Configurações",
            "Configurações do sistema"
        )

    # ================================================================
    # TELA TEMPORÁRIA
    # ================================================================

    def show_placeholder(
        self,
        title,
        subtitle
    ):

        frame = ctk.CTkFrame(
            self.content,
            fg_color="#F5F5F5",
            corner_radius=0
        )

        frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        frame.grid_columnconfigure(
            0,
            weight=1
        )

        frame.grid_rowconfigure(
            0,
            weight=1
        )

        container = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        container.grid(
            row=0,
            column=0
        )

        title_label = ctk.CTkLabel(
            container,
            text=title,
            font=ctk.CTkFont(
                family="Arial",
                size=32,
                weight="bold"
            ),
            text_color="#111111"
        )

        title_label.pack(
            pady=(0, 5)
        )

        subtitle_label = ctk.CTkLabel(
            container,
            text=subtitle,
            font=ctk.CTkFont(
                size=14
            ),
            text_color="#666666"
        )

        subtitle_label.pack()

        status_label = ctk.CTkLabel(
            container,
            text="Esta tela será implementada na próxima etapa.",
            font=ctk.CTkFont(
                size=12
            ),
            text_color="#C8102E"
        )

        status_label.pack(
            pady=(15, 0)
        )


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()