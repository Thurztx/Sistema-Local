import customtkinter as ctk


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Controle de Estoque")
        self.geometry("1700x900")

        self.criar_interface()

    def criar_interface(self):
        pass