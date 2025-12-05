# import mysql.connector
from cadastro_pessoas import cadastro_usuarios
from listar_usuariosb import listar_usuarios
from atualizar_usuario import atualiza_usuario
from pessoasDB import conexao_banco_dados
from reload import reload
import os

def main():
    
    banco = conexao_banco_dados()
    cursor = banco.cursor()
    
    print('-------------Aréa de login-----------'.upper())
    email = input('Email:')
    senha = input('Senha:')


    comando = f"""select nome, email, senha from usuarios where email = '{email}' and senha = '{senha}';"""
    cursor.execute(comando)
    resultado = cursor.fetchone()

    

    if resultado:
        print('Login efetuado com sucesso!\n')
        print(f'Bem vindo ADM {resultado[0]}\n')
        os.system('cls')
        print('Carregando!', flush=True)
        reload()  # animação roda agora
        os.system('cls')

    else: 
        print('Usuário ou senha icorretos')
        exit()

    cursor.close()
    banco.close()


    while True:
        print(f'ADMINISTRADOR: {resultado[0]}\n')
        print('--------CADASTRO DE USUARIOS-----------\n')
        print('Selecione uma opção \n')
        print('(1) cadastrar usuário'.title())
        print('(2) listar usuário'.title())
        print('(3) atualizar dados do  usuário'.title())
        print('(4) deletar usuário'.title())
        print('Precione  a tecla [Esc]\n')

        entrada = input('Escolha uma opção: ')

        if entrada == '0':
            break
        
        if entrada == '1':
            os.system('cls')
            cadastro_usuarios()
        elif entrada == '2':
            os.system('cls')
            listar_usuarios()
        elif entrada == '3':
            os.system('cls')
            atualiza_usuario()

        
    



main()