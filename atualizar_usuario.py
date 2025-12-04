from pessoasDB import conexao_banco_dados
from listar_usuariosb import listar_usuarios
import os

def atualiza_usuario():



    print('--------ATUALIZAR  USUARIOS-----------\n')
    print('Selecione uma opção \n')
    print('(1) Atualizar nome de usuário:'.title())
    print('(2) Atualizar idade de usuário:'.title())
    print('(3) Atualizar email de usuário:'.title())
    print('(4) atualizar senha de usuário:'.title())
    
    entrada = input('Escolha uma opção: ')

    if entrada == '1':
       ...