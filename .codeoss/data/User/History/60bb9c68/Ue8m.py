# Fórmula IMC:
# IMC = peso / (altura x altura)

# Peso normal quando IMC está entre 18,5 e 24,9 

peso = float(input("Informe o seu peso em KG: "))
altura = float(input("Agora informe a sua altura: "))

def calculaImc():
    return peso / (altura * altura)

IMC = calculaImc()

text = ''
teste: int = 0
if IMC >= 18.5 and IMC <= 24.9:
    text = 'Parabéns, você está no peso ideal!'
elif IMC < 18.5:
    text = 'Cuidado, seu peso está abaixo do indicado!'
else:
    text = 'Cuidado, seu peso está acima do indicado!' 

print(f'Seu IMC é {IMC:.1f}')
print(text)