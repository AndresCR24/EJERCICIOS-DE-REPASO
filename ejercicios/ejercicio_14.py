if __name__ == "__main__":

    def sumar_lista(lista):

        suma = 0
        for numero in lista:
            suma += numero

        return suma

    lista_numeros = []
    cantidad_numeros = int(input("Ingrese la cantidad de numeros que quieres que tenga la lista: "))
    control = 1

    while(cantidad_numeros >= control):
        numero = float(input(("ingresa tu numero #" +str(control)+ ": ")))
        lista_numeros.append(numero)
        control += 1
    
    mayor = max(lista_numeros)
    menor = min(lista_numeros)
    print(lista_numeros)
    promedio = (sumar_lista(lista_numeros))/cantidad_numeros
    print(F"El promedio de la lista de numeros es {promedio}")