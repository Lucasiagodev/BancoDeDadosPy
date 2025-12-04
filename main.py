# import mysql.connector
from cadastro_pessoas import cadastro_usuarios
from listar_usuariosb import listar_usuarios
from atualizar_usuario import atualiza_usuario
import os

def main():
    


    while True:
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