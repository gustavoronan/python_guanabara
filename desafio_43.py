#calculadora de IMC

peso = float (input("Insira seu peso \n"))
altura = float (input("Insira sua altura \n"))

imc_calc = peso / (altura + altura)

if imc_calc < 18.5:
    print("Abaixo do peso")
elif imc_calc >= 18.5 and imc_calc < 25:
    print("Peso ideal") 
elif imc_calc >= 25 and imc_calc < 30:
    print("Sobrepeso")
elif imc_calc >=30 and imc_calc < 40:
    print ("Obesidade")
else:
    print ("Obesidade mórbida")
       