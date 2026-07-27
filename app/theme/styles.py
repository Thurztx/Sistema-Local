from .colors import Colors
from .fonts import Fonts


class Styles:

    PRIMARY_BUTTON = {
        "fg_color": Colors.PRIMARY,
        "hover_color": Colors.PRIMARY_HOVER,
        "text_color": "white",
        "font": Fonts.BUTTON,
        "corner_radius": 8,
        "height": 42
    }

    SECONDARY_BUTTON = {
        "fg_color": Colors.BUTTON_SECONDARY,
        "hover_color": Colors.BUTTON_SECONDARY_HOVER,
        "text_color": Colors.TEXT,
        "border_width": 1,
        "border_color": Colors.BORDER,
        "font": Fonts.BUTTON,
        "corner_radius": 8,
        "height": 42
    }

    CARD = {
        "fg_color": Colors.SURFACE,
        "corner_radius": 12
    }

    INPUT = {
        "fg_color": Colors.INPUT_BG,
        "border_color": Colors.INPUT_BORDER,
        "text_color": Colors.TEXT,
        "corner_radius": 8,
        "height": 40
    }