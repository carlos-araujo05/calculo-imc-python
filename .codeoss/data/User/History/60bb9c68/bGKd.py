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

peso = solicitar_valor("Informe o seu peso em KG: ")
altura = solicitar_valor("Agora informe a sua altura: ")

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