# Fórmula IMC:
# IMC = peso / (altura x altura)

# Peso normal quando IMC está entre 18,5 e 24,9 

def solicitar_valor(mensagem: str):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

try:
    peso = float(input("Informe o seu peso em KG: "))
except ValueError as e:
    peso = float(input("Valor inválido. Informe o seu peso novamente: "))

try:
    altura = float(input("Agora informe a sua altura: "))
except ValueError as e:
    altura = float(input("Valor inválido. Informe a sua altura novamente: "))
    

def calculaImc():
    return peso / (altura * altura)

IMC = calculaImc()

text = ''

if IMC >= 18.5 and IMC <= 24.9:
    text = 'Parabéns, você está no peso ideal!'
elif IMC < 18.5:
    text = 'Cuidado, seu peso está abaixo do indicado!'
else:
    text = 'Cuidado, seu peso está acima do indicado!' 

print(f'Seu IMC é de {IMC:.1f}')
print(text)