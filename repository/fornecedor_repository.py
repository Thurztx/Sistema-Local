# Importação da Model
from config.database import SessionLocal
from models.fornecedor import Fornecedor


class FornecedorRepository:

# Método 1 — Cadastrar Fornecedor
    def cadastrar(self, fornecedor):

        with SessionLocal() as session:

            session.add(fornecedor)

            session.commit()

            session.refresh(fornecedor)

            return fornecedor

# Método 2 — Listar Fornecedores
    def listar(self):

        with SessionLocal() as session:

            return session.query(Fornecedor).all()

# Método 3 — Buscar por ID
    def buscar_por_id(self, fornecedor_id):

        with SessionLocal() as session:

            return session.query(Fornecedor).filter(
                Fornecedor.id == fornecedor_id
            ).first()
        
# Método 4 — Atualizar Fornecedor
    def atualizar(self, fornecedor):

        with SessionLocal() as session:

            session.merge(fornecedor)

            session.commit()

            return fornecedor

# Método 5 — Excluir Fornecedor
    def excluir(self, fornecedor_id):

        with SessionLocal() as session:

            fornecedor = session.query(Fornecedor).filter(
                Fornecedor.id == fornecedor_id
            ).first()

            if fornecedor:

                session.delete(fornecedor)

                session.commit()

                return True

            return False