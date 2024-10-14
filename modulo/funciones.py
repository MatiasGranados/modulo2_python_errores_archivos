#LISTA para el historial
historial = []

def suma():
    print('ELEGISTE LA OPCIÓN DE SUMA')
    num1 = float(input("INGRESE NUMERO 1:"))
    num2 = float(input("INGRESE NUMERO 2:"))
    suma = num1+num2
    print('LA SUMA DE',num1,'+',num2,'ES IGUAL A',suma)
    h = '{a} + {b} = {c}'.format(a=num1, b=num2, c=suma)
    historial.append(h)

def resta():
    print('ELEGISTE LA OPCIÓN DE RESTA')
    num1 = float(input("INGRESE NUMERO 1:"))
    num2 = float(input("INGRESE NUMERO 2:"))
    resta = num1-num2
    print('LA RESTA DE',num1,'-',num2,'ES IGUAL A',resta)
    h = '{a} - {b} = {c}'.format(a=num1, b=num2, c=resta)
    historial.append(h)

def multiplicacion():
    print('ELEGISTE LA OPCIÓN DE MULTIPLICACIÓN')
    num1 = float(input("INGRESE NUMERO 1:"))
    num2 = float(input("INGRESE NUMERO 2:"))
    multiplicacion = num1*num2
    print('LA MULTIPLICACIÓN DE',num1,'X',num2,'ES IGUAL A',multiplicacion)
    h = '{a} * {b} = {c}'.format(a=num1, b=num2, c=multiplicacion)
    historial.append(h)

#IMPLEMENTACIÓN DE MANEJO DE ERRORES CON TRY EXCEPT
def division():
    print('ELEGISTE LA OPCIÓN DE DIVISIÓN')
    num1 = float(input("INGRESE NUMERO 1:"))
    num2 = float(input("INGRESE NUMERO 2:"))
    try:
        division = num1/num2
        print('LA DIVISIÓN DE',num1,'/',num2,'ES IGUAL A',division)
        h = '{a} / {b} = {c}'.format(a=num1, b=num2, c=division)
        historial.append(h)
    except Exception:
        print("Error de calculo. Estoy utilizando Manejo de errores")