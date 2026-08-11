class ClienteService:

    def __init__(self, repository):

        self.repository = repository

    def create(self, dados):

        return self.repository.create(
            dados
        )

    def update(self, cliente_id, dados):

        return self.repository.update(
            cliente_id,
            dados
        )

    def get_all(self):

        return self.repository.get_all()

    def get_by_id(self, cliente_id):

        return self.repository.get_by_id(
            cliente_id
        )

    def delete(self, cliente_id):

        return self.repository.delete(
            cliente_id
        )