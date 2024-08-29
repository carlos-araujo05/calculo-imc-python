# Fórmula IMC:
# IMC = peso / (altura x altura)

peso = input("Informe o seu peso em KG: ")
altura = input("Agora informa a sua altura: ")

def calculaImc():
    return peso / (altura * altura)

IMC = calculaImc()

printf(r"Seu IMC é {IMC}")