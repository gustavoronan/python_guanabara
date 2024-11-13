#Um programa que receba varios numeros inteiros, condicao de parada digitar 999, ao final somar todos os numeros

num = 0
cont = 0
soma = 0
num = int(input("Insira um valor ou 999 para parar: "))

while num != 999:
    cont += 1
    soma = soma + num
    num = int(input("Insira um valor ou 999 para parar: "))

print(f"Voce digitou {cont} numeros e a soma entre eles é {soma}")
   

