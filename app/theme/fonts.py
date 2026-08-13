import customtkinter as ctk


class Fonts:

    # ==========================================
    # TÍTULO
    # ==========================================

    @staticmethod
    def title():

        return ctk.CTkFont(
            size=28,
            weight="bold"
        )

    # ==========================================
    # SUBTÍTULO
    # ==========================================

    @staticmethod
    def subtitle():

        return ctk.CTkFont(
            size=16
        )

    # ==========================================
    # TEXTO
    # ==========================================

    @staticmethod
    def body():

        return ctk.CTkFont(
            size=14
        )

    # ==========================================
    # LABEL
    # ==========================================

    @staticmethod
    def label():

        return ctk.CTkFont(
            size=13,
            weight="bold"
        )

    # ==========================================
    # BOTÃO
    # ==========================================

    @staticmethod
    def button():

        return ctk.CTkFont(
            size=14,
            weight="bold"
        )

    # ==========================================
    # PEQUENO
    # ==========================================

    @staticmethod
    def small():

        return ctk.CTkFont(
            size=12
        )