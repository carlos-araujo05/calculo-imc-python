# Fórmula IMC:
# IMC = peso / (altura x altura)

peso = float(input("Informe o seu peso em KG: "))
altura = float(input("Agora informe a sua altura: "))

def calculaImc():
    return peso / (altura * altura)

IMC = calculaImc()

print(f'Seu IMC é {IMC:,.2f}')