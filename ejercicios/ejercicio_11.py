if __name__ == "__main__":
    numero = 1
    lista_numeros = []
    while numero <= 100:
        if numero % 2 == 0:
            print(f"El nunero {numero} es par")
            lista_numeros.append(numero)

        numero += 1

    print(lista_numeros)
