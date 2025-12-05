# login.py
from pessoasDB import conexao_banco_dados
from reloadd import reload
import os

def login():  # Linha 1
    banco = conexao_banco_dados()
    cursor = banco.cursor()
    
    print('-------------ARÉA DE LOGIN-----------'.upper())
    email = input('Email:')
    senha = input('Senha:')

    comando = f"""SELECT id, nome, idade, email, senha 
                  FROM usuarios 
                  WHERE email = '{email}' AND senha = '{senha}';"""
    cursor.execute(comando)
    resultado = cursor.fetchone()

    

    if resultado:
        print('Login efetuado com sucesso!\n')
        print(f'Bem vindo ADM {resultado[1]}\n')
        os.system('cls')
        print('Carregando!', flush=True)
        reload()
        os.system('cls')
        return resultado

    else: 
        print('Usuário ou senha incorretos')
        exit()  # Linha 28: encerra programa
