# delete.py
from pessoasDB import conexao_banco_dados
from reloadd import reload
from login import login
import os

def delete_usuario():  # Linha 1
    banco = conexao_banco_dados()
    cursor = banco.cursor()

    login()
    reload()
    

    comando1 = f"SELECT * FROM usuarios;"
    cursor.execute(comando1)
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print('Banco de dados vazio')
        cursor.close()
        banco.close()
        os.system('cls')
        return
    else:
        print(f'Entrada de segurança:')
        id_usuario = input('Informe o id do usuário: ')
        os.system('cls')

        comando = f"SELECT id, nome, idade, email, senha FROM usuarios WHERE id = {id_usuario}"

        try:
            cursor.execute(comando)
            resultado = cursor.fetchone()
        except Exception:
            print('Erro ao encontrar usuário!')
            cursor.close()
            banco.close()
            os.system('cls')
            return
                
        if resultado is None:
            print('Usuário não encontrado!')
            cursor.close()
            banco.close()
            os.system('cls')
            return

        print(f'Conta do Usuário: ID: {resultado[0]} | NOME: {resultado[1]} IDADE: {resultado[2]} EMAIL: {resultado[3]} SENHA: {resultado[4]}')
        confirma = input('Tem certeza que quer apagar esse usuário? [s/n]'.title())

        if confirma.lower() != 's':
            cursor.close()
            banco.close()
            os.system('cls')
            return
        else:
            delete = f"DELETE FROM usuarios WHERE id = {id_usuario}"
            cursor.execute(delete)
            banco.commit()
            print("\nUsuário apagado com sucesso!\n")
            input('Aperte qualquer tecla para voltar. ')
            os.system('cls')

        cursor.close()
        banco.close()
    return

if __name__ == '__main__':
    delete_usuario()