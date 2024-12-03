name = "Julian V"
age  = 19
heigth = 1.73
teacher  = False
trainer = True
#Conjunto de datos
hobbies = list()
hobbies = ["Cocinar", "Programar", "Jugar", "Dormir", "Musica"]

#print(name, age, heigth, teacher, trainer, hobbies)
print(hobbies[2])
print(len(hobbies))

hobbies[2]="Despertarme"
print(hobbies)


dato = input("Ingrese otro pasatiempo:")

hobbies.append(dato)