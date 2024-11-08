import datetime
#Um programa que leia o ano de nascimento de um atleta e
#mostre sua categoria de acordo com a idade

nasc_atleta = int (input("Insira a data de nascimento do atleta: "))

data = datetime.datetime.today()
ano = data.year
categoria = ano - nasc_atleta

if categoria <= 9:
    print("Sua categoria é mirim")

elif categoria > 9 and categoria <= 14:
    print("Sua categoria é Infantil")

elif categoria > 14 and categoria <= 19:
    print("Sua categoria é junior")

elif categoria == 20:
    print("Sua categoria é senior")    

else:
    print("Sua categoria é master")