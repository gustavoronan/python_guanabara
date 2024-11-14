#Sequencia de Fibonacci

n = int(input("Quantos termos você deseja mostrar?: \n"))
termo1 = 0 #por padrao o primeiro termo é zero
termo2 = 1 #por padrao o segundo termo é um
print("=="*30)

print(f"{termo1}  {termo2}", end= ' ')

cont = 3 #iniciando no 3 pq ja temos o primeiro e o segundo termo
while cont <= n:
    termo3 = termo1 + termo2 #sempre o termo3 vai ser a soma do 1 e do 2
    print(f"{termo3}",end= ' ')
    cont = cont + 1 #segue o loop de repetições
    termo1 = termo2 #faz com que ele ande uma casa ao lado
    termo2 = termo3#faz com que ele ande uma casa ao lado

