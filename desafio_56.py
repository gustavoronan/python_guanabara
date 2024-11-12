#Um programa que leia, nome idade e sexo de 4 pessoas, e retorne
# - A média de idade do grupo, o nome do homem mais velho, quantas mulheres tem menos de 20 anos

somaidade = 0 #varivel que vai armazenar a soma de idade
mediaidade = 0 # variavel que vai armazenar a media final de idade
maioridadehomem = 0 #variavel que vai armazenar a maior idade do homem
nomevelho = '' #variavel que vai armazenar o nome da do homem mais velho
totmulher20 = 0 #variavel que vai armazenar o total de mulheres com menos de 20 anos

for p in range (1, 5):
    print(f'-----{p} PESSOA ------')
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    somaidade += idade #basicamente somando todas as idade inseridas manualmente

    if p == 1 and sexo == 'M': #se a pessoa da primeira posiçao for homem
        maioridadehomem = idade #maioridade vai receber a idade inserida 
        nomevelho = nome #nomevelho vai receber o nome inserido

    if sexo == 'M' and idade>maioridadehomem: #se sexo for masculino e a idade for maior que a maioridade anterior
        maioridadehomem = idade #maioridade recebe idade
        nomevelho = nome #nomevelho recebe nome

    if sexo == 'F' and idade < 20: #se sexo for feminino e idade menor que 20 anos
        totmulher20 +=1        

mediaidade = somaidade / 4

print(f"A media de idade do grupo é de {mediaidade} anos")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho} ")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos")