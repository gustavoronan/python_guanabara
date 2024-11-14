#Um programa que simule um caixa eletronico, pergunte o valor inicial a ser sacado, e o programa vai informar quantas cedulas sera entregues
#considerando, R$50 R$20 R$10 R$1

print("ULTIMO EX DO MUNDO 2")
print("=-"*20)
valor = int(input("Insira o valor a ser sacado: "))
total = valor
ced = 50
totced = 0

while True:
    if total>= ced: #se o total que seria o valor for maior que ced que inicia com 50
        total -= ced #eu começo retirando uma cedula e diminuindo do total
        totced += 1 #como estou tirando uma cedula, somo uma cedula que foi retirada
    else: #se o total for menor que cedula que inicia com 50

        if totced > 0: #o total de cedulas deve ser maior que 0 para ser printado na tela
            print(f"Total de {totced} cédulas de R${ced}")

        if ced == 50: #entao cedula que valia 50 
            ced = 20#passa a valer 20
        elif ced == 20:#oque era 20
            ced = 10   #passa a valer 10
        elif ced == 10: #oque era 10
            ced = 1 #passa a valer 1
        totced = 0 #sempre que inicia em um destes ifs o total de cedula zera
        if total == 0: #se acabou o dinheiro....
            break #para a aplicacao

print("=="*14)