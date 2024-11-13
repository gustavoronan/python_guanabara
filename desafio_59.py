#Um programa que receba 2 valores e de um menu de opcoes: somar, multiplicar, novos numeros, sair
valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
menu = 0

while menu != 4:
    
    print(" 1 = Somar \n 2 = Multiplicar \n 3 = Alterar valores \n 4 = Sair")
    menu = int(input("Selecione uma opção: "))
    if menu > 4:
        print("Opção inexistente! ")

    match menu:
        case 1:
            soma = valor1 + valor2
            print(f"O resultado foi {soma} \n")
            print("=="*12)
        case 2:
            mult = valor1 * valor2
            print(f"O resultado foi {mult} \n")
            print("=="*12)
        case 3:
            valor1 = int (input("Insira seu novo valor: "))
            valor2 = int (input("Insira seu segundo novo valor: "))    
        case 4: 
            break
