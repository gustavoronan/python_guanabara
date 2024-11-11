#Um programa que calcule todos o numeros impares, multiplos de 3 que se encontram em um intervalo de 1 a 500

soma = 0
contador = 0
for c in range (1, 501):
    if c % 2 != 0 and c % 3 == 0:
     soma = soma + c
     contador = contador + 1
print(soma)  
print(contador)   