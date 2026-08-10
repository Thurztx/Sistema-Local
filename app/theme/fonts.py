import customtkinter as ctk

class Fonts:

    FAMILY = "Segoe UI"

    DISPLAY = (FAMILY, 28, "bold")

    H1 = ctk.CTkFont(
        family="Segoe UI",
        size=26,
        weight="bold"
    )

    H2 = ctk.CTkFont(
        family="Segoe UI",
        size=18,
        weight="bold"
    )

    H3 = (FAMILY, 18, "bold")

    SUBTITLE = (FAMILY, 16, "bold")

    BODY = ctk.CTkFont(
        family="Segoe UI",
        size=14
    )

    SMALL = ctk.CTkFont(
        family="Segoe UI",
        size=12
    )

    BUTTON = (FAMILY, 14, "bold")

    INPUT = (FAMILY, 14)

    PLACEHOLDER = (FAMILY, 13, "italic")

    TABLE_HEADER = (FAMILY, 14, "bold")

    TABLE_BODY = (FAMILY, 13)