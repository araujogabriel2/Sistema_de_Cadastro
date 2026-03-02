from db import * 


def interface_cadastrar_usuario():
    print('--- CADASTRAR USUÁRIO ---')

    nome = input('Digite seu nome:')
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            break
        except ValueError:
            print('Digite apenas números no campo idade!')
    
    inserir_dados(nome, idade)

def interface_listar_usuarios():
    print('LISTANDO TODOS OS USUÁRIOS...')
    listar_dados()

def interface_listar_usuario_ID():
    print("Listar usuário com FILTRO (ID)")
    usuario_id=input('Digite o ID do usuário:')
    listar_dados_ID(usuario_id)

menus = {
    "1": interface_cadastrar_usuario,
    "2": interface_listar_usuarios,
    "3": interface_listar_usuario_ID
}


def inicializar_sistema():
    criar_tabela_usuarios()
    while True:
        print("0. Sair")
        print("1. Cadastar usuário")
        print("2. Listar todos os usuários")
        print("3. Listar usuário pelo ID")

        escolha=input('Escolha um número da opção desejada:')
        if escolha == "0":
            print('Saindo..')
            break
        if escolha in menus:
            funcao_escolhida = menus[escolha]
            funcao_escolhida()
        else:
            print('Escolha uma opção válida!')