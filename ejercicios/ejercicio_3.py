#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random
if __name__ == "__main__":
    
 lista_numeros_aleatorios = [random.randint(1,100) for i in range(0,15)]


 print(lista_numeros_aleatorios)

