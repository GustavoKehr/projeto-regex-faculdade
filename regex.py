import re
def validacao_email(email):
    regex = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        return False

email = input("Digite o endereço de email: ")

if validacao_email(email):
    print("O endereço de email é válido.")
else:
    print("O endereço de email é inválido.")
