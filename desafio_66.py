#Um programa que leia varios numeros inteiros, so para quando digitado 999, mostrar quantidade de numeros digitados e a soma


cont = 0
soma = 0
while True:
    num = int(input("Insira um numero inteiro: "))
    if num == 999:
        break
    soma = soma + num
print(f"A soma dos valores é: {soma}")