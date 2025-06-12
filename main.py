import usuario
import caronas
import os
usuarios = {}

def carregar_usuarios():
    if os.path.exists('usuarios.txt'):
        # Lê o arquivo linha por linha
        with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Remove vírgula e quebra de linha
                linha = linha.strip().rstrip(',')

                # Divide a linha na chave e no valor
                if ':' in linha:
                    chave, valor = linha.split(':', 1)
                    nome = chave.strip().strip("'")  # Remove espaços e aspas simples
                    dados = eval(valor.strip())  # Converte a string ['email', 'senha'] em lista

                    usuarios[nome] = dados

        # Agora você pode usar um for normalmente:
        for nome, dados in usuarios.items():
            email, senha = dados
    return usuarios


def menu_principal():
    while True:
        print('\n========= MENU ========')
        print('1- Cadastre-se')
        print('2- Login')
        print('0- Sair do programa')

        op = input('Digite a opção desejada: ')

        if op == '1':
            usuario.cadastrar_usuario()
        elif op == '2':
            email_login = usuario.fazer_login()
            if email_login:
                menu_usuario_logado(email_login)
        elif op == '0':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida!')

def menu_usuario_logado(email_login):
    while True:
        print('\n============ MENU =============')
        print('1- Cadastro de carona')
        print('2- Listar todas as caronas')
        print('3- Buscar carona por origem e destino')
        print('4- Reservar vaga em carona')
        print('5- Cancelar reserva')
        print('6- Remover carona')
        print('7- Mostrar detalhes da carona')
        print('8- Caronas que você está cadastrado')
        print('9- Função extra')
        print('10- relatório do total')
        print('11- Logout')

        op = input('\nDigite a opção desejada: ')

        if op == '1':
            caronas.cadastrar_carona(email_login)
        elif op == '2':
            caronas.listar_caronas()
        elif op == '3':
            caronas.buscar_carona_por_rota()
        elif op == '4':
            caronas.reservar_vaga(email_login)
        elif op == '5':
            caronas.cancelar_reserva(email_login)
        elif op == '6':
            caronas.remover_carona(email_login)
        elif op == '7':
            caronas.mostrar_detalhes_carona()
        elif op == '8':
            caronas.mostrar_caronas_cadastradas(email_login)
        elif op == '9':
            print('em manutenção')
        elif op == '10':
            print('em desenvolvimento')
        elif op == '11':
            print('\n-----------logout-------------')
            msg_confirmacao = input('Tem certeza que gostaria de sair? (s/n): ').lower()
            if msg_confirmacao == 's':
                print('Logout realizado com sucesso, volte sempre!')
                break
            else:
                print('Logout cancelado')
        else:
            print('opção inválida!')

if __name__ == '__main__':
    usuarios = carregar_usuarios()
    menu_principal()


                    
                        















