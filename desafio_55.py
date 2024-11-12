#Um programa que leia o peso de 5 pessoas, no final mostre qual foi o maior e o menor peso
maior = 0
menor = 0
for c in range (1, 5+1):
    peso = float(input(f"Insira o peso da pessoa {c}: "))
    if c == 1: #Se for o primeiro laço de rep
        maior = peso # maior recebe o valor de peso
        menor = peso# menor recebe o valor de peso
        #isso ocorre pq ambos sao maior e menor, por serem o primeiro laço 
    else: #se nao for o primeiro laço
        if peso > maior:
            maior = peso #maior passa a receber peso que foi inserido
        if peso < menor:
            menor = peso    #menor passa a receber peso que foi inserido
print (f"O maior peso foi de {maior} kg")
print (f"O menor peso foi de {menor} kg")
