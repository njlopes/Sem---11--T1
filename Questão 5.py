def main():
    numero=float(input())
    a=True
    while a==True:
          if numero>10 or numero<0:
               print('Nota inválida.') 
               numero=float(input())
          elif numero>=8.5:
               a=False
               print('A')
          elif numero>=7.0:
               a=False
               print('B')
          elif numero>=5:
               a=False
               print('C')
          elif numero>=4:
               a=False
               print('D')
          elif numero>=0:
               a=False
               print('E')             

if __name__== '__main__':
   main()
