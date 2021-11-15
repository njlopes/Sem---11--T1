def conceitos(nota):

    if nota >= 0.0 and nota <= 3.9:
        return "E"
    elif nota >= 4.0 and nota <= 4.9:
        return "D"
    elif nota >= 5.0 and nota <= 6.9:
        return "C"
    elif nota >= 7.0 and nota <= 8.4:
        return "B"
    elif nota >= 8.5 and nota <= 10:
        return "A"

def main():
    while True:
        nota = float(input())
        resultado = conceitos(nota)
        if(resultado):
            print(resultado)
            break
        else:
            print('Nota inválida.')

if __name__ == '__main__':
    main()
