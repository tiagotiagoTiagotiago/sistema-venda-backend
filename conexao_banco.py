import mysql.connector

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            database="testpos"
        )
        return conexao
    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)
        return None
