from app.views.clientes.cliente_form import ClienteForm

from app.theme.theme_manager import ThemeManager
from app.theme.fonts import Fonts

def open_client_form(self):

    ClienteForm(
        self,
        controller=self.controller
    )

    command=self.open_client_form

def edit_client(self, cliente):

    ClienteForm(
        self,
        controller=self.controller,
        cliente=cliente
    )

def refresh_clients(self):

    clientes = self.controller.get_clients()

    self.update_table(clientes)