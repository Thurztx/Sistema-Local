import customtkinter as ctk
import os
import customtkinter as ctk

from tkinter import messagebox
from PIL import Image
from tkinter import filedialog
from theme.theme_manager import ThemeManager
from theme.fonts import Fonts

class ProdutoForm(ctk.CTkToplevel):

    def __init__(self, master, controller=None, produto=None):
        super().__init__(master)

        self.controller = controller
        self.produto = produto

        self.colors = ThemeManager.colors()

        self.title(
            "Novo Produto"
            if produto is None
            else "Editar Produto"
        )

        self.geometry("900x700")

        self.resizable(False, False)

        self.configure(
            fg_color=self.colors.BACKGROUND
        )

        self.create_widgets()

        self.grab_set()

    # Estrutura Principal
    def create_widgets(self):

        self.create_header()

        self.create_basic_information()

        self.create_stock_information()

        self.create_price_information()

        self.create_footer()

    # Cabeçalho
    def create_header(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        titulo = ctk.CTkLabel(
            frame,
            text="Cadastro de Produto",
            font=Fonts.H1
        )

        titulo.pack(anchor="w")

        descricao = ctk.CTkLabel(
            frame,
            text="Preencha as informações abaixo.",
            font=Fonts.BODY
        )

        descricao.pack(anchor="w")

    # Informações Básicas
    def create_basic_information(self):

        frame = ctk.CTkFrame(self)

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

    # Código
        ctk.CTkLabel(frame, text="Código").grid(row=0,column=0,padx=10,pady=10)
        self.codigo = ctk.CTkEntry(frame)
        self.codigo.grid(row=1,column=0,padx=10)

    # Nome
        ctk.CTkLabel(frame,text="Nome").grid(row=0,column=1)
        self.nome = ctk.CTkEntry(frame,width=350)
        self.nome.grid(row=1,column=1,padx=10)

    # Categoria
        self.categoria = ctk.CTkComboBox(
            frame,
            values=[
                "Camisetas",
                "Calças",
                "Moletons",
                "Bonés"
            ]
        )

    # Marca
        self.marca = ctk.CTkEntry(frame)

    # Cor
        self.cor = ctk.CTkEntry(frame)

    # Tamanho
        self.tamanho = ctk.CTkComboBox(

            frame,

            values=[
                "PP",
                "P",
                "M",
                "G",
                "GG",
                "XG"
            ]
        )   

    # Estoque
    def create_stock_information(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Quantidade
        lbl_quantidade = ctk.CTkLabel(
            frame,
            text="Quantidade"
        )

        lbl_quantidade.grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=(10,5)
        )

        self.quantidade = ctk.CTkEntry(frame)

        self.quantidade.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=10
        )

        # Estoque Mínimo
        lbl_minimo = ctk.CTkLabel(
            frame,
            text="Estoque Mínimo"
        )

        lbl_minimo.grid(
            row=0,
            column=1,
            sticky="w",
            padx=10,
            pady=(10,5)
        )

        self.estoque_minimo = ctk.CTkEntry(frame)

        self.estoque_minimo.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=10
        )

        # Localização
        lbl_localizacao = ctk.CTkLabel(
            frame,
            text="Localização"
        )

        lbl_localizacao.grid(
            row=0,
            column=2,
            sticky="w",
            padx=10,
            pady=(10,5)
        )

        self.localizacao = ctk.CTkEntry(
            frame,
            placeholder_text="Ex.: A01-B03"
        )

        self.localizacao.grid(
            row=1,
            column=2,
            sticky="ew",
            padx=10
        )

        # Status
        lbl_status = ctk.CTkLabel(
            frame,
            text="Status"
        )

        lbl_status.grid(
            row=0,
            column=3,
            sticky="w",
            padx=10,
            pady=(10,5)
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
            padx=10
        )

    # Valolres
    def create_price_information(self):

        #FRAME
        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )   

        frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Preço de Custo
        lbl_custo = ctk.CTkLabel(
            frame,
            text="Preço de Custo"
        )

        lbl_custo.grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=(10,5)
        )

        self.preco_custo = ctk.CTkEntry(
            frame,
            placeholder_text="R$ 0,00"
        )

        self.preco_custo.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=10
        )

        # Preço de Venda
        lbl_venda = ctk.CTkLabel(
            frame,
            text="Preço de Venda"
        )

        lbl_venda.grid(
            row=0,
            column=1,
            sticky="w",
            padx=10,
            pady=(10,5)
        )

        self.preco_venda = ctk.CTkEntry(
            frame,
            placeholder_text="R$ 0,00"
        )

        self.preco_venda.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=10
        )

        # Margem de Lucro
        lbl_margem = ctk.CTkLabel(
            frame,
            text="Margem de Lucro (%)"
        )

        lbl_margem.grid(
            row=0,
            column=2,
            sticky="w",
            padx=10,
            pady=(10,5)
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
            padx=10
        )

    # Observações
    def create_observations(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # Título da seção
        lbl_observacoes = ctk.CTkLabel(
            frame,
            text="Observações",
            font=Fonts.BODY
        )

        lbl_observacoes.pack(
            anchor="w",
            pady=(10, 5)
        )

        # Campo de texto
        self.observacoes = ctk.CTkTextbox(
            frame,
            height=120,
            corner_radius=8,
            wrap="word"
        )

        self.observacoes.pack(
            fill="both",
            expand=True,
            pady=(0, 10)
        )

        # Texto de ajuda
        lbl_info = ctk.CTkLabel(
            frame,
            text="Ex.: Material, coleção, instruções de armazenamento ou outras informações relevantes.",
            font=Fonts.SMALL,
            text_color=self.colors.TEXT_SECONDARY
        )

        lbl_info.pack(
            anchor="w"
        )

    # Foto
    def create_photo_section(self):

        # FRAME
        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Título do Frame
        titulo = ctk.CTkLabel(
            frame,
            text="Foto do Produto",
            font=Fonts.BODY
        )

        titulo.pack(anchor="w", pady=(0, 10))


        self.photo_label = ctk.CTkLabel(
            frame,
            text="Nenhuma imagem selecionada",
            width=180,
            height=180,
            corner_radius=10
        )

        self.photo_label.pack(side="left")

        # Frame para os Botões
        botoes = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        botoes.pack(side="left", padx=20)

        # Botão "Selecionar Imagem"
        ctk.CTkButton(
            botoes,
            text="Selecionar Imagem",
            command=self.select_image
        ).pack(fill="x", pady=(0, 10))

        # Botão "Remover Imagem"
        ctk.CTkButton(
            botoes,
            text="Remover Imagem",
            fg_color="#B22222",
            hover_color="#8B1A1A",
            command=self.remove_image
        ).pack(fill="x")

        self.image_path = None

    # Método para Selecionar Imagem
    def select_image(self):

        caminho = filedialog.askopenfilename(

            title="Selecionar imagem",

            filetypes=[
                ("Imagens", "*.png *.jpg *.jpeg *.webp")
            ]

        )

        if not caminho:
            return

        self.image_path = caminho

        imagem = ctk.CTkImage(
            light_image=Image.open(caminho),
            dark_image=Image.open(caminho),
            size=(180, 180)
        )

        self.photo_label.configure(
            image=imagem,
            text=""
        )   

        self.photo_label.image = imagem

    # Método para Remover Imagem
    def remove_image(self):

        self.image_path = None

        self.photo_label.configure(
            image=None,
            text="Nenhuma imagem selecionada"
        )

    # Método para Salvar a Imagem no Banco
    dados = {
        ...,
        "imagem": self.image_path
    }

#   <--- Rodapé --->
    def create_footer(self):

        footer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        footer.pack(
            fill="x",
            padx=20,
            pady=(20, 20)
        )

        footer.grid_columnconfigure(0, weight=1)

        buttons_frame = ctk.CTkFrame(
            footer,
            fg_color="transparent"
        )

        buttons_frame.grid(
            row=0,
            column=1,
            sticky="e"
        )

        self.btn_cancelar = ctk.CTkButton(
            buttons_frame,
            text="Cancelar",
            width=140,
            height=40,
            fg_color="transparent",
            border_width=1,
            command=self.destroy
        )

        self.btn_cancelar.pack(
            side="left",
            padx=(0, 10)
        )

        self.btn_salvar = ctk.CTkButton(
            buttons_frame,
            text="Salvar Produto",
            width=180,
            height=40,
            command=self.save_product
        )

        self.btn_salvar.pack(
            side="left"
        )

# <--- SALVAR --->
    def save_product(self):

        if not self.validate_form():
            return

        dados = self.get_form_data()

        try:

            if self.produto is None:

                self.controller.create_product(dados)

            else:

                self.controller.update_product(
                    self.produto.id,
                    dados
                )

            self.destroy()

        except Exception as erro:

            ctk.CTkMessagebox(
                title="Erro",
                message=str(erro),
                icon="cancel"
            )

    # Método para a Centralização da Leitura do Formulário
    def get_form_data(self):

        return {

            "codigo": self.codigo.get().strip(),

            "nome": self.nome.get().strip(),

            "categoria": self.categoria.get(),

            "marca": self.marca.get().strip(),

            "cor": self.cor.get().strip(),

            "tamanho": self.tamanho.get(),

            "quantidade": int(self.quantidade.get()),

            "estoque_minimo": int(self.estoque_minimo.get()),

            "localizacao": self.localizacao.get().strip(),

            "status": self.status.get(),

            "preco_custo": float(
            self.preco_custo.get().replace(",", ".")
            ),

            "preco_venda": float(
            self.preco_venda.get().replace(",", ".")
            ),

            "observacoes": self.observacoes.get(
                "1.0",
                "end"
            ).strip(),

            "imagem": self.image_path

        }
    
    # Método de Validação
    def validate_form(self):

        if not self.nome.get().strip():

            self.show_error(
                "Informe o nome do produto."
            )

            return False

        if not self.categoria.get():

            self.show_error(
                "Selecione uma categoria."
            )

            return False

        try:

            quantidade = int(
                self.quantidade.get()
            )

            if quantidade < 0:

                raise ValueError

        except ValueError:

            self.show_error(
                "Quantidade inválida."
            )

            return False

        try:

            custo = float(
                self.preco_custo.get().replace(",", ".")
            )

            venda = float(
                self.preco_venda.get().replace(",", ".")
            )

            if custo < 0 or venda < 0:

                raise ValueError

        except ValueError:

            self.show_error(
                "Valores inválidos."
            )

            return False

        return True

    # Método de Erro
    def show_error(self, mensagem):

        messagebox.showerror(
            "Erro",
            mensagem
        )

    # Atualizando o botão
        self.btn_salvar = ctk.CTkButton(

            buttons_frame,

            text="Salvar Produto",

            command=self.save_product
        )