class ClienteRepository:

    def __init__(self, connection):

        self.connection = connection

    def create(self, dados):

        # INSERT
        ...

    def update(self, cliente_id, dados):

        # UPDATE
        ...

    def get_all(self):

        # SELECT
        ...

    def get_by_id(self, cliente_id):

        # SELECT
        ...

    def delete(self, cliente_id):

        # DELETE
        ...