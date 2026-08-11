import re
from datetime import datetime
from tkinter import messagebox

import customtkinter as ctk

from app.controllers.cliente_controller import ClienteController
from theme.theme_manager import ThemeManager
from theme.fonts import Fonts

class ClienteForm(ctk.CTkToplevel):

    def __init__(self, 
                 master, 
                 controller=None, 
                 cliente=None,
                 on_saved=None
    ):
        super().__init__(master)

        self.controller = controller
        self.cliente = cliente
        self.on_saved=None

        self.colors = ThemeManager.colors()

        self.configure_window()

        self.create_widgets()

        self.center_window()

        self.grab_set()

        if self.cliente is not None:
            self.load_client()

        if self.on_saved:
            self.on_saved()

        self.destroy()

    def configure_window(self):

        if self.cliente is None:
            self.title("Cadastro de Cliente")
        else:
            self.title("Editar Cliente")

        self.geometry("1000x750")

        self.minsize(900, 700)

        self.resizable(True, True)

        self.configure(
            fg_color=self.colors.BACKGROUND
        )

    def center_window(self):

        self.update_idletasks()

        width = 1000
        height = 750

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(1, weight=1)

        self.create_header()

        self.create_personal_information()

        self.create_contact_information()

        self.create_address_information()

        self.create_observations()

        self.create_footer()

    def create_header(self):

        self.header_frame = ctk.CTkFrame(
        self,
        fg_color="transparent"
        )

        self.header_frame.pack(
        fill="x",
        padx=20,
        pady=(20, 10)
        )

        if self.cliente is None:
            titulo = "Cadastro de Cliente"
            descricao = "Cadastre um novo cliente no sistema."
        else:
            titulo = "Editar Cliente"
            descricao = "Atualize as informações do cliente."

        self.lbl_title = ctk.CTkLabel(
            self.header_frame,
            text=titulo,
            font=Fonts.H1,
            text_color=self.colors.TEXT
        )

        self.lbl_title.pack(
            anchor="w"
        )

        self.lbl_description = ctk.CTkLabel(
            self.header_frame,
            text=descricao,
            font=Fonts.BODY,
            text_color=self.colors.TEXT_SECONDARY
        )

        self.lbl_description.pack(
            anchor="w",
            pady=(5, 0)
        )

        self.separator = ctk.CTkFrame(
            self,
            height=2,
            fg_color=self.colors.BORDER
        )

        self.separator.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

    def create_personal_information(self):

    # Container da seção
        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

    # =================
    # Título da seção
    # ================= 
        section_title = ctk.CTkLabel(
            frame,
            text="Informações Pessoais",
            font=Fonts.H2,
            text_color=self.colors.TEXT
        )

        section_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10,
            pady=(5, 15)
        )

    
        # Nome Completo
        lbl_nome = ctk.CTkLabel(
            frame,
            text="Nome Completo"
        )

        lbl_nome.grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.nome = ctk.CTkEntry(
            frame,
            placeholder_text="Digite o nome completo",
            height=40
        )

        self.nome.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    
        # CPF
        lbl_cpf = ctk.CTkLabel(
            frame,
            text="CPF"
        )

        lbl_cpf.grid(
            row=1,
            column=1,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.cpf = ctk.CTkEntry(
            frame,
            placeholder_text="000.000.000-00",
            height=40
        )

        self.cpf.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

        
        # Data de Nascimento
        lbl_data_nascimento = ctk.CTkLabel(
            frame,
            text="Data de Nascimento"
        )

        lbl_data_nascimento.grid(
            row=3,
            column=0,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.data_nascimento = ctk.CTkEntry(
            frame,
            placeholder_text="DD/MM/AAAA",
            height=40
        )

        self.data_nascimento.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    
        # Gênero
        lbl_genero = ctk.CTkLabel(
            frame,
            text="Gênero"
        )

        lbl_genero.grid(
            row=3,
            column=1,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.genero = ctk.CTkComboBox(
            frame,
            values=[
                "Masculino",
                "Feminino",
                "Outro",
                "Prefiro não informar"
            ],
            height=40
        )

        self.genero.set("Prefiro não informar")

        self.genero.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

# INFORMAÇÕES DE CONTATO
    def create_contact_information(self):

    # Container da seção
        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

   
    # Título da seção
        section_title = ctk.CTkLabel(
            frame,
            text="Contato",
            font=Fonts.H2,
            text_color=self.colors.TEXT
        )

        section_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10,
            pady=(5, 15)
        )

    
        # E-mail
   

        lbl_email = ctk.CTkLabel(
            frame,
            text="E-mail"
        )

        lbl_email.grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.email = ctk.CTkEntry(
            frame,
            placeholder_text="exemplo@email.com",
            height=40
        )

        self.email.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    
        # Telefone
   

        lbl_telefone = ctk.CTkLabel(
            frame,
            text="Telefone"
        )

        lbl_telefone.grid(
            row=1,
            column=1,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.telefone = ctk.CTkEntry(
            frame,
            placeholder_text="(00) 00000-0000",
            height=40
        )

        self.telefone.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )


    def create_address_information(self):

    # Container da seção
        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

    # Título da seção
        section_title = ctk.CTkLabel(
            frame,
            text="Endereço",
            font=Fonts.H2,
            text_color=self.colors.TEXT
        )

        section_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10,
            pady=(5, 15)
        )

    # CEP
        lbl_cep = ctk.CTkLabel(
            frame,
            text="CEP"
        )

        lbl_cep.grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.cep = ctk.CTkEntry(
            frame,
            placeholder_text="00000-000",
            height=40
        )

        self.cep.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    # Estado
        lbl_estado = ctk.CTkLabel(
            frame,
            text="Estado"
        )

        lbl_estado.grid(
            row=1,
            column=1,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.estado = ctk.CTkComboBox(
            frame,
            values=[
                "AC",
                "AL",
                "AP",
                "AM",
                "BA",
                "CE",
                "DF",
                "ES",
                "GO",
                "MA",
                "MT",
                "MS",
                "MG",
                "PA",
                "PB",
                "PR",
                "PE",
                "PI",
                "RJ",
                "RN",
                "RS",
                "RO",
                "RR",
                "SC",
                "SP",
                "SE",
                "TO"
            ],
            height=40
        )

        self.estado.set("RS")

        self.estado.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    # Cidade
        lbl_cidade = ctk.CTkLabel(
            frame,
            text="Cidade"
        )

        lbl_cidade.grid(
            row=3,
            column=0,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.cidade = ctk.CTkEntry(
            frame,
            placeholder_text="Digite a cidade",
            height=40
        )

        self.cidade.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    # Bairro
        lbl_bairro = ctk.CTkLabel(
            frame,
            text="Bairro"
        )

        lbl_bairro.grid(
            row=3,
            column=1,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.bairro = ctk.CTkEntry(
            frame,
            placeholder_text="Digite o bairro",
            height=40
        )

        self.bairro.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    # Rua
        lbl_rua = ctk.CTkLabel(
            frame,
            text="Rua"
        )

        lbl_rua.grid(
            row=5,
            column=0,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.rua = ctk.CTkEntry(
            frame,
            placeholder_text="Digite o nome da rua",
            height=40
        )

        self.rua.grid(
            row=6,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    # Número
        lbl_numero = ctk.CTkLabel(
            frame,
            text="Número"
        )

        lbl_numero.grid(
            row=5,
            column=1,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.numero = ctk.CTkEntry(
            frame,
            placeholder_text="Ex.: 123",
            height=40
        )

        self.numero.grid(
            row=6,
            column=1,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

    # Complemento
        lbl_complemento = ctk.CTkLabel(
            frame,
            text="Complemento"
        )

        lbl_complemento.grid(
            row=7,
            column=0,
            sticky="w",
            padx=10,
            pady=(0, 5)
        )

        self.complemento = ctk.CTkEntry(
            frame,
            placeholder_text="Apartamento, sala, casa, etc.",
            height=40
        )

        self.complemento.grid(
            row=8,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

# OBSERVAÇÕES
    def create_observations(self):

    # Frame principal
        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        frame.grid_columnconfigure(0, weight=1)

        # Título
        section_title = ctk.CTkLabel(
            frame,
            text="Observações",
            font=Fonts.H2,
            text_color=self.colors.TEXT
        )

        section_title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=(5, 10)
        )

        # Campo de Observações
        self.observacoes = ctk.CTkTextbox(
            frame,
            height=120,
            corner_radius=8,
            wrap="word"
        )

        self.observacoes.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0, 5)
        )

        # Informações auxiuliares
        self.lbl_observacoes_info = ctk.CTkLabel(
            frame,
            text="0/500 caracteres",
            font=Fonts.SMALL,
            text_color=self.colors.TEXT_SECONDARY
        )

        self.lbl_observacoes_info.grid(
            row=2,
            column=0,
            sticky="e",
            padx=10,
            pady=(0, 5)
        )

        self.observacoes.bind(
            "<KeyRelease>",
            self.update_observations_counter
        )

# RODAPÉ
    def create_footer(self):

    # Container do rodapé
        footer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        footer.pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )

        footer.grid_columnconfigure(
            0,
            weight=1
        )

    # Linha separadora
        separator = ctk.CTkFrame(
            footer,
            height=1,
            fg_color=self.colors.BORDER
        )

        separator.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 15)
        )

    # Container dos botões
        buttons_frame = ctk.CTkFrame(
            footer,
            fg_color="transparent"
        )

        buttons_frame.grid(
            row=1,
            column=0,
            sticky="e"
        )

    # Botão Cancelar
        self.btn_cancelar = ctk.CTkButton(
            buttons_frame,
            text="Cancelar",
            width=140,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color=self.colors.BORDER,
            text_color=self.colors.TEXT,
            hover_color=self.colors.SURFACE,
            command=self.cancel
        )

        self.btn_cancelar.pack(
            side="left",
            padx=(0, 10)
        )

    # Texto do botão Salvar
        if self.cliente is None:
            texto_salvar = "Salvar Cliente"
        else:
            texto_salvar = "Salvar Alterações"

    # Botão Salvar
        self.btn_salvar = ctk.CTkButton(
            buttons_frame,
            text=texto_salvar,
            width=180,
            height=40,
            command=self.save_client
        )

        self.btn_salvar.pack(
            side="left"
        )

    # VALIDAÇÃO FORM
    def validate_form(self):

        # ==========================================
        # Nome
        # ==========================================

        nome = self.nome.get().strip()

        if not nome:
            self.show_error(
                "Informe o nome completo do cliente.",
                self.nome
            )
            return False

        if len(nome) < 3:
            self.show_error(
                "O nome do cliente deve possuir pelo menos 3 caracteres.",
                self.nome
            )
            return False

        # ==========================================
        # CPF
        # ==========================================

        cpf = self.cpf.get().strip()

        if not cpf:
            self.show_error(
                "Informe o CPF do cliente.",
                self.cpf
            )
            return False

        if not self.validate_cpf(cpf):
            self.show_error(
                "Informe um CPF válido.",
                self.cpf
            )
            return False

        # ==========================================
        # Data de nascimento
        # ==========================================

        data_nascimento = self.data_nascimento.get().strip()

        if not data_nascimento:
            self.show_error(
                "Informe a data de nascimento.",
                self.data_nascimento
            )
            return False

        if not self.validate_birth_date(data_nascimento):
            self.show_error(
                "Informe uma data de nascimento válida no formato DD/MM/AAAA.",
                self.data_nascimento
            )
            return False

        # ==========================================
        # Gênero
        # ==========================================

        genero = self.genero.get().strip()

        if not genero:
            self.show_error(
                "Selecione o gênero do cliente.",
                self.genero
            )
            return False

        # ==========================================
        # E-mail
        # ==========================================

        email = self.email.get().strip()

        if email and not self.validate_email(email):
            self.show_error(
                "Informe um endereço de e-mail válido.",
                self.email
            )
            return False

        # ==========================================
        # Telefone
        # ==========================================

        telefone = self.telefone.get().strip()

        if not telefone:
            self.show_error(
                "Informe o telefone do cliente.",
                self.telefone
            )
            return False

        if not self.validate_phone(telefone):
            self.show_error(
                "Informe um telefone válido.",
                self.telefone
            )
            return False

        # ==========================================
        # CEP
        # ==========================================

        cep = self.cep.get().strip()

        if not cep:
            self.show_error(
                "Informe o CEP.",
                self.cep
            )
            return False

        if not self.validate_cep(cep):
            self.show_error(
                "Informe um CEP válido.",
                self.cep
            )
            return False

        # ==========================================
        # Estado
        # ==========================================

        estado = self.estado.get().strip()

        if not estado:
            self.show_error(
                "Selecione o estado.",
                self.estado
            )
            return False

        # ==========================================
        # Cidade
        # ==========================================

        cidade = self.cidade.get().strip()

        if not cidade:
            self.show_error(
                "Informe a cidade.",
                self.cidade
            )
            return False

        # ==========================================
        # Bairro
        # ==========================================

        bairro = self.bairro.get().strip()

        if not bairro:
            self.show_error(
                "Informe o bairro.",
                self.bairro
            )
            return False

        # ==========================================
        # Rua
        # ==========================================

        rua = self.rua.get().strip()

        if not rua:
            self.show_error(
                "Informe a rua.",
                self.rua
            )
            return False

        # ==========================================
        # Número
        # ==========================================

        numero = self.numero.get().strip()

        if not numero:
            self.show_error(
                "Informe o número do endereço.",
                self.numero
            )
            return False

        # ==========================================
        # Observações
        # ==========================================

        observacoes = self.observacoes.get(
            "1.0",
            "end-1c"
        ).strip()

        if len(observacoes) > 500:
            self.show_error(
                "As observações podem possuir no máximo 500 caracteres.",
                self.observacoes
            )
            return False

        return True

# VALIDAÇÃO CPF
    def validate_cpf(self, cpf):

        cpf = re.sub(
            r"\D",
            "",
            cpf
        )

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma = 0

        for i in range(9):
            soma += int(cpf[i]) * (10 - i)

        resto = soma % 11

        digito_1 = 0 if resto < 2 else 11 - resto

        if int(cpf[9]) != digito_1:
            return False

        soma = 0

        for i in range(10):
            soma += int(cpf[i]) * (11 - i)

        resto = soma % 11

        digito_2 = 0 if resto < 2 else 11 - resto

        if int(cpf[10]) != digito_2:
            return False

        return True
    
# VALIDAÇÃO CPF
    def validate_birth_date(self, date_text):

        try:

            data = datetime.strptime(
                date_text,
                "%d/%m/%Y"
            )

            if data.date() > datetime.today().date():
                return False

            return True

        except ValueError:

            return False
        
# VALIDAÇÃO TELEFONE
    def validate_phone(self, telefone):

        digits = re.sub(
            r"\D",
            "",
            telefone
        )

        return len(digits) in (10, 11)
    
# VALIDAÇÃO CEP
    def validate_cep(self, cep):

        digits = re.sub(
            r"\D",
            "",
            cep
        )

        return len(digits) == 8
    
# EXIBIÇÃO DE ERRO
    def show_error(self, message, widget=None):

        messagebox.showerror(
            "Dados inválidos",
            message,
            parent=self
        )

        if widget is not None:

            try:
                widget.focus_set()
            except Exception:
                pass

    def save_client(self):

        # ==========================================
        # Validação
        # ==========================================

        if not self.validate_form():
            return

        # ==========================================
        # Verificar Controller
        # ==========================================

        if self.controller is None:

            self.show_error(
                "O controlador de clientes não foi configurado."
            )

            return

        # ==========================================
        # Obter dados
        # ==========================================

        dados = self.get_form_data()

        # ==========================================
        # Desabilitar botão
        # ==========================================

        self.btn_salvar.configure(
            state="disabled"
        )

        try:

            # ======================================
            # Cadastro
            # ======================================

            if self.cliente is None:

                self.controller.create_client(
                    dados
                )

                messagebox.showinfo(
                    "Sucesso",
                    "Cliente cadastrado com sucesso!",
                    parent=self
                )

            # ======================================
            # Edição
            # ======================================

            else:

                self.controller.update_client(
                    self.cliente.id,
                    dados
                )

                messagebox.showinfo(
                    "Sucesso",
                    "Cliente atualizado com sucesso!",
                    parent=self
                )

            # ======================================
            # Fechar formulário
            # ======================================
        
            if self.on_saved is not None:
                self.on_saved()

            self.destroy()

        except Exception as erro:

            self.btn_salvar.configure(
                state="normal"
            )

            messagebox.showerror(
                "Erro",
                f"Não foi possível salvar o cliente.\n\n{erro}",
                parent=self
            )

    def get_form_data(self):

        return {
            "nome": self.nome.get().strip(),

            "cpf": self.cpf.get().strip(),

            "data_nascimento": self.format_birth_date_for_database(
                self.data_nascimento.get().strip()
            ),

            "genero": self.genero.get().strip(),

            "email": self.email.get().strip(),

            "telefone": self.telefone.get().strip(),

            "cep": self.cep.get().strip(),

            "estado": self.estado.get().strip(),

            "cidade": self.cidade.get().strip(),

            "bairro": self.bairro.get().strip(),

            "rua": self.rua.get().strip(),

            "numero": self.numero.get().strip(),

            "complemento": self.complemento.get().strip(),

            "observacoes": self.observacoes.get(
                "1.0",
                "end-1c"
            ).strip()
        }
        
    def load_client(self):

        self.nome.insert(
            0,
            self.cliente.nome or ""
        )

        self.cpf.insert(
            0,
            self.cliente.cpf or ""
        )

        self.data_nascimento.insert(
            0,
            self.format_birth_date_for_form(
                self.cliente.data_nascimento
            )
        )

        self.genero.set(
            self.cliente.genero or ""
        )

        self.email.insert(
            0,
            self.cliente.email or ""
        )

        self.telefone.insert(
            0,
            self.cliente.telefone or ""
        )

        self.cep.insert(
            0,
            self.cliente.cep or ""
        )

        self.estado.set(
            self.cliente.estado or ""
        )

        self.cidade.insert(
            0,
            self.cliente.cidade or ""
        )

        self.bairro.insert(
            0,
            self.cliente.bairro or ""
        )

        self.rua.insert(
            0,
            self.cliente.rua or ""
        )

        self.numero.insert(
            0,
            self.cliente.numero or ""
        )

        self.complemento.insert(
            0,
            self.cliente.complemento or ""
        )

        self.observacoes.insert(
            "1.0",
            self.cliente.observacoes or ""
        )

        self.update_observations_counter()

    def format_birth_date_for_form(self, value):

        if not value:
            return ""

        if isinstance(value, datetime):
            return value.strftime("%d/%m/%Y")

        try:

            data = datetime.strptime(
                str(value),
                "%Y-%m-%d"
            )

            return data.strftime("%d/%m/%Y")

        except ValueError:

            return str(value)
        
    def format_birth_date_for_database(self, value):

        if not value:
            return None

        data = datetime.strptime(
            value,
            "%d/%m/%Y"
        )

        return data.strftime(
            "%Y-%m-%d"
        )