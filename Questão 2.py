somaidade = 0
mediaidade = 0
pessoas = 0
maior = 0
menor = 0
cont = 0
while True:
    idade = int(input())
    cont += 1
    if idade == 0: break
    somaidade += idade
    pessoas += 1
    mediaidade = somaidade / pessoas
    if cont == 1:
        maior = menor = idade
    
    else:
        if idade > maior:
            maior = idade
        elif idade < menor:
            menor = idade

if pessoas != 0:
    print(pessoas)
if mediaidade != 0:
    print(round(mediaidade,2))
if menor != 0:
    print(menor)
if maior != 0:
    print(maior)











    
