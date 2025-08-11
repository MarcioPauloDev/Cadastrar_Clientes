from aplicacao.bd import create_connection
from aplicacao.models import Cliente


# ✅ Insere um novo cliente na tabela 'clientes'.
def adicionar_cliente(cliente: Cliente):
    conn = create_connection()
    cursor = conn.cursor()

    # SQL de inserção com placeholders (%s) — mesmo para números
    sql = """
        INSERT INTO clientes (
            nome, email, telefone, endereco,
            estado_civil, documento, cpf_cnpj,
            cadastro_ativo, situacao_profissional
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Execução com os dados do objeto Cliente
    cursor.execute(sql, (
        cliente.nome,
        cliente.email,
        cliente.telefone,
        cliente.endereco,
        cliente.estado_civil,
        cliente.documento,
        cliente.cpf_cnpj,
        'ativo' if cliente.cadastro_ativo else 'inativo',
        cliente.situacao_profissional
    ))

    conn.commit()
    conn.close()


# ✅ Retorna todos os clientes cadastrados no banco de dados.
def listar_clientes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()
    conn.close()
    return resultados


# ✅ Seleciona um cliente específico pelo ID
def selecionar_cliente(cliente_id: int):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado


# ✅ Atualiza os dados de um cliente existente.
def atualizar_cliente(cliente_id: int, novo_cliente: Cliente):
    conn = create_connection()
    cursor = conn.cursor()

    sql = """
        UPDATE clientes 
        SET nome=%s, email=%s, telefone=%s, endereco=%s,
            estado_civil=%s, documento=%s, cpf_cnpj=%s,
            cadastro_ativo=%s, situacao_profissional=%s
        WHERE id=%s
    """

    cursor.execute(sql, (
        novo_cliente.nome,
        novo_cliente.email,
        novo_cliente.telefone,
        novo_cliente.endereco,
        novo_cliente.estado_civil,
        novo_cliente.documento,
        novo_cliente.cpf_cnpj,
        'ativo' if novo_cliente.cadastro_ativo else 'inativo',
        novo_cliente.situacao_profissional,
        cliente_id
    ))

    conn.commit()
    conn.close()


# ✅ Remove um cliente do banco de dados pelo ID.
def deletar_cliente(cliente_id: int):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
    conn.commit()
    conn.close()