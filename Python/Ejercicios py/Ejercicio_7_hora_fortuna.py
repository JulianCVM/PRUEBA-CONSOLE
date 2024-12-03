#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, 
# que indique qué hora marcará el reloj dentro de h horas:

t = int(input("Ingrese la hora actual del reloj: "))
h = int(input("Ingrese el número de horas: "))
hora = t+h
excedente = round(hora / 12)
print(excedente)
if excedente > 0:
    for i in range(excedente):
        if excedente>i:
            print(f"La hora es: {hora-12*i}")
        elif excedente<i:
            print(f"La hora es: {hora}")
else:
    print(f"La hora es: {hora}")