#Um jogo onde o computador escolhe um numero aleatorio e voce tente acertar de 0 a 10
import random
list_number = [0,1,2,3,4,5,6,7,8,9,10]
user_choice = 0
contador = 0
escolha = random.choice(list_number)

user_choice = int(input("Adivinhe o número: "))
contador = contador + 1

while user_choice != escolha:
    user_choice = int(input("Errou, Adivinhe o número: "))
    contador = contador + 1
    if user_choice == escolha:
        print(f"Parabéns, você acertou!, precisou de {contador} tentativas")