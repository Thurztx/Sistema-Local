import customtkinter as ctk
from datetime import datetime

from theme.theme_manager import ThemeManager
from theme.fonts import Fonts

# Componentes reutilizáveis (adicione conforme for criando)
from components.search_bar import SearchBar
from components.filter_bar import FilterBar
from components.data_table import DataTable
from components.toolbar import Toolbar
from components.pagination import Pagination

class ProdutosView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.create_header()

        self.create_search()

        self.create_filters()

        self.create_table()

        self.create_pagination()