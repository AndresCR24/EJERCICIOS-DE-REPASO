#Escribir un programa que determine si un número dado es par o impar.

if __name__ == "__main__":
    numero_ingresado = int(input("Ingrese un numero: "))

    if numero_ingresado % 2 == 0:
        print("El numero es par ")

    else:
        print("El numero es impar")
