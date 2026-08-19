import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    # ================================================================
    # CORES ARYN
    # ================================================================

    BLACK = "#0A0A0A"
    BLACK_LIGHT = "#171717"

    RED = "#C8102E"
    RED_DARK = "#A50D25"

    WHITE = "#FFFFFF"

    def __init__(
        self,
        master,
        on_dashboard=None,
        on_products=None,
        on_categories=None,
        on_suppliers=None,
        on_purchases=None,
        on_sales=None,
        on_reports=None,
        on_settings=None,
        **kwargs
    ):
        super().__init__(
            master,
            width=250,
            corner_radius=0,
            fg_color=self.BLACK,
            **kwargs
        )

        self.grid_propagate(False)

        # ============================================================
        # CALLBACKS
        # ============================================================

        self.on_dashboard = on_dashboard
        self.on_products = on_products
        self.on_categories = on_categories
        self.on_suppliers = on_suppliers
        self.on_purchases = on_purchases
        self.on_sales = on_sales
        self.on_reports = on_reports
        self.on_settings = on_settings

        # ============================================================
        # LOGO
        # ============================================================

        self.create_logo()

        # ============================================================
        # MENU PRINCIPAL
        # ============================================================

        self.create_main_menu()

        # ============================================================
        # MENU SISTEMA
        # ============================================================

        self.create_system_menu()

        # ============================================================
        # USUÁRIO
        # ============================================================

        self.create_user_area()

    # ================================================================
    # LOGO
    # ================================================================

    def create_logo(self):

        self.logo_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.logo_frame.pack(
            fill="x",
            padx=22,
            pady=(28, 35)
        )

        self.logo = ctk.CTkLabel(
            self.logo_frame,
            text="ARYN",
            font=ctk.CTkFont(
                family="Arial",
                size=32,
                weight="bold"
            ),
            text_color=self.WHITE
        )

        self.logo.pack(anchor="w")

        self.logo_line = ctk.CTkFrame(
            self.logo_frame,
            height=3,
            width=45,
            fg_color=self.RED
        )

        self.logo_line.pack(
            anchor="w",
            pady=(6, 5)
        )

        self.logo_subtitle = ctk.CTkLabel(
            self.logo_frame,
            text="CONTROLE DE ESTOQUE",
            font=ctk.CTkFont(
                size=9,
                weight="bold"
            ),
            text_color="#999999"
        )

        self.logo_subtitle.pack(
            anchor="w"
        )

    # ================================================================
    # MENU PRINCIPAL
    # ================================================================

    def create_main_menu(self):

        self.menu_title = ctk.CTkLabel(
            self,
            text="MENU PRINCIPAL",
            font=ctk.CTkFont(
                size=10,
                weight="bold"
            ),
            text_color="#777777"
        )

        self.menu_title.pack(
            anchor="w",
            padx=22,
            pady=(0, 10)
        )

        self.dashboard_button = self.create_menu_button(
            "⌂",
            "Dashboard",
            self.on_dashboard,
            active=True
        )

        self.products_button = self.create_menu_button(
            "▣",
            "Produtos",
            self.on_products
        )

        self.categories_button = self.create_menu_button(
            "▤",
            "Categorias",
            self.on_categories
        )

        self.suppliers_button = self.create_menu_button(
            "♙",
            "Fornecedores",
            self.on_suppliers
        )

        self.purchases_button = self.create_menu_button(
            "↓",
            "Compras",
            self.on_purchases
        )

        self.sales_button = self.create_menu_button(
            "↑",
            "Vendas",
            self.on_sales
        )

    # ================================================================
    # MENU SISTEMA
    # ================================================================

    def create_system_menu(self):

        separator = ctk.CTkFrame(
            self,
            height=1,
            fg_color="#292929"
        )

        separator.pack(
            fill="x",
            padx=22,
            pady=22
        )

        self.system_title = ctk.CTkLabel(
            self,
            text="SISTEMA",
            font=ctk.CTkFont(
                size=10,
                weight="bold"
            ),
            text_color="#777777"
        )

        self.system_title.pack(
            anchor="w",
            padx=22,
            pady=(0, 10)
        )

        self.reports_button = self.create_menu_button(
            "▥",
            "Relatórios",
            self.on_reports
        )

        self.settings_button = self.create_menu_button(
            "⚙",
            "Configurações",
            self.on_settings
        )

    # ================================================================
    # ÁREA DO USUÁRIO
    # ================================================================

    def create_user_area(self):

        self.user_frame = ctk.CTkFrame(
            self,
            fg_color=self.BLACK_LIGHT,
            corner_radius=10
        )

        self.user_frame.pack(
            side="bottom",
            fill="x",
            padx=15,
            pady=15
        )

        self.user_avatar = ctk.CTkLabel(
            self.user_frame,
            text="A",
            width=38,
            height=38,
            corner_radius=19,
            fg_color=self.RED,
            text_color=self.WHITE,
            font=ctk.CTkFont(
                size=16,
                weight="bold"
            )
        )

        self.user_avatar.pack(
            side="left",
            padx=(10, 8),
            pady=10
        )

        self.user_info = ctk.CTkFrame(
            self.user_frame,
            fg_color="transparent"
        )

        self.user_info.pack(
            side="left",
            pady=8
        )

        self.user_name = ctk.CTkLabel(
            self.user_info,
            text="Administrador",
            font=ctk.CTkFont(
                size=12,
                weight="bold"
            ),
            text_color=self.WHITE
        )

        self.user_name.pack(
            anchor="w"
        )

        self.user_role = ctk.CTkLabel(
            self.user_info,
            text="Administrador",
            font=ctk.CTkFont(
                size=10
            ),
            text_color="#999999"
        )

        self.user_role.pack(
            anchor="w"
        )

    # ================================================================
    # BOTÃO DO MENU
    # ================================================================

    def create_menu_button(
        self,
        icon,
        text,
        command,
        active=False
    ):

        if active:
            fg_color = self.RED
            hover_color = self.RED_DARK
            text_color = self.WHITE

        else:
            fg_color = "transparent"
            hover_color = "#1F1F1F"
            text_color = "#CCCCCC"

        button = ctk.CTkButton(
            self,
            text=f"{icon}    {text}",
            command=command,
            anchor="w",
            height=42,
            corner_radius=8,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            )
        )

        button.pack(
            fill="x",
            padx=15,
            pady=3
        )

        return button

    # ================================================================
    # ITEM ATIVO
    # ================================================================

    def set_active(self, active_button):

        buttons = [
            self.dashboard_button,
            self.products_button,
            self.categories_button,
            self.suppliers_button,
            self.purchases_button,
            self.sales_button,
            self.reports_button,
            self.settings_button
        ]

        for button in buttons:

            if button == active_button:

                button.configure(
                    fg_color=self.RED,
                    hover_color=self.RED_DARK,
                    text_color=self.WHITE
                )

            else:

                button.configure(
                    fg_color="transparent",
                    hover_color="#1F1F1F",
                    text_color="#CCCCCC"
                )