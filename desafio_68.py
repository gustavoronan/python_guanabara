#Um programa que jogue par ou impar com o computador, sera interrompido quando o jogador perder, deve mostrar quantas vitorias do jogador
contador = 0
from random import randint
while True:
    computer_numer = randint(0,10)
    user_choice_number = int(input("Insira o seu número: "))
    user_choice = str(input("Insira sua Par ou Impar [P/I]: ").upper())
    
    final = user_choice_number + computer_numer

    if user_choice == 'P' and final % 2 == 0:
        print("Parabén você venceu")
        contador = contador + 1
    elif user_choice == 'I' and final % 2 != 0:
        print("Parabén você venceu")
        contador = contador + 1
    else:
        break
print(f"Você perdeu, mas saiu com {contador} vitorias")