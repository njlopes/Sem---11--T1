opção = 0
while True:
    print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
    opção = int(input())

    if opção == 1:
        print('1 - Olá. Como vai?')

    elif opção == 2:
        print ('2 - Vamos estudar mais.')

    elif opção == 3:
        print('3 - Meus Parabéns!')


    elif opção == 0:
        print('0 - Fim de serviço.')
        break
    else:
        print('Opção inválida.')
        
        

    
