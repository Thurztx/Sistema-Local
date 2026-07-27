from config.database import SessionLocal
from models.movimentacao import Movimentacao


# Método 1 — Cadastrar 
# Método 2 — Listar 
# Método 3 — Buscar por ID
# Método 4 — Atualizar 
# Método 5 — Excluir 


class MovimentacaoRepository:

# Método 1 — Cadastrar 
    def cadastrar(self, movimentacao):

        with SessionLocal() as session:

            session.add(movimentacao)

            session.commit()

            session.refresh(movimentacao)

            return movimentacao

# Método 2 — Listar 
    def listar(self):

        with SessionLocal() as session:

            return session.query(Movimentacao).all()

# Método 3 — Buscar por ID
    def buscar_por_id(self, movimentacao_id):

        with SessionLocal() as session:

            return session.query(Movimentacao).filter(
                Movimentacao.id == movimentacao_id
            ).first()

# Método 4 — Atualizar 
    def atualizar(self, movimentacao):

        with SessionLocal() as session:

            session.merge(movimentacao)

            session.commit()

            return movimentacao

# Método 5 — Excluir 
    def excluir(self, movimentacao_id):

        with SessionLocal() as session:

            movimentacao = session.query(Movimentacao).filter(
                Movimentacao.id == movimentacao_id
            ).first()

            if movimentacao:

                session.delete(movimentacao)

                session.commit()

                return True

            return False