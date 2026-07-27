from config.database import SessionLocal
from models.entrada import Entrada

# Método 1 — Cadastrar 
# Método 2 — Listar 
# Método 3 — Buscar por ID
# Método 4 — Atualizar 
# Método 5 — Excluir 

class EntradaRepository:

# Método 1 — Cadastrar 
    def cadastrar(self, entrada):

        with SessionLocal() as session:

            session.add(entrada)

            session.commit()

            session.refresh(entrada)

            return entrada

# Método 2 — Listar 
    def listar(self):

        with SessionLocal() as session:

            return session.query(Entrada).all()

# Método 3 — Buscar por ID
    def buscar_por_id(self, entrada_id):

        with SessionLocal() as session:

            return session.query(Entrada).filter(
                Entrada.id == entrada_id
            ).first()

# Método 4 — Atualizar 
    def atualizar(self, entrada):

        with SessionLocal() as session:

            session.merge(entrada)

            session.commit()

            return entrada

# Método 5 — Excluir 
    def excluir(self, entrada_id):

        with SessionLocal() as session:

            entrada = session.query(Entrada).filter(
                Entrada.id == entrada_id
            ).first()

            if entrada:

                session.delete(entrada)

                session.commit()

                return True

            return False