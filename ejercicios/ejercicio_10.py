if __name__ == "__main__":

    def calcular_factorial(numero):
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial
        
        
    numero = int(input("Ingrese el numero al que desea encontrarle el facotorial: "))
    resultado = calcular_factorial(numero)
    print(resultado)

    