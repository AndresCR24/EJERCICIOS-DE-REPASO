#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y
#división.
if __name__ == "__main__":

    numero_1 = float(input("Ingrese un numero: "))
    numero_2 = float(input("Ingrese un segundo numero: "))

    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    division = numero_1 / numero_2

    print(f"El resultado de sumar tus dos numeros es {suma}")
    print(f"El resultado de restar tus dos numeros es {resta}")
    print(f"El resultado de multiplicar tus dos numeros es {multiplicacion}")
    print(f"El resultado de dividir tus dos numeros es {division}")