import customtkinter as ctk

from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts


class StatCard(ctk.CTkFrame):

    def __init__(self, master, icon, title, value):

        colors = ThemeManager.colors()

        super().__init__(
            master,
            fg_color=colors.SURFACE,
            corner_radius=12
        )

        self.grid_columnconfigure(1, weight=1)

        self.icon = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 28)
        )
        self.icon.grid(row=0, column=0, rowspan=2, padx=20, pady=20)

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=Fonts.SMALL,
            text_color=colors.TEXT_SECONDARY
        )
        self.title.grid(row=0, column=1, sticky="w", pady=(20, 0))

        self.value = ctk.CTkLabel(
            self,
            text=value,
            font=Fonts.H2,
            text_color=colors.TEXT
        )
        self.value.grid(row=1, column=1, sticky="w", pady=(0, 20))