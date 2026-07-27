from config.database import SessionLocal
from models.saida import Saida


class SaidaRepository:

# Método 1 — Cadastrar
    def cadastrar(self, saida):

        with SessionLocal() as session:

            session.add(saida)

            session.commit()

            session.refresh(saida)

            return saida
 
# Método 2 — Listar 
    def listar(self):

        with SessionLocal() as session:

            return session.query(Saida).all()

# Método 3 — Buscar por ID
    def buscar_por_id(self, saida_id):

        with SessionLocal() as session:

            return session.query(Saida).filter(
                Saida.id == saida_id
            ).first()

# Método 4 — Atualizar 
    def atualizar(self, saida):

        with SessionLocal() as session:

            session.merge(saida)

            session.commit()

            return saida

# Método 5 — Excluir 
    def excluir(self, saida_id):

        with SessionLocal() as session:

            saida = session.query(Saida).filter(
                Saida.id == saida_id
            ).first()

            if saida:

                session.delete(saida)

                session.commit()

                return True

            return False