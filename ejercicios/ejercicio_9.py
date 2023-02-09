if __name__ == "__main__":

    def crear_matriz(m,n):

        return[[i*j for j in range(n)] for i in range (m)]

    filas = int(input("Ingrese le numero de filas: "))
    columnas = int(input("Ingrese el numero de columnas: "))

    matriz = crear_matriz(filas, columnas)

    print(matriz)