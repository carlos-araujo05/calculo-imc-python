# Fórmula IMC:
# IMC = peso / (altura x altura)

# Peso normal quando IMC está entre 18,5 e 24,9 

peso = float(input("Informe o seu peso em KG: "))
altura = float(input("Agora informe a sua altura: "))

def calculaImc():
    return peso / (altura * altura)

IMC = calculaImc()

if IMC >= 18.5 and <= 24.9:


print(f'Seu IMC é {IMC:.1f}')