#Escreva um programa que leia dois numeros inteiros e compare-os
#mostrando na tela uma mensage:

#-O primeiro valor é maior
#O segundo valor eh maior
# Os numeros sao iguais

num1=float(input("Insira um valor decimal \n"))
num2 = float(input("Insira outro valor decimal \n"))

if num1 > num2:
    print("O primeiro valor é maior!")
elif num2 > num1:
    print("O segundo valor é maior!")
else:
    print("Os numeros fornecidos tem o mesmo valor!")