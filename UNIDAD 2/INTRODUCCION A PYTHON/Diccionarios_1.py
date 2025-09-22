#Se declara la Variable
Edades={
	"Brayan" : 25,
	"Luis" : 30,
	"Jose" : 22
}

#Declaramos a luis
print("Edad de Luis:", Edades["Luis"])
Edades["Brayan"] = 28
print("\nDespues de añadir a Brayan:")
print(Edades)

#Se actualiza la edad de Luis
Edades["Luis"] = 26
print("\nDespues de actualizar la edad de luis:")
print (Edades)

#Se elimina a Jose
del Edades["Jose"]
print("\nDespues de eliminar a Jose:")
print(Edades)

print("\nRecorriendo el diccionario:")
for Nombre,Edad in Edades.items():
	print (f"{Nombre} tiene {Edad} años")