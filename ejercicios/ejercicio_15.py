if __name__ == "__main__":

    def palindromo(cadena):
        posicion_izquierda = 0
        posicion_derecha = len(cadena) - 1

        while posicion_derecha >= posicion_izquierda:
            if not cadena[posicion_izquierda] == cadena[posicion_derecha]:
                return False
           
            posicion_derecha -= 1
            posicion_izquierda += 1

        print("Es palindroma")
        return True
       

letra_palindromo = str(input("Ingrese la palabra que quieres saber si es palindroma: "))

print(palindromo(letra_palindromo))