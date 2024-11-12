#Ler 7 datas de nascimento e retornar quais são maiores de idade
from datetime import date

today = date.today()
ano_atual = today.year
contador = 0
cont_menor = 0


for c in range (1, 7+1):
    data_nasc = int (input("Digite o ano de nascimento: "))
    idade = ano_atual - data_nasc
    print("==>"*11)    
    if idade >=18:
        contador = contador + 1
    else:
        cont_menor = cont_menor + 1
print(f"Você tem {contador} pessoas maiores de idade!")
print(f"Você tem {contador} pessoas menores de idade!")
    

