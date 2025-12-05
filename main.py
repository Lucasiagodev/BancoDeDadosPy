# main.py
from cadastro_pessoas import cadastro_usuarios
from listar_usuariosb import listar_usuarios
from atualizar_usuario import atualiza_usuario
from delete import delete_usuario
from login import login
import os

def main():  # Linha 1
    resultado = login()

    while True:
        os.system('cls')
        print(f'ADMINISTRADOR: {resultado[1]}\n')
        print('--------CADASTRO DE USUÁRIOS-----------\n')
        print('(1) Cadastrar usuário')
        print('(2) Listar usuários')
        print('(3) Atualizar dados do usuário')
        print('(4) Deletar usuário')
        print('Digite [0] para sair\n')
        

        entrada = input('Escolha uma opção: ')

        if entrada == '0':
            break
        os.system('cls')

        if entrada == '0':
            break
        elif entrada == '1':
            cadastro_usuarios()
        elif entrada == '2':
            listar_usuarios()
        elif entrada == '3':
            atualiza_usuario()
        elif entrada == '4':
            delete_usuario()
        else:
            print('Invalido! somente de 1 a 4.')

if __name__ == "__main__":
    main()
