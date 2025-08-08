import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Noah@010123',
            database='cadastro_clientes_bd'
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        print("Conexão bem-sucedida!")
        conn.close()