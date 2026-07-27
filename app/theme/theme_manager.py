import customtkinter as ctk

from .colors import Colors, DarkColors


class ThemeManager:

    _dark = False

    @classmethod
    def set_dark(cls):

        cls._dark = True

        ctk.set_appearance_mode("dark")

    @classmethod
    def set_light(cls):

        cls._dark = False

        ctk.set_appearance_mode("light")

    @classmethod
    def toggle(cls):

        if cls._dark:
            cls.set_light()
        else:
            cls.set_dark()

    @classmethod
    def colors(cls):

        return DarkColors if cls._dark else Colors

    @classmethod
    def is_dark(cls):

        return cls._dark