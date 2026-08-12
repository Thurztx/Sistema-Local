from app.database.connection import get_connection


class CompraRepository:

    def __init__(self):
        pass

    # ==========================================
    # CRIAR COMPRA
    # ==========================================

    def create(self, compra, itens):

        connection = get_connection()

        try:

            cursor = connection.cursor()

            # ----------------------------------
            # Inserir compra
            # ----------------------------------

            cursor.execute(
                """
                INSERT INTO compras (
                    fornecedor_id,
                    data_compra,
                    valor_total,
                    forma_pagamento,
                    observacoes
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    compra["fornecedor_id"],
                    compra["data_compra"],
                    compra["valor_total"],
                    compra["forma_pagamento"],
                    compra.get("observacoes")
                )
            )

            compra_id = cursor.lastrowid

            # ----------------------------------
            # Inserir itens
            # ----------------------------------

            for item in itens:

                subtotal = (
                    item["quantidade"]
                    * item["valor_unitario"]
                )

                cursor.execute(
                    """
                    INSERT INTO compra_itens (
                        compra_id,
                        produto_id,
                        quantidade,
                        valor_unitario,
                        subtotal
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        compra_id,
                        item["produto_id"],
                        item["quantidade"],
                        item["valor_unitario"],
                        subtotal
                    )
                )

            connection.commit()

            return compra_id

        except Exception:

            connection.rollback()

            raise

        finally:

            connection.close()

    # ==========================================
    # BUSCAR POR ID
    # ==========================================

    def get_by_id(self, compra_id):

        connection = get_connection()

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    c.id,
                    c.fornecedor_id,
                    c.data_compra,
                    c.valor_total,
                    c.forma_pagamento,
                    c.observacoes
                FROM compras c
                WHERE c.id = ?
                """,
                (compra_id,)
            )

            compra = cursor.fetchone()

            if compra is None:
                return None

            cursor.execute(
                """
                SELECT
                    ci.id,
                    ci.compra_id,
                    ci.produto_id,
                    ci.quantidade,
                    ci.valor_unitario,
                    ci.subtotal
                FROM compra_itens ci
                WHERE ci.compra_id = ?
                ORDER BY ci.id
                """,
                (compra_id,)
            )

            itens = cursor.fetchall()

            return {
                "id": compra["id"],
                "fornecedor_id": compra["fornecedor_id"],
                "data_compra": compra["data_compra"],
                "valor_total": compra["valor_total"],
                "forma_pagamento": compra["forma_pagamento"],
                "observacoes": compra["observacoes"],
                "itens": [
                    dict(item)
                    for item in itens
                ]
            }

        finally:

            connection.close()

    # ==========================================
    # BUSCAR TODAS
    # ==========================================

    def get_all(self):

        connection = get_connection()

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    c.id,
                    c.fornecedor_id,
                    f.nome AS fornecedor_nome,
                    c.data_compra,
                    c.valor_total,
                    c.forma_pagamento,
                    c.observacoes
                FROM compras c
                LEFT JOIN fornecedores f
                    ON f.id = c.fornecedor_id
                ORDER BY c.data_compra DESC, c.id DESC
                """
            )

            compras = cursor.fetchall()

            return [
                dict(compra)
                for compra in compras
            ]

        finally:

            connection.close()

    # ==========================================
    # BUSCAR ITENS
    # ==========================================

    def get_items(self, compra_id):

        connection = get_connection()

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    ci.id,
                    ci.compra_id,
                    ci.produto_id,
                    p.nome AS produto_nome,
                    ci.quantidade,
                    ci.valor_unitario,
                    ci.subtotal
                FROM compra_itens ci
                INNER JOIN produtos p
                    ON p.id = ci.produto_id
                WHERE ci.compra_id = ?
                ORDER BY ci.id
                """,
                (compra_id,)
            )

            itens = cursor.fetchall()

            return [
                dict(item)
                for item in itens
            ]

        finally:

            connection.close()

    # ==========================================
    # ATUALIZAR COMPRA
    # ==========================================

    def update(self, compra_id, compra, itens):

        connection = get_connection()

        try:

            cursor = connection.cursor()

            # ----------------------------------
            # Atualizar compra
            # ----------------------------------

            cursor.execute(
                """
                UPDATE compras
                SET
                    fornecedor_id = ?,
                    data_compra = ?,
                    valor_total = ?,
                    forma_pagamento = ?,
                    observacoes = ?
                WHERE id = ?
                """,
                (
                    compra["fornecedor_id"],
                    compra["data_compra"],
                    compra["valor_total"],
                    compra["forma_pagamento"],
                    compra.get("observacoes"),
                    compra_id
                )
            )

            # ----------------------------------
            # Remover itens antigos
            # ----------------------------------

            cursor.execute(
                """
                DELETE FROM compra_itens
                WHERE compra_id = ?
                """,
                (compra_id,)
            )

            # ----------------------------------
            # Inserir itens novamente
            # ----------------------------------

            for item in itens:

                subtotal = (
                    item["quantidade"]
                    * item["valor_unitario"]
                )

                cursor.execute(
                    """
                    INSERT INTO compra_itens (
                        compra_id,
                        produto_id,
                        quantidade,
                        valor_unitario,
                        subtotal
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        compra_id,
                        item["produto_id"],
                        item["quantidade"],
                        item["valor_unitario"],
                        subtotal
                    )
                )

            connection.commit()

        except Exception:

            connection.rollback()

            raise

        finally:

            connection.close()

    # ==========================================
    # EXCLUIR COMPRA
    # ==========================================

    def delete(self, compra_id):

        connection = get_connection()

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM compra_itens
                WHERE compra_id = ?
                """,
                (compra_id,)
            )

            cursor.execute(
                """
                DELETE FROM compras
                WHERE id = ?
                """,
                (compra_id,)
            )

            connection.commit()

        except Exception:

            connection.rollback()

            raise

        finally:

            connection.close()

    # ==========================================
    # PESQUISAR
    # ==========================================

    def search(self, search_text):

        connection = get_connection()

        try:

            cursor = connection.cursor()

            search = f"%{search_text}%"

            cursor.execute(
                """
                SELECT
                    c.id,
                    c.fornecedor_id,
                    f.nome AS fornecedor_nome,
                    c.data_compra,
                    c.valor_total,
                    c.forma_pagamento,
                    c.observacoes
                FROM compras c
                LEFT JOIN fornecedores f
                    ON f.id = c.fornecedor_id
                WHERE
                    f.nome LIKE ?
                    OR CAST(c.id AS TEXT) LIKE ?
                    OR c.forma_pagamento LIKE ?
                ORDER BY
                    c.data_compra DESC,
                    c.id DESC
                """,
                (
                    search,
                    search,
                    search
                )
            )

            compras = cursor.fetchall()

            return [
                dict(compra)
                for compra in compras
            ]

        finally:

            connection.close()

    # ==========================================
    # FILTRAR POR PERÍODO
    # ==========================================

    def get_by_period(
        self,
        start_date,
        end_date
    ):

        connection = get_connection()

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    c.id,
                    c.fornecedor_id,
                    f.nome AS fornecedor_nome,
                    c.data_compra,
                    c.valor_total,
                    c.forma_pagamento,
                    c.observacoes
                FROM compras c
                LEFT JOIN fornecedores f
                    ON f.id = c.fornecedor_id
                WHERE
                    DATE(c.data_compra)
                    BETWEEN DATE(?)
                    AND DATE(?)
                ORDER BY
                    c.data_compra DESC,
                    c.id DESC
                """,
                (
                    start_date,
                    end_date
                )
            )

            compras = cursor.fetchall()

            return [
                dict(compra)
                for compra in compras
            ]

        finally:

            connection.close()