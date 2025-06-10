usuarios = {'kevensoares@gmail.com': ['joelderson keven soares da silva','keven123'],
            'jubiscleudo@gmail.com': ['jubiscleudo jeberson santos', 'juju123']}

import utilidade

def cadastrar_usuario():
    print('----------- CADASTRO ------------')
    nome_completo = input('Digite seu nome completo: ')
    email = input('Digite seu melhor email: ')
    while '@' not in email or '.com' not in email:
        email = input('Digite um email válido (ex: usuario@exemplo.com): ')
    senha = input('Digite sua senha: ')
    usuarios[email] = [nome_completo, senha]
    with open("usuarios.txt", "a") as arquivo: ##### copiei do chat gpt ######
        arquivo.write(f"{email}:{senha}\n")
    print('Usuário cadastrado com sucesso!')
    utilidade.mostrar_linha()

def fazer_login():
    print('-------- FAÇA SEU LOGIN ----------')
    email_login = input('digite seu email: ')
    senha_login = input('digite sua senha: ')
    if email_login in usuarios and usuarios[email_login][1] == senha_login:
        print(f'\nBem-vindo, {usuarios[email_login][0]}! Login realizado com sucesso!')
        return email_login
    else:
        print('Email ou senha inválidos!')
        return None



