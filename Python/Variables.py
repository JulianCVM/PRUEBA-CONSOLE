#Tipos de datos primitivos
#String, int, char, float, bool
name = "Julian V"
age  = 19
heigth = 1.73
teacher  = False
trainer = True
#Conjunto de datos
hobbies = list()
hobbies = ["Cocinar", "Programar", "Jugar", "Dormir", "Musica"]

#print(name, age, heigth, teacher, trainer, hobbies)
#Se imprime la lista
print(hobbies[2])
print(len(hobbies))
#Se asigna un valor a un espacio en la lista, se cambia el valor
hobbies[2]="Despertarme"
print(hobbies)

#Se solicita un dato
dato = input("Ingrese otro pasatiempo:")
#Se ingresa un dato
hobbies.append(dato)
#Se elimina un dato
hobbies.pop(2)
print(hobbies)

