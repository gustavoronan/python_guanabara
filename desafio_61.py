#Refazer o desafio 51
termo1 = int(input("Insira o primeiro termo: ")) #recebe o termo
razao = int(input("Insira a razão: ")) #recebe a razap
count = 1 #contador inicia em um, vai auxiliar para mostrar os 10 termos solicitados
while count <= 10: #enquanto contador for menor igual a 10
    print(f"{termo1}", end=' ')
    termo1 += razao
    count += 1