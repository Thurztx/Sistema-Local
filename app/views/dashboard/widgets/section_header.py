import customtkinter as ctk

from app.theme.fonts import Fonts
from app.theme.theme_manager import ThemeManager


class SectionHeader(ctk.CTkFrame):

    def __init__(self, master, title):

        colors = ThemeManager.colors()

        super().__init__(
            master,
            fg_color="transparent"
        )

        label = ctk.CTkLabel(
            self,
            text=title,
            font=Fonts.H3,
            text_color=colors.TEXT
        )

        label.pack(anchor="w")