count = 1
while count <=10:
    print(count)
    count = count + 1
print("==>"*13)
############

qnt = 1
par = impar = 0 #mesma coisa que colocar par=0 e impar =0
while qnt != 0:
    qnt= int(input("Insira um numero: "))
    if qnt !=0: 
        if qnt % 2 == 0:
            par = par + 1
        else:
             impar = impar + 1
print(f"Quantidade de pares: {par} \n Quantidade de impares: {impar}")    

#######################################################################
#Desafios
#Um programa que leia o sexo da pessoa mas que só aceite M ou F, caso errado, pedir ate ter um valor correto
#Um jogo onde o computador escolhe um numero aleatorio e voce tente acertar de 0 a 10
#Um programa que receba 2 valores e de um menu de opcoes: somar, multiplicar, novos numeros, sair
#Um programa que receba um numero e mostre seu fatorial
#Refazer o desafio 51
#Um programa que receba varios numeros inteiros, condicao de parada digitar 999, ao final somar todos os numeros
#Um programa que leia varios numeros inteiros, no final mostre a media entre eles e qual foi o menor e o maior numero entre eles

