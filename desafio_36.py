#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar 
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário
#ou então o emprestimo será negado

casa_value = float(input("Qual o valor a ser pago na casa? \n "))
salario_comp = float(input("Qual sua renda mensal? \n "))
periodo_pag = int(input("Em quantos anos deseja quitar a casa? \n "))

periodo_pag = periodo_pag * 12
prestacao_mes = casa_value / periodo_pag

if prestacao_mes > salario_comp * 0.30:
    print("Você não tem pataco pra comprar esta propriedade, o emprestimo foi negado")
else:
    print("Voce foi aprovado")