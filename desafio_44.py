#calculadora de descontos
#a vista 10% desconto / avista no cartão 5% desconto / em até 2x preço normal / 3x ou mais 20% juros

valor_prod = float(input("Insira o valor do produto: "))

print("Metodos de pagamento \n 1- a vista = 10% desconto \n 2- a vista no cartao = 5% desconto \n 3- 2x cartao = preço normal \n 4- 3x ou mais 20% juros")
opc_pag = int(input("\nInsira o metodo de pagamento de acordo com o numero a esquerda: \n"))
if opc_pag > 4:
    print("Escolha invalida")
elif opc_pag == 1:

    valor_prod = valor_prod * 0.90

    print(f"O valor final do produto com desconto aplicado fica {valor_prod} reais")
elif opc_pag == 2:
    
    valor_prod = valor_prod * 0.95

    print(f"O valor final do produto com desconto aplicado fica {valor_prod} reais")
elif opc_pag == 3:
    print(f"O valor continua o mesmo para esta opção {valor_prod} reais")
else:
    
    valor_prod = valor_prod * 1.2

    print(f"O valor final do produto com acréscimo aplicado fica {valor_prod} reais")