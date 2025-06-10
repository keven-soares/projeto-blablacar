from datetime import datetime

def mostrar_linha():
    print('-' * 50)

def verificar_email(email):
    while not ('@' in email and '.' in email.split('@')[1]):
        email = input('digite um email válido (deve conter @ e .com): ')

def verificar_data(data_str):
    try:
        data = datetime.strptime(data_str,"%d/%m/%Y")
        if data < datetime.now():
            print("Data inválida! Não pode ser no passado.")
            return False
        return True
    except ValueError:
        print("Formato inválido! Use dd/mm/aaaa.")
        return False

