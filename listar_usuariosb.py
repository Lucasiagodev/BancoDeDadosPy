from pessoasDB import conexao_banco_dados
import os

def listar_usuarios():
    banco = conexao_banco_dados()
    cursor = banco.cursor()

    print('---------lista de usuário-----------\n'.title())
    

    comando = f"""SELECT * FROM usuarios;"""
    cursor.execute(comando)

    resultado = cursor.fetchall()
    if  len(resultado) == 0:
         
        print('Banco de dados vazio')
        
        cursor.close()
        banco.close()
    else:

        for linha in resultado:
                print('-' * 55 * 2)
                print(f'ID: {linha[0]} | NOME: {linha[1]} IDADE: {linha[2]} EMAIL: {linha[3]} SENHA: {linha[4]}')
              

    sair = input('Tecle [enter] para voltar: ')
    banco.close()
    cursor.close()


    os.system('cls')
    if sair == '0':
        return None


