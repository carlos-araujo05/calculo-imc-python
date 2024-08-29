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

def calcula_imc(peso:float, altura:float):
    return peso / (altura **2)

IMC = calcula_imc(peso='1', altura=altura)

texto = ''

if 18.5 <= IMC <= 24.9:
    texto = 'Parabéns, você está no peso ideal!'
elif IMC < 18.5:
    texto = 'Cuidado, seu peso está abaixo do indicado!'
else:
    texto = 'Cuidado, seu peso está acima do indicado!' 

print(f'Seu IMC é de {IMC:.1f}')
print(texto)