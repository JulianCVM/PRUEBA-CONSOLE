#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
#de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras: c2=a2+b2
import math
a = int(input("Ingrese el cateto a: "))
b = int(input("Ingrese el cateto b: "))
c =  math.sqrt(a**2 + b**2)
print(f"La hipotenusa es: {c}")