from config.database import SessionLocal
from models.cliente import Cliente


class ClienteRepository:

# Método 1 — Cadastrar 
    def cadastrar(self, cliente):

        with SessionLocal() as session:

            session.add(cliente)

            session.commit()

            session.refresh(cliente)

            return cliente

# Método 2 — Listar 
    def listar(self):

        with SessionLocal() as session:

            return session.query(Cliente).all()

# Método 3 — Buscar por ID
    def buscar_por_id(self, cliente_id):

        with SessionLocal() as session:

            return session.query(Cliente).filter(
                Cliente.id == cliente_id
            ).first()

# Método 4 — Atualizar 
    def atualizar(self, cliente):

        with SessionLocal() as session:

            session.merge(cliente)

            session.commit()

            return cliente

# Método 5 — Excluir 
    def excluir(self, cliente_id):

        with SessionLocal() as session:

            cliente = session.query(Cliente).filter(
                Cliente.id == cliente_id
            ).first()

            if cliente:

                session.delete(cliente)

                session.commit()

                return True

            return False