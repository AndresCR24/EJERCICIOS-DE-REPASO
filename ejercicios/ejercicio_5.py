if __name__ == "__main__":
    
    ingrese_grados_Fahrenheit = int(input("Ingrese los grados Fahrenheit que desea convertir a grados celsius: "))
    formula_convertir = round((ingrese_grados_Fahrenheit -32)*(5/9),2)
    ingrese_grados_Fahrenheit = str(ingrese_grados_Fahrenheit)
    formula_convertir = str(formula_convertir)
    print(ingrese_grados_Fahrenheit+" Fahrenheit en celsius son "+formula_convertir)