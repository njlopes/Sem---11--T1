def main():
    s = 0
    while True:
        numero = input('CÓDIGO  PRODUTO         PREÇO (R$) \nH       Hamburger       5,50 \nC       Cheeseburger    6,80 \nM       Misto Quente    4,50 \nA       Americano       7,00 \nQ       Queijo Prato    4,00 \nX       PARA TOTAL DA CONTA \n') .strip().upper() [0]
        h = 5.50
        c = 6.80
        m = 4.50
        a = 7.00
        q = 4.00
        if numero!='X':
           if numero == 'H':
              s += h
           if numero == 'C':
              s += c
           if numero == 'M':
               s += m
           if numero == 'A':
               s += a
           if numero == 'Q':
               s += q
        if numero == 'X':
            break
    print('%.2f'%s)
    
   
if __name__ == '__main__':
   main()
