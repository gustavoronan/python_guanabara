#Tabuada de varios numeros, um de cada vez para cada valor digitado pelo usuario, programa para ao inserir um valor negativo

while True:
    numero = int(input("Insira um numero para visualizar sua tabuada: "))
    if numero < 1:
        break
    for multiplicador in range (1,11):
        print("{} x {} = {}".format(numero, multiplicador, numero*multiplicador))
    print("=-="*13)
    
    print("Digite um valor negativo para parar")
    print("-"*13)
