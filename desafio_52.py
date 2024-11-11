#Um programa que leia um numero inteiro e retorne se é ou não um numero primo
num = int(input("Digite um número: "))
valid = 0
for c in range (1, num+1):
    if num % c == 0:
        print('\033[32m', end=' ')
        valid = valid + 1
    else:
        print('\033[31m', end=' ')
    print(f"{c}", end= ' ')

if valid == 2:
    print(f"\n O numero foi divisivel {valid} vezes, é um numero primo!")
else:
    print(f"\n O numero foi divisivel {valid} vezes, por tanto não é um número primo")