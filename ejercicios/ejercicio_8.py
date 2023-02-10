#Crear una función que invierta el orden de los elementos en una lista dada.
if __name__ == "__main__":

    lista = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]

    def invertir_lista(lista):
        
      lista = lista [::-1]
      return lista

    print(invertir_lista(lista))