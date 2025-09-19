#Van a crear una lista vacia con su nombre y van a agregar 5 elementos con input:
#(Nombre, Preparatoria, Lugar de Residencia, Edad, Carrera)

ListasDatos = []

print ("Lista de Registro")

#Agregar Registro1
Registro1=input("Dame tu Nombre: ")
ListasDatos.append(Registro1)

#Agregar Registro2
Registro2=input("Dame el nombre de tu Prepa: ")
ListasDatos.append(Registro2)


#Agregar Registro3
Registro3=input("Escribe tu Lugar de Residencia: ")
ListasDatos.append(Registro3)

#Agregar Registro4
Registro4=input("Dame tu Edad: ")
ListasDatos.append(Registro4)

#Agregar Registro5
Registro5=input("Dame tu Carrera: ")
ListasDatos.append(Registro5)

print("\n Tu lista de registro es: ")
for producto in ListasDatos:
	print (f"- {producto}")

print("\n ✔️ ¡Lista creada con exito!")