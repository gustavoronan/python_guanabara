#Faça um programa que leia o ano de nascimento de um jovem e inform
# de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar
#se é a hora de se alistar
#Se já passou do tempo do alistamento
#Seu programa tambem deve mostrar o tempo que falta ou que passou do prazo

import datetime

ano_rec = int(input("Qual em que ano voce nasceu? "))

data = datetime.datetime.today()
ano = data.year
idade_rec = ano - ano_rec

if idade_rec < 18:
    diferenca = 18 - idade_rec
    print(f"Você ainda é muito novo para se alistar, faltam {diferenca} anos para cumprir este objetivo!")
elif idade_rec == 18:
    print("Está na hora de se alistar")

else:
    diferenca = idade_rec - 18
    print(f"Ja passou da hora de se alistar, você esta {diferenca} anos atrasado!")



