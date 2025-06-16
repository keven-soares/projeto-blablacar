from yfinance.utils import fix_Yahoo_returning_live_separate

import utilidade
from main import carregar_usuarios

usuarios = carregar_usuarios()

def cadastrar_usuario():
    print('----------- CADASTRO ------------')
    nome_completo = input('Digite seu nome completo: ')
    while len(nome_completo) < 13:
        print('nome muito curto, digite seu nome completo')
        nome_completo = input('digite seu nome completo: ')

    while True:
        email_login = input('Digite seu e-mail: ')
        if '@' in email_login and '.com' in email_login:
            if email_login not in usuarios:
                break
            else:
                print('E-mail já cadastrado!')
        else:
            print('E-mail inválido (use formato: usuario@exemplo.com)')

    senha = input('Digite sua senha: ')
    while len(senha) < 8:
        print('Senha muito curta (mínimo 8 caracteres)')
        senha = input('Digite sua senha: ')

    with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"'{nome_completo}': ['{email_login}', '{senha}'],\n")

    print('Usuário cadastrado com sucesso!')

    atualizar = carregar_usuarios()

    for nome, dados in atualizar.items():
        if email_login == dados[0] and dados[1] == senha:
            print(f'{dados[0]}: {nome} (senha: {'*' * len(dados[1])})')
            break
    utilidade.mostrar_linha()

'''def verificar_usuarios():
    print('\n Usuários no sistema:')
    if not usuarios:
        print('Nenhum usuário foi carregado!')
        return False
    return True

if not verificar_usuarios():
    print('Falha ao carregar usuários. Verifique o arquivo usuarios.txt')'''

def fazer_login():
    print('-------- FAÇA SEU LOGIN ----------')
    email_login = input('digite seu email: ')
    senha_login = input('digite sua senha: ')

    usuarios = carregar_usuarios()

    for nome, dados in usuarios.items():
        email, senha = dados

        if email_login == email and senha_login == senha:
            print('login bem sucedido')
            return True
    else:
        print("erro ao fazer login")
        return False


utilidade.mostrar_linha()




