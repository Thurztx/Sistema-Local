import customtkinter as ctk

from theme.theme_manager import ThemeManager
from theme.fonts import Fonts

# Classe Principal
class ClienteForm(ctk.CTkToplevel):

    def __init__(self, master, controller=None, cliente=None):
        super().__init__(master)

        self.controller = controller
        self.cliente = cliente

        self.colors = ThemeManager.colors()

        self.configure_window()

        self.create_widgets()

        self.center_window()

        self.grab_set()

    # Método que Concentra Todas as Config da Janela
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