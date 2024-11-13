#Um programa que leia o sexo da pessoa mas que só aceite M ou F, caso errado, pedir ate ter um valor correto
sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = str(input("Insira o sexo [M/F]: ").upper())
    if sexo == 'F' or sexo == 'M':
        print(f"O sexo introduzido foi {sexo}")  
    else:
        print("insira uma opção válida!")


 