import customtkinter as ctk

from tkinter import messagebox, filedialog

from PIL import Image

from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts


class ProdutoForm(ctk.CTkToplevel):

    def __init__(
        self,
        master,
        controller=None,
        produto=None
    ):

        super().__init__(master)

        self.controller = controller
        self.produto = produto
        self.image_path = None

        self.colors = ThemeManager.colors()

        # ==========================================
        # CONFIGURAÇÃO DA JANELA
        # ==========================================

        self.title(
            "Novo Produto"
            if produto is None
            else "Editar Produto"
        )

        self.geometry("900x850")

        self.minsize(900, 800)

        self.configure(
            fg_color=self.colors.BACKGROUND
        )

        # ==========================================
        # INTERFACE
        # ==========================================

        self.create_widgets()

        # ==========================================
        # CARREGAR PRODUTO
        # ==========================================

        if self.produto is not None:

            self.load_product_data()

        # ==========================================
        # MODAL
        # ==========================================

        self.transient(master)

        self.grab_set()

    # ==========================================================
    # ESTRUTURA
    # ==========================================================

    def create_widgets(self):

        self.create_header()

        self.create_basic_information()

        self.create_stock_information()

        self.create_price_information()

        self.create_observations()

        self.create_photo_section()

        self.create_footer()

    # ==========================================================
    # CABEÇALHO
    # ==========================================================

    def create_header(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=(25, 15)
        )

        titulo = ctk.CTkLabel(
            frame,
            text=(
                "Novo Produto"
                if self.produto is None
                else "Editar Produto"
            ),
            font=Fonts.title(),
            text_color=self.colors.TEXT
        )

        titulo.pack(
            anchor="w"
        )

        descricao = ctk.CTkLabel(
            frame,
            text="Preencha as informações do produto.",
            font=Fonts.body(),
            text_color=self.colors.TEXT_SECONDARY
        )

        descricao.pack(
            anchor="w",
            pady=(5, 0)
        )

    # ==========================================================
    # INFORMAÇÕES BÁSICAS
    # ==========================================================

    def create_basic_information(self):

        frame = ctk.CTkFrame(
            self,
            fg_color=self.colors.SURFACE,
            corner_radius=10
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        frame.grid_columnconfigure(
            0,
            weight=1
        )

        frame.grid_columnconfigure(
            1,
            weight=2
        )

        frame.grid_columnconfigure(
            2,
            weight=1
        )

        # ------------------------------------------
        # Código
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Código",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.codigo = ctk.CTkEntry(
            frame,
            placeholder_text="Ex.: CAM001"
        )

        self.codigo.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Nome
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Nome *",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.nome = ctk.CTkEntry(
            frame,
            placeholder_text="Nome do produto"
        )

        self.nome.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Categoria
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Categoria *",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.categoria = ctk.CTkComboBox(
            frame,
            values=[
                "Camisetas",
                "Calças",
                "Moletons",
                "Bonés",
                "Meias",
                "Casacos",
                "Outros"
            ]
        )

        self.categoria.grid(
            row=1,
            column=2,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Marca
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Marca",
            text_color=self.colors.TEXT
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=15,
            pady=(5, 5)
        )

        self.marca = ctk.CTkEntry(
            frame,
            placeholder_text="Ex.: ARYN"
        )

        self.marca.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Cor
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Cor",
            text_color=self.colors.TEXT
        ).grid(
            row=2,
            column=1,
            sticky="w",
            padx=15,
            pady=(5, 5)
        )

        self.cor = ctk.CTkEntry(
            frame,
            placeholder_text="Ex.: Preto"
        )

        self.cor.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Tamanho
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Tamanho",
            text_color=self.colors.TEXT
        ).grid(
            row=2,
            column=2,
            sticky="w",
            padx=15,
            pady=(5, 5)
        )

        self.tamanho = ctk.CTkComboBox(
            frame,
            values=[
                "PP",
                "P",
                "M",
                "G",
                "GG",
                "XG",
                "Único"
            ]
        )

        self.tamanho.grid(
            row=3,
            column=2,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

    # ==========================================================
    # ESTOQUE
    # ==========================================================

    def create_stock_information(self):

        frame = ctk.CTkFrame(
            self,
            fg_color=self.colors.SURFACE,
            corner_radius=10
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        frame.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        # ------------------------------------------
        # Quantidade
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Quantidade",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.quantidade = ctk.CTkEntry(frame)

        self.quantidade.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Estoque mínimo
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Estoque Mínimo",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.estoque_minimo = ctk.CTkEntry(frame)

        self.estoque_minimo.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Localização
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Localização",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.localizacao = ctk.CTkEntry(
            frame,
            placeholder_text="Ex.: A01-B03"
        )

        self.localizacao.grid(
            row=1,
            column=2,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Status
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Status",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=3,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.status = ctk.CTkComboBox(
            frame,
            values=[
                "Ativo",
                "Inativo"
            ]
        )

        self.status.set("Ativo")

        self.status.grid(
            row=1,
            column=3,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

    # ==========================================================
    # PREÇOS
    # ==========================================================

    def create_price_information(self):

        frame = ctk.CTkFrame(
            self,
            fg_color=self.colors.SURFACE,
            corner_radius=10
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        frame.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        # ------------------------------------------
        # Preço de custo
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Preço de Custo",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.preco_custo = ctk.CTkEntry(
            frame,
            placeholder_text="R$ 0,00"
        )

        self.preco_custo.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Preço de venda
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Preço de Venda",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.preco_venda = ctk.CTkEntry(
            frame,
            placeholder_text="R$ 0,00"
        )

        self.preco_venda.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        # ------------------------------------------
        # Margem
        # ------------------------------------------

        ctk.CTkLabel(
            frame,
            text="Margem de Lucro (%)",
            text_color=self.colors.TEXT
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        self.margem_lucro = ctk.CTkEntry(
            frame,
            placeholder_text="Calculada automaticamente",
            state="disabled"
        )

        self.margem_lucro.grid(
            row=1,
            column=2,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

        self.preco_custo.bind(
            "<KeyRelease>",
            lambda event: self.calculate_margin()
        )

        self.preco_venda.bind(
            "<KeyRelease>",
            lambda event: self.calculate_margin()
        )

    # ==========================================================
    # OBSERVAÇÕES
    # ==========================================================

    def create_observations(self):

        frame = ctk.CTkFrame(
            self,
            fg_color=self.colors.SURFACE,
            corner_radius=10
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        ctk.CTkLabel(
            frame,
            text="Observações",
            font=Fonts.body(),
            text_color=self.colors.TEXT
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        self.observacoes = ctk.CTkTextbox(
            frame,
            height=80,
            corner_radius=8
        )

        self.observacoes.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

    # ==========================================================
    # FOTO
    # ==========================================================

    def create_photo_section(self):

        frame = ctk.CTkFrame(
            self,
            fg_color=self.colors.SURFACE,
            corner_radius=10
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        ctk.CTkLabel(
            frame,
            text="Foto do Produto",
            font=Fonts.body(),
            text_color=self.colors.TEXT
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 10)
        )

        content = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        content.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        self.photo_label = ctk.CTkLabel(
            content,
            text="Nenhuma imagem selecionada",
            width=160,
            height=120,
            corner_radius=10,
            fg_color=self.colors.BACKGROUND,
            text_color=self.colors.TEXT_SECONDARY
        )

        self.photo_label.pack(
            side="left"
        )

        buttons = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        buttons.pack(
            side="left",
            padx=20
        )

        ctk.CTkButton(
            buttons,
            text="Selecionar Imagem",
            command=self.select_image
        ).pack(
            fill="x",
            pady=(0, 10)
        )

        ctk.CTkButton(
            buttons,
            text="Remover Imagem",
            fg_color=self.colors.ERROR,
            hover_color=self.colors.ERROR,
            command=self.remove_image
        ).pack(
            fill="x"
        )

    # ==========================================================
    # SELECIONAR IMAGEM
    # ==========================================================

    def select_image(self):

        caminho = filedialog.askopenfilename(
            title="Selecionar imagem",
            filetypes=[
                (
                    "Imagens",
                    "*.png *.jpg *.jpeg *.webp"
                )
            ]
        )

        if not caminho:
            return

        try:

            imagem_original = Image.open(caminho)

            imagem = ctk.CTkImage(
                light_image=imagem_original,
                dark_image=imagem_original,
                size=(160, 120)
            )

            self.image_path = caminho

            self.photo_label.configure(
                image=imagem,
                text=""
            )

            self.photo_label.image = imagem

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar a imagem.\n\n{erro}",
                parent=self
            )

    # ==========================================================
    # REMOVER IMAGEM
    # ==========================================================

    def remove_image(self):

        self.image_path = None

        self.photo_label.configure(
            image=None,
            text="Nenhuma imagem selecionada"
        )

        self.photo_label.image = None

    # ==========================================================
    # RODAPÉ
    # ==========================================================

    def create_footer(self):

        footer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        footer.pack(
            fill="x",
            padx=30,
            pady=20
        )

        buttons = ctk.CTkFrame(
            footer,
            fg_color="transparent"
        )

        buttons.pack(
            side="right"
        )

        self.btn_cancelar = ctk.CTkButton(
            buttons,
            text="Cancelar",
            width=140,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color=self.colors.BORDER,
            text_color=self.colors.TEXT,
            hover_color=self.colors.BUTTON_SECONDARY_HOVER,
            command=self.destroy
        )

        self.btn_cancelar.pack(
            side="left",
            padx=(0, 10)
        )

        self.btn_salvar = ctk.CTkButton(
            buttons,
            text="Salvar Produto",
            width=180,
            height=40,
            command=self.save_product
        )

        self.btn_salvar.pack(
            side="left"
        )

    # ==========================================================
    # CALCULAR MARGEM
    # ==========================================================

    def calculate_margin(self):

        try:

            custo = float(
                self.preco_custo.get()
                .replace(",", ".")
            )

            venda = float(
                self.preco_venda.get()
                .replace(",", ".")
            )

            if custo <= 0:

                return

            margem = (
                (venda - custo)
                / custo
            ) * 100

            self.margem_lucro.configure(
                state="normal"
            )

            self.margem_lucro.delete(
                0,
                "end"
            )

            self.margem_lucro.insert(
                0,
                f"{margem:.2f}%"
            )

            self.margem_lucro.configure(
                state="disabled"
            )

        except (ValueError, ZeroDivisionError):

            self.margem_lucro.configure(
                state="normal"
            )

            self.margem_lucro.delete(
                0,
                "end"
            )

            self.margem_lucro.configure(
                state="disabled"
            )

    # ==========================================================
    # OBTER DADOS DO FORMULÁRIO
    # ==========================================================

    def get_form_data(self):

        return {

            "codigo": self.codigo.get().strip(),

            "nome": self.nome.get().strip(),

            "categoria": self.categoria.get(),

            "marca": self.marca.get().strip(),

            "cor": self.cor.get().strip(),

            "tamanho": self.tamanho.get(),

            "quantidade": int(
                self.quantidade.get()
            ),

            "estoque_minimo": int(
                self.estoque_minimo.get()
            ),

            "localizacao": self.localizacao.get().strip(),

            "status": self.status.get(),

            "preco_custo": float(
                self.preco_custo.get()
                .replace(",", ".")
            ),

            "preco_venda": float(
                self.preco_venda.get()
                .replace(",", ".")
            ),

            "observacoes": self.observacoes.get(
                "1.0",
                "end"
            ).strip(),

            "imagem": self.image_path
        }

    # ==========================================================
    # VALIDAR FORMULÁRIO
    # ==========================================================

    def validate_form(self):

        # ------------------------------------------
        # Nome
        # ------------------------------------------

        if not self.nome.get().strip():

            self.show_error(
                "Informe o nome do produto."
            )

            return False

        # ------------------------------------------
        # Categoria
        # ------------------------------------------

        if not self.categoria.get():

            self.show_error(
                "Selecione uma categoria."
            )

            return False

        # ------------------------------------------
        # Quantidade
        # ------------------------------------------

        try:

            quantidade = int(
                self.quantidade.get()
            )

            if quantidade < 0:

                raise ValueError

        except ValueError:

            self.show_error(
                "Informe uma quantidade válida."
            )

            return False

        # ------------------------------------------
        # Estoque mínimo
        # ------------------------------------------

        try:

            estoque_minimo = int(
                self.estoque_minimo.get()
            )

            if estoque_minimo < 0:

                raise ValueError

        except ValueError:

            self.show_error(
                "Informe um estoque mínimo válido."
            )

            return False

        # ------------------------------------------
        # Preços
        # ------------------------------------------

        try:

            custo = float(
                self.preco_custo.get()
                .replace(",", ".")
            )

            venda = float(
                self.preco_venda.get()
                .replace(",", ".")
            )

            if custo < 0 or venda < 0:

                raise ValueError

        except ValueError:

            self.show_error(
                "Informe valores válidos para os preços."
            )

            return False

        # ------------------------------------------
        # Venda menor que custo
        # ------------------------------------------

        if venda < custo:

            resposta = messagebox.askyesno(
                "Atenção",
                "O preço de venda é menor que o preço de custo.\n\n"
                "Deseja continuar?",
                parent=self
            )

            if not resposta:

                return False

        return True

    # ==========================================================
    # SALVAR PRODUTO
    # ==========================================================

    def save_product(self):

        if self.controller is None:

            self.show_error(
                "Controller de produtos não foi configurado."
            )

            return

        if not self.validate_form():

            return

        try:

            dados = self.get_form_data()

            # ------------------------------------------
            # NOVO
            # ------------------------------------------

            if self.produto is None:

                self.controller.create_product(
                    dados
                )

            # ------------------------------------------
            # EDIÇÃO
            # ------------------------------------------

            else:

                produto_id = self.get_product_id()

                self.controller.update_product(
                    produto_id,
                    dados
                )

            messagebox.showinfo(
                "Sucesso",
                "Produto salvo com sucesso.",
                parent=self
            )

            self.destroy()

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível salvar o produto.\n\n{erro}",
                parent=self
            )

    # ==========================================================
    # ID DO PRODUTO
    # ==========================================================

    def get_product_id(self):

        if isinstance(self.produto, dict):

            return self.produto.get(
                "id"
            )

        return getattr(
            self.produto,
            "id",
            None
        )

    # ==========================================================
    # CARREGAR DADOS DO PRODUTO
    # ==========================================================

    def load_product_data(self):

        produto = self.produto

        def get_value(
            key,
            default=""
        ):

            if isinstance(produto, dict):

                return produto.get(
                    key,
                    default
                )

            return getattr(
                produto,
                key,
                default
            )

        self.codigo.insert(
            0,
            str(
                get_value(
                    "codigo",
                    ""
                )
            )
        )

        self.nome.insert(
            0,
            str(
                get_value(
                    "nome",
                    ""
                )
            )
        )

        self.categoria.set(
            str(
                get_value(
                    "categoria",
                    ""
                )
            )
        )

        self.marca.insert(
            0,
            str(
                get_value(
                    "marca",
                    ""
                )
            )
        )

        self.cor.insert(
            0,
            str(
                get_value(
                    "cor",
                    ""
                )
            )
        )

        self.tamanho.set(
            str(
                get_value(
                    "tamanho",
                    ""
                )
            )
        )

        self.quantidade.insert(
            0,
            str(
                get_value(
                    "quantidade",
                    0
                )
            )
        )

        self.estoque_minimo.insert(
            0,
            str(
                get_value(
                    "estoque_minimo",
                    0
                )
            )
        )

        self.localizacao.insert(
            0,
            str(
                get_value(
                    "localizacao",
                    ""
                )
            )
        )

        self.status.set(
            str(
                get_value(
                    "status",
                    "Ativo"
                )
            )
        )

        self.preco_custo.insert(
            0,
            str(
                get_value(
                    "preco_custo",
                    0
                )
            )
        )

        self.preco_venda.insert(
            0,
            str(
                get_value(
                    "preco_venda",
                    0
                )
            )
        )

        observacoes = get_value(
            "observacoes",
            ""
        )

        self.observacoes.insert(
            "1.0",
            str(observacoes)
        )

        imagem = get_value(
            "imagem",
            None
        )

        if imagem:

            try:

                imagem_original = Image.open(
                    imagem
                )

                imagem_ctk = ctk.CTkImage(
                    light_image=imagem_original,
                    dark_image=imagem_original,
                    size=(160, 120)
                )

                self.image_path = imagem

                self.photo_label.configure(
                    image=imagem_ctk,
                    text=""
                )

                self.photo_label.image = imagem_ctk

            except Exception:

                pass

        self.calculate_margin()

    # ==========================================================
    # MENSAGEM DE ERRO
    # ==========================================================

    def show_error(self, mensagem):

        messagebox.showerror(
            "Erro",
            mensagem,
            parent=self
        )