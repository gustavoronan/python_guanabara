#Ler 7 datas de nascimento e retornar quais são maiores de idade
import datetime

today = datetime.datetime.today()
ano = today.year

date = datetime(input("Insira sua data de nascimento: "))

print(date)