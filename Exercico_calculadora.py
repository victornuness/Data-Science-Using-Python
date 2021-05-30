def calculadora(n1,n2,operador):
    if operador == '+':
        resultado=n1 + n2
        print(resultado)
    if operador == '-':
        resultado=n1 + n2
        print(resultado)
    if operador == '*' or operador == 'x':
        resultado=n1 * n2
        print(resultado)
    if operador == '/' :
        if n2 == 0:
            print('Não é possivel fazer divisão por zero')
            resultado=0
            print(resultado)
        else :
            resultado=n1 / n2
    if operador == '^' or operador == '**':
            resultado=n1 ** n2
    print(resultado)
    return resultado


calculadora(1,2,'+')
