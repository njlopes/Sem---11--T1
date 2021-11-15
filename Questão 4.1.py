def compra(opção):
    if opção == 'H':
        return 5.5
    elif opção == 'C':
        return 6.8
    elif opção == 'M':
        return 4.5
    elif opção == 'A':
        return 7
    elif opção == 'Q':
        return 4
    else:
        print('Opção inválida.')
        return 0

def main(): 
    total = 0
    while True:        
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        opção = input().strip().upper()[0]        
        if opção == 'X' :
            print(f'{total:.2f}')
            break
        else:
            total += compra(opção)

if __name__ == '__main__':
    main()
