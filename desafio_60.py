#Um programa que receba um numero e mostre seu fatorial
from math import factorial

num = int (input("Digite um numero para calcular seu fatorial: "))
fat = factorial(num)

print(f"O fatorial de {num} é {fat}")