#Desenvolver um programa para ler 6 numeros, e mostrar a soma dos numeros pares

soma = 0
for c in range (1,7):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        soma = soma + numero
print(soma)