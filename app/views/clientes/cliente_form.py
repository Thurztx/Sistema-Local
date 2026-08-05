import customtkinter as ctk

from theme.theme_manager import ThemeManager
from theme.fonts import Fonts

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

    def create_header(self):
        pass


    def create_personal_information(self):
        pass


    def create_contact_information(self):
        pass


    def create_address_information(self):
        pass


    def create_observations(self):
        pass


    def create_footer(self):
        pass

