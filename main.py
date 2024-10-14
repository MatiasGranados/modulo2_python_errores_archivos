from modulo.funciones import *
import files

def run():
    files.write_messages()
    files.read_messages()

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for mostrar in sorted(opciones):
        print(f' {mostrar}) {opciones[mostrar][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('SUMAR', suma),
        '2': ('RESTAR', resta),
        '3': ('MULTIPLICAR', multiplicacion),
        '4': ('DIVIDIR', division),
        '5': ('MOSTRAR HISTORIAL', mostrar_historial),
        '6': ('Salir', salir)
    }
    generar_menu(opciones, '6')

def mostrar_historial():
    print("EL HISTORIAL DE CALCULOS:", historial)

def salir():
    print('SALISTE DE LA CALCULAD0RA')

if __name__ == '__main__':
    menu_principal()
    run()