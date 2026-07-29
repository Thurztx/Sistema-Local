def criar_interface(self):
    titulo = ctk.CTkLabel(
        self,
        text="Sistema de Controle de Estoque",
        font=("Segoe UI", 28, "bold")
    )

    titulo.pack(pady=40)

    botao = ctk.CTkButton(
        self,
        text="Produtos"
    )

    botao.pack()