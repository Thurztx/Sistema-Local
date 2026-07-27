import customtkinter as ctk

from components.sidebar import Sidebar
from components.navbar import Navbar

from app.theme.theme_manager import ThemeManager


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Controle de Estoque")

        self.geometry("1600x900")

        self.minsize(1200, 700)

        colors = ThemeManager.colors()

        self.configure(
            fg_color=colors.BACKGROUND
        )

        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(1, weight=1)

        self.navbar = Navbar(self)

        self.navbar.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="ns"
        )

        self.content = ctk.CTkFrame(
            self,
            fg_color=colors.BACKGROUND,
            corner_radius=0
        )

        self.content.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )