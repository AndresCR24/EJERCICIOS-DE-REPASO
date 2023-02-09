import math

if __name__ == "__main__":

    radio_circulo = int(input("Ingrese el radio del circulo: "))
    area_circulo = round((math.pi*(radio_circulo)**2),2)
    area_circulo = str(area_circulo)
    print("El area del circulo es "+area_circulo)