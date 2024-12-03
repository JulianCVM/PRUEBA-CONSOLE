#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
import math
radio = int(input("Ingrese el radio: "))
perimetro = 2 * math.pi * radio
area = (radio**2) * math.pi 
print("El área del círculo es: ", area)
print("El perimetro del círculo es: ", perimetro)