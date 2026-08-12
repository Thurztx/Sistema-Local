import customtkinter as ctk

from tkinter import messagebox

from datetime import datetime, timedelta

from theme.theme_manager import ThemeManager
from theme.fonts import Fonts


class ComprasView(ctk.CTkFrame):

    def __init__(self, master, controller=None):

        super().__init__(master)

        self.controller = controller

        self.colors = ThemeManager.colors()

        self.configure(
            fg_color=self.colors["background"]
        )

        self.create_widgets()
        self.load_purchases()

    # ==========================================
    # Estrutura
    # ==========================================

    def create_widgets(self):

        self.create_header()

        self.create_action_bar()

        self.create_purchase_list()

        self.create_footer()

    # ==========================================
    # Cabeçalho
    # ==========================================

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

    # ==========================================
    # Barra de ações
    # ==========================================

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

        self.search_entry = ctk.CTkEntry(
            self.action_bar,
            width=280,
            height=40,
            placeholder_text="Pesquisar compra..."
        )

        self.search_entry.pack(
            side="right"
        )

    # ==========================================
    # Lista
    # ==========================================

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

    # ==========================================
    # Rodapé
    # ==========================================

    def create_footer(self):

        self.footer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.footer.pack(
            fill="x",
            padx=30,
            pady=(0, 20)
        )

        self.total_label = ctk.CTkLabel(
            self.footer,
            text="0 compras encontradas",
            font=Fonts.body(),
            text_color=self.colors["text_secondary"]
        )

        self.total_label.pack(
            side="left"
        )

    # ==========================================
    # Carregar compras
    # ==========================================

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

    # ==========================================
    # Atualizar lista
    # ==========================================

    def update_purchase_list(self, purchases):

        for widget in self.table_body.winfo_children():

            widget.destroy()

        self.total_label.configure(
            text=f"{len(purchases)} compras encontradas"
        )

        if not purchases:

            self.show_empty_state()

            return

        for purchase in purchases:

            self.create_purchase_row(
                purchase
            )

    # ==========================================
    # Estado vazio
    # ==========================================

    def show_empty_state(self):

        empty_label = ctk.CTkLabel(
            self.table_body,
            text="Nenhuma compra encontrada.",
            font=Fonts.body(),
            text_color=self.colors["text_secondary"]
        )

        empty_label.pack(
            pady=50
        )

    # ==========================================
    # Linha
    # ==========================================

    def create_purchase_row(self, purchase):

        row = ctk.CTkFrame(
            self.table_body,
            fg_color=self.colors["background"],
            corner_radius=8
        )

        row.pack(
            fill="x",
            pady=3
        )

        # ==========================================
        # DATA
        # ==========================================

        data = purchase.get(
            "data_compra",
            "-"
        )

        label_data = ctk.CTkLabel(
            row,
            text=str(data),
            font=Fonts.body(),
            text_color=self.colors["text"]
        )

        label_data.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5,
            pady=12
        )

        # ==========================================
        # FORNECEDOR
        # ==========================================

        fornecedor = purchase.get(
            "fornecedor_nome",
            "Não informado"
        )

        label_fornecedor = ctk.CTkLabel(
            row,
            text=fornecedor,
            font=Fonts.body(),
            text_color=self.colors["text"]
        )

        label_fornecedor.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        # ==========================================
        # NÚMERO DA COMPRA
        # ==========================================

        numero = purchase.get(
            "id",
            "-"
        )

        label_numero = ctk.CTkLabel(
            row,
            text=f"#{numero}",
            font=Fonts.body(),
            text_color=self.colors["text"]
        )

        label_numero.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        # ==========================================
        # PRODUTOS
        # ==========================================

        produtos = self.get_product_count(
            numero
        )

        label_produtos = ctk.CTkLabel(
            row,
            text=str(produtos),
            font=Fonts.body(),
            text_color=self.colors["text"]
        )

        label_produtos.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        # ==========================================
        # PAGAMENTO
        # ==========================================

        pagamento = purchase.get(
            "forma_pagamento",
            "-"
        )

        label_pagamento = ctk.CTkLabel(
            row,
            text=pagamento,
            font=Fonts.body(),
            text_color=self.colors["text"]
        )

        label_pagamento.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        # ==========================================
        # TOTAL
        # ==========================================

        total = purchase.get(
            "valor_total",
            0
        )

        try:

            total = float(total)

        except (TypeError, ValueError):

            total = 0

        label_total = ctk.CTkLabel(
            row,
            text=f"R$ {total:,.2f}".replace(
                ",",
                "X"
            ).replace(
                ".",
                ","
            ).replace(
                "X",
                "."
            ),
            font=Fonts.body(),
            text_color=self.colors["text"]
        )

        label_total.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        # ==========================================
        # STATUS
        # ==========================================

        status = ctk.CTkLabel(
            row,
            text="Concluída",
            font=Fonts.label(),
            text_color=self.colors["success"]
        )

        status.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        # ==========================================
        # CLIQUE
        # ==========================================

        row.bind(
            "<Double-Button-1>",
            lambda event,
            compra_id=numero:
            self.open_purchase_details(
                compra_id
            )
        )

    # ==========================================
    # Ações
    # ==========================================

    def open_purchase_form(self):

        print("Abrir cadastro de compra")

    def search_purchases(self):

        if self.controller is None:
            return

        search_text = (
            self.search_entry
            .get()
            .strip()
        )

        try:

            purchases = self.controller.search_purchases(
                search_text
            )

            self.update_purchase_list(
                purchases
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível pesquisar.\n\n{erro}",
                parent=self
            )

    def filter_purchases(self, value):

        if self.controller is None:
            return

        hoje = datetime.now().date()

        try:

            # ======================================
            # TODAS
            # ======================================

            if value == "Todas":

                purchases = (
                    self.controller
                    .get_purchases()
                )

            # ======================================
            # HOJE
            # ======================================

            elif value == "Hoje":

                start_date = hoje.isoformat()

                end_date = hoje.isoformat()

                purchases = (
                    self.controller
                    .filter_purchases(
                        start_date,
                        end_date
                    )
                )

            # ======================================
            # 7 DIAS
            # ======================================

            elif value == "Últimos 7 dias":

                start_date = (
                    hoje - timedelta(days=6)
                ).isoformat()

                end_date = hoje.isoformat()

                purchases = (
                    self.controller
                    .filter_purchases(
                        start_date,
                        end_date
                    )
                )

            # ======================================
            # 30 DIAS
            # ======================================

            elif value == "Últimos 30 dias":

                start_date = (
                    hoje - timedelta(days=29)
                ).isoformat()

                end_date = hoje.isoformat()

                purchases = (
                    self.controller
                    .filter_purchases(
                        start_date,
                        end_date
                    )
                )

            else:

                purchases = (
                    self.controller
                    .get_purchases()
                )

            self.update_purchase_list(
                purchases
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível aplicar o filtro.\n\n{erro}",
                parent=self
            )

    def get_product_count(self, compra_id):

        try:

            items = self.controller.get_purchase_items(
                compra_id
            )

            return len(items)

        except Exception:

            return 0
        
    def open_purchase_details(self, compra_id):

        if self.controller is None:
            return

        try:

            purchase = self.controller.get_purchase(
                compra_id
            )

            if purchase is None:

                messagebox.showerror(
                    "Erro",
                    "Compra não encontrada.",
                    parent=self
                )

                return

            self.show_purchase_details(
                purchase
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar a compra.\n\n{erro}",
                parent=self
            )

    def show_purchase_details(self, purchase):

        window = ctk.CTkToplevel(
            self
        )

        window.title(
            f"Compra #{purchase['id']}"
        )

        window.geometry(
            "800x600"
        )

        window.transient(
            self.winfo_toplevel()
        )

        window.grab_set()

        colors = self.colors

        # ==========================================
        # TÍTULO
        # ==========================================

        title = ctk.CTkLabel(
            window,
            text=f"Compra #{purchase['id']}",
            font=Fonts.title(),
            text_color=colors["text"]
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        # ==========================================
        # INFORMAÇÕES
        # ==========================================

        info = ctk.CTkLabel(
            window,
            text=(
                f"Fornecedor: "
                f"{purchase.get('fornecedor_nome', 'Não informado')}\n"
                f"Data: "
                f"{purchase.get('data_compra', '-')}\n"
                f"Pagamento: "
                f"{purchase.get('forma_pagamento', '-')}"
            ),
            font=Fonts.body(),
            text_color=colors["text_secondary"],
            justify="left"
        )

        info.pack(
            anchor="w",
            padx=30,
            pady=15
        )

        # ==========================================
        # ITENS
        # ==========================================

        items_frame = ctk.CTkScrollableFrame(
            window,
            fg_color=colors["surface"]
        )

        items_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        try:

            items = self.controller.get_purchase_items(
                purchase["id"]
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar os itens.\n\n{erro}",
                parent=window
            )

            window.destroy()

            return

        for item in items:

            produto = item.get(
                "produto_nome",
                "Produto"
            )

            quantidade = item.get(
                "quantidade",
                0
            )

            valor = item.get(
                "valor_unitario",
                0
            )

            subtotal = item.get(
                "subtotal",
                0
            )

            label = ctk.CTkLabel(
                items_frame,
                text=(
                    f"{produto}    |    "
                    f"{quantidade} un.    |    "
                    f"R$ {valor:.2f}    |    "
                    f"Subtotal: R$ {subtotal:.2f}"
                ),
                font=Fonts.body(),
                text_color=colors["text"],
                anchor="w"
            )

            label.pack(
                fill="x",
                padx=10,
                pady=8
            )

        # ==========================================
        # TOTAL
        # ==========================================

        total = purchase.get(
            "valor_total",
            0
        )

        total_label = ctk.CTkLabel(
            window,
            text=f"Total: R$ {total:.2f}",
            font=Fonts.subtitle(),
            text_color=colors["text"]
        )

        total_label.pack(
            anchor="e",
            padx=30,
            pady=20
        )