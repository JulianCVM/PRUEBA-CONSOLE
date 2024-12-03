#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

num = input("Ingrese un número de 3 digitos: ")
longitud = len(str(num))
if longitud <= 3:
    numInvrtd = str(num)[::-1]
    print(f"El número invertido es: {numInvrtd}")
else:
    print("Ingrese un número valido de 3 cifras")