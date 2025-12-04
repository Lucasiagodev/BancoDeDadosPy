from pessoasDB import conexao_banco_dados
import os

def cadastro_usuarios():
    banco = conexao_banco_dados()

    cursor = banco.cursor()

    print('---------cadastro de usuário-----------'.title())
    print()

    nome = input('Nome de usuário: ')
    
    try:
        idade = int(input('Idade: ')) # conserta o erro 
    except ValueError:
        os.system('cls')
        print('somente números!'.upper())
        input('aperte qualquer tecla para continuar...')
        cursor.close()
        banco.close()
        os.system('cls')

        return None
    else:
        email = input('Email: ')
        senha = input('Senha: ')


        comando = f"""INSERT INTO usuarios (nome, idade, email, senha) VALUES ('{nome}', {idade}, '{email}', '{senha}')"""

        sair = input('Digite [enter] para voltar: ')
        os.system('cls')

        cursor.execute(comando)
        banco.commit()


        cursor.close()
        banco.close()

        if sair == '0':
            return None