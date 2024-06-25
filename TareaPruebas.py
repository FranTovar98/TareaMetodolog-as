def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

while True:
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    c = int(input("Escoja qué operación desea realizar:\n 1) Suma\n 2) Resta\n 3) Multiplicación\n 4) División\n"))

    if c == 1:
        resultado = suma(a, b)
        operacion = "suma"
    elif c == 2:
        resultado = resta(a, b)
        operacion = "resta"
    elif c == 3:
        resultado = multiplicacion(a, b)
        operacion = "multiplicación"
    elif c == 4:
        resultado = division(a, b)
        operacion = "división"
    else:
        resultado = None
        operacion = "operación inválida"

    if resultado is not None:
        print(f"La {operacion} entre {a} y {b} es: {resultado}")
    else:
        print("Selección de operación no válida.")

    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        break

print("Gracias por usar la calculadora.")
