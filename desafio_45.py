#jokenpo com o computador

import random
list_opc = ["Pedra", "Papel", "Tesoura"]
input("Digite sua escolha: ")
escolha = random.choice(list_opc)
print(f"O computador escolheu {escolha}")