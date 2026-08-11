class ClienteController:

    def __init__(self, service):

        self.service = service

    def create_client(self, dados):

        return self.service.create(dados)

    def update_client(self, cliente_id, dados):

        return self.service.update(
            cliente_id,
            dados
        )

    def get_clients(self):

        return self.service.get_all()

    def get_client(self, cliente_id):

        return self.service.get_by_id(
            cliente_id
        )

    def delete_client(self, cliente_id):

        return self.service.delete(
            cliente_id
        )