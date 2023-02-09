if __name__ == "__main__":
    lista_numeros = []
    cantidad_numeros = int(input("Ingrese la cantidad de numeros que quieres que tenga la lista: "))
    control = 1

    while(cantidad_numeros >= control):
        numero = float(input(("ingresa tu numero #" +str(control)+ ": ")))
        lista_numeros.append(numero)
        control += 1
    
    mayor = max(lista_numeros)
    menor = min(lista_numeros)
    print(f"El numero mayor es: {mayor}")
    print(f"El numero menor es: {menor}")