usuarios = {'kevensoares@gmail.com': ['joelderson keven soares da silva','keven123',],
            'jubiscleudo@gmail.com': ['jubiscleudo jeberson santos', 'juju123']}
caronas = {'kevensoares@gmail.com': ['conceição', 'cajazeiras', '17/05/2025', '22 horas', 4, '25', ['xuxubeleza@.com', '17/05/2025']],
           'jubiscleudo@gmail.com': ['cajazeiras', 'pombal', '22/05/2025', '13 horas', 10, '20', []]}

import utilidade

def cadastrar_carona(email_motorista):
    print('\n-----voce é o motorista da viagem, atualize as opções abaixo------')
    origem = input('qual o local de origem da sua carona: ').title()
    destino = input('qual o local de destino da sua carona: ').title()
    data = utilidade.verificar_data
    hora = input('qual o horário de partida: ')
    qtde_vagas = int(input('vagas disponíveis: '))
    valor_vagas = float(input('qual o valor da viajem(por vaga): '))
    caronas[email_motorista] = [origem, destino, data, hora, qtde_vagas, valor_vagas, []]
    print('\n viagem confirmada')

    utilidade.mostrar_linha()


def listar_caronas():
    print('\n--------- CARONAS DISPONÍVEIS --------')
    encontrou = False
    for email in caronas:
        origem, destino, data, hora, vagas, valor, passageiros = caronas[email]
        if vagas > 0:
            encontrou = True
            print(f'\nMotorista: {usuarios[email][0]}')
            print(f'saindo De {origem} para {destino}')
            print(f'Dia: {data} - {hora}')
            print(f'Vagas: {vagas} - Preço: R${valor}')

    if not encontrou:
        print('nenhuma carona disponível no momento')
    utilidade.mostrar_linha()


def buscar_carona_por_rota():
    print('\n----- Buscar Carona -----')
    origem_busca = input('Digite a origem desejada: ').title()
    destino_busca = input('Digite o destino desejado: ').title()
    encontrou = False

    for email in caronas:
        origem, destino, data, hora, vagas, valor, passageiros = caronas[email]
        if origem == origem_busca and destino == destino_busca and vagas > 0:
            encontrou = True
            print(f'\nMotorista: {usuarios[email][0]}')
            print(f'De: {origem} para {destino}')
            print(f'Data: {data} - {hora}')
            print(f'Vagas: {vagas} - Preço: R${valor}')

    if not encontrou:
        print('\nNenhuma carona disponível para essa rota no momento')
    utilidade.mostrar_linha()


def reservar_vaga(email_passageiro):
    print('\n----- Reservar Vaga -----')
    origem2 = input('Digite a origem: ').title()
    destino2 = input('Digite o destino: ').title()
    encontrou = False

    for email_motorista in caronas:
        origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]
        if origem == origem2 and destino == destino2 and vagas > 0:
            encontrou = True
            print(f'\nCarona encontrada:')
            print(f'Motorista: {usuarios[email_motorista][0]}')
            print(f'De: {origem} para {destino}')
            print(f'Data: {data} - {hora}')
            print(f'Vagas: {vagas} - Preço: R${valor}')

            confirmar = input('\nReservar esta vaga? (s/n): ').lower()
            if confirmar == 's':
                caronas[email_motorista][4] -= 1
                caronas[email_motorista][6].append(email_passageiro)
                print('\nReserva confirmada!')
            else:
                print('reserva cancelada')
            break

    if not encontrou:
        print('\nNenhuma carona disponível para essa rota.')
    utilidade.mostrar_linha()


def cancelar_reserva(email_usuario):
    print('\n----- Cancelar Reserva -----')
    encontrou_reserva = False

    for email_motorista in caronas:
        origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]
        if email_usuario in passageiros:
            encontrou_reserva = True
            print(f'\nReserva encontrada:')
            print(f'Motorista: {usuarios[email_motorista][0]}')
            print(f'De: {origem} para {destino}')
            print(f'Data: {data} - {hora}')

            confirmar = input('Cancelar reserva? (s/n): ').lower()
            if confirmar == 's':
                caronas[email_motorista][6].remove(email_usuario)
                caronas[email_motorista][4] += 1
                print('Reserva cancelada com sucesso!')
            break

    if not encontrou_reserva:
        print('Você não tem reservas ativas.')
    utilidade.mostrar_linha()


def remover_carona(email_motorista):
    print('\n------- REMOVER CARONA -------')

    if email_motorista not in caronas:
        print('Você não tem caronas cadastradas!')
        utilidade.mostrar_linha()
        return
    origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]
    print(f'Carona encontrada: de {origem} para {destino} em {data}')

    confirmacao = input('Tem certeza que deseja remover sua carona? (s/n): ').lower()
    if confirmacao == 's':
        del caronas[email_motorista]
        print('Sua carona foi removida com sucesso!!!')
    else:
        print('operação cancelada')

    utilidade.mostrar_linha()


def mostrar_detalhes_carona():
    print('\n-------Mostrar detalhes da carona-------')
    detcar_email = input('insira os dados do email do motorista: ')
    detcar_data = input('insira os dados da data no formato dd/mm/aa: ')

    if detcar_email in caronas:
        origem, destino, data, hora, vagas, valor, passageiros = caronas[detcar_email]
        if detcar_data == data:
            print(f'\nMotorista: {usuarios[detcar_email][0]}')
            print(f'De {origem} para {destino}')
            print(f'Dia: {data} - {hora}')
            print(f'Vagas: {vagas} - Preço: R${valor}')
            print(f'Passageiros: {passageiros}')
        else:
            print('Data não corresponde à carona deste motorista.')
    else:
        print('Carona não encontrada com os dados fornecidos.')
    utilidade.mostrar_linha()


def mostrar_caronas_cadastradas(email_usuario):
    print('\n----------CARONAS QUE VOCÊ SE CADASTROU------------')
    encontrou_caronas = False

    for email_motorista in caronas:
        origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]
        if email_usuario in passageiros:
            encontrou_caronas = True
            print(f'\nMotorista: {usuarios[email_motorista][0]}')
            print(f'De {origem} para {destino}')
            print(f'Dia: {data} - {hora}')
            print(f'Vagas: {vagas} - Preço: R${valor}')

    if not encontrou_caronas:
        print('\nVocê não está cadastrado em nenhuma carona no momento.')
    utilidade.mostrar_linha()

def carteira_motorista_relatorio():
    print('\n---------- CARTEIRA DO MOTORISTA ------------')
    total_geral = 0
    caronas_encontradas = False
    email_login = usuarios

    for email_motorista in caronas:
        if email_motorista == email_login:
            caronas_encontradas = True
            origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]
            vagas_ocupadas = int(vagas) - len(passageiros)
            total_carona = vagas_ocupadas * float(valor)
            total_geral += total_carona

            print(f'\nDe: {origem} para {destino}')
            print(f'Data/Horário: {data} - {hora}')
            print(f'Valor por vaga: R${valor}')
            print(f'Vagas restantes: {vagas}')
            print(f'Vagas ocupadas: {vagas_ocupadas}')
            print(f'Total desta carona: R${total_carona}')

    if caronas_encontradas:
        print(f'\nTOTAL GERAL A RECEBER: R${total_geral:.2f}')
    else:
        print('\nNão há caronas cadastradas')
    utilidade.mostrar_linha()


