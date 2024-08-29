# Fórmula IMC:
# IMC = peso / (altura x altura)
import sys
import random
import tkinter as tk
from tkinter import messagebox

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Definição da janela
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Jogo da forca")

# Lista de palavras para o jogo
words = ["PYTHON", "JAVA", "JAVASCRIPT", "HTML",
         "CSS", "RUBY", "PHP", "MYSQL", "PYTHONIC"]

# Seleciona uma palavra aleatória
word = random.choice(words)

def select_word():
    return random.choice(words)


palavra_escolhida = select_word()


def reset_game():
    global word, guessed_letters, wrong_guesses
    word = palavra_escolhida
    guessed_letters = set()
    wrong_guesses = 0


def show_end_message(message):
    font = pygame.font.Font(None, 72)
    text_color = red if "perdeu" in message else green
    text = font.render(message, True, text_color)
    screen.blit(text, (275, 250))
    if "perdeu" in message:
        font = pygame.font.Font(None, 48)
        lost_next = font.render(f"A palavra era {palavra_escolhida}", True, red)
        screen.blit(lost_next,(275,320))
    pygame.display.flip()


def show_restart_message():
    font = pygame.font.Font(None, 36)
    text = font.render("Fim de jogo, deseja jogar novamente? (y/n)", True, white)
    screen.blit(text, (200, 350))
    pygame.display.flip()


def show_restart_popup():
    root = tk.Tk()
    root.withdraw()
    restart = messagebox.askquestion("Fim de jogo", "Deseja jogar novamente?")
    return restart


# Loop principal do jogo
while True:
    reset_game()  # Reinicia o jogo

    # Loop interno para controlar um único jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.add(letter)
                        if letter not in word:
                            wrong_guesses += 1

        # Limpa a tela
        screen.fill(black)

        # Verifica se o jogador ganhou
        if check_win():
            show_end_message("Você venceu!")
            restart_choice = show_restart_popup()
            if restart_choice == "yes":
                break  # Reinicia o jogo
            else:
                sys.exit()

        # Verifica se o jogador perdeu
        elif check_loss():
            show_end_message("Você perdeu!")
            restart_choice = show_restart_popup()
            if restart_choice == "yes":
                break  # Sai do loop interno
            else:
                sys.exit()

        # Atualiza a tela
        pygame.display.flip()


# peso = float(input("Informe o seu peso em KG: "))
# altura = float(input("Agora informe a sua altura: "))

# def calculaImc():
#     return peso / (altura * altura)

# IMC = calculaImc()

# print(f'Seu IMC é {IMC:.2f}')