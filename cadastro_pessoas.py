# cadastro_pessoas.py
from pessoasDB import conexao_banco_dados
import os

def cadastro_usuarios():  # Linha 1
    banco = conexao_banco_dados()
    cursor = banco.cursor()

    os.system('cls')
    print('---------CADASTRO DE USUÁRIO-----------\n')

    nome = input('Nome de usuário: ')
    
    try:
        idade = int(input('Idade: '))
    except ValueError:
        os.system('cls')
        print('SOMENTE NÚMEROS!'.upper())
        input('Aperte qualquer tecla para continuar...')
        cursor.close()
        banco.close()
        os.system('cls')
        return  # Linha 20: alterado de "return None" → "return"

    email = input('Email: ')
    senha = input('Senha: ')

    comando = f"""INSERT INTO usuarios (nome, idade, email, senha)
                  VALUES ('{nome}', {idade}, '{email}', '{senha}')"""

    cursor.execute(comando)
    banco.commit()
    cursor.close()
    banco.close()

    sair = input('Digite [enter] para voltar: ')
    os.system('cls')
    return  # Linha 36: alterado de "return None" → "return"
