# atualizar_usuario.py
from pessoasDB import conexao_banco_dados
import os

def atualiza_usuario():  # Linha 1
    while True:
        os.system('cls')
        print('--------ATUALIZAR USUÁRIOS-----------\n')
        print('Selecione uma opção ou digite [s] para voltar \n')
        print('(1) Atualizar nome de usuário')
        print('(2) Atualizar idade de usuário')
        print('(3) Atualizar email de usuário')
        print('(4) Atualizar senha de usuário')

        entrada = input('Escolha uma opção: ')
        os.system('cls')

        if entrada.lower() == 's':
            break

        banco = conexao_banco_dados()
        cursor = banco.cursor()
        id_usuario = input('Informe o id do usuário: ')
        os.system('cls')

        if entrada == '1':
            comando = f"SELECT id, nome FROM usuarios WHERE id = {id_usuario}"
            campo = 'nome'
            novo_valor = input('Digite o novo nome: ')
        elif entrada == '2':
            comando = f"SELECT id, idade FROM usuarios WHERE id = {id_usuario}"
            campo = 'idade'
            novo_valor = input('Digite a nova idade: ')
        elif entrada == '3':
            comando = f"SELECT id, email FROM usuarios WHERE id = {id_usuario}"
            campo = 'email'
            novo_valor = input('Digite o novo email: ')
        elif entrada == '4':
            comando = f"SELECT id, senha FROM usuarios WHERE id = {id_usuario}"
            campo = 'senha'
            novo_valor = input('Digite a nova senha: ')
        else:
            print('Opção inválida!')
            os.system('cls')
            continue

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

        update = f"UPDATE usuarios SET {campo} = '{novo_valor}' WHERE id = {id_usuario}"
        cursor.execute(update)
        banco.commit()

        print(f"\n{campo.capitalize()} atualizado com sucesso!\n")
        os.system('cls')
        cursor.close()
        banco.close()
    return
