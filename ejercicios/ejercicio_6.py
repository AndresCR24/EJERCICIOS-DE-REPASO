if __name__ == "__main__":

    def sumar_lista(lista):

        suma = 0
        for numero in lista:
            suma += numero

        return suma

    numeros = [1,2,3,4,5,6,7,8,9,10]
    print(sumar_lista(numeros))