num = 0
s = 0

while True:
    n = int(input('Digite um valor:'))
    if n != 0:
        s += n
    if n == 0: break


if s != 0:
    print('A soma é igual a: {}.'.format(s))
if s == 0:
    print ('A soma é igual a: 0')
