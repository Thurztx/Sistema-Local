from config.database import SessionLocal
from models.usuario import Usuario


class UsuarioRepository:

# Método 1 — Cadastrar 
    def cadastrar(self, usuario):

        with SessionLocal() as session:

            session.add(usuario)

            session.commit()

            session.refresh(usuario)

            return usuario

# Método 2 — Listar 
    def listar(self):

        with SessionLocal() as session:

            return session.query(Usuario).all()

# Método 3 — Buscar por ID
    def buscar_por_id(self, usuario_id):

        with SessionLocal() as session:

            return session.query(Usuario).filter(
                Usuario.id == usuario_id
            ).first()

# Método 4 — Atualizar 
    def atualizar(self, usuario):

        with SessionLocal() as session:

            session.merge(usuario)

            session.commit()

            return usuario

# Método 5 — Excluir 
    def excluir(self, usuario_id):

        with SessionLocal() as session:

            usuario = session.query(Usuario).filter(
                Usuario.id == usuario_id
            ).first()

            if usuario:

                session.delete(usuario)

                session.commit()

                return True

            return False