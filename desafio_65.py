#Um programa que leia varios numeros inteiros, no final mostre a media entre eles e qual foi o menor e o maior numero entre eles
num = 0
cond = ''
media = 0
count_num = 0
soma = 0
maior = 0
menor = 0
while cond != "N":
    num = int(input("Insira um valor: "))
    cond = str(input("Deseja continuar? [S/N]: ").upper())
    count_num = count_num + 1
    soma = soma + num
    if count_num == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num    
media = soma / count_num
print(f"Quantidade de numeros inseridos {count_num}")
print(f"Media dos valores inseridos {media}")
print(f"Menor numero = {menor}, maior numero = {maior}")
