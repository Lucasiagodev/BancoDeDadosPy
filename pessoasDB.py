import mysql.connector
from mysql.connector import errorcode

def conexao_banco_dados():
    try:
        conectar = mysql.connector.connect(
            user='root',
            password='lucas',
            host='localhost',
            database='pessoas'
        )

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha incorretos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        elif err.errno == errorcode.ER_NO_SUCH_TABLE:
            print("Tabela não existe")
        else:
            print(err)
        return None
    else:
        print('conectado com sucesso')
        return conectar











            










