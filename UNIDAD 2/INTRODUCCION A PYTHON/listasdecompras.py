#Se crea una lista llamada listas_compras
listas_compras = []

print (" 🛒 Lista de Compra 🛒")

#Agregar producto
producto1=input("Agrega el primer producto: ")
listas_compras.append(producto1)

#Agregar Producto
producto2=input("Agregar el segundo producto: ")
listas_compras.append(producto2)


#Agregar Producto3
producto3=input("Agregar el segundo producto: ")
listas_compras.append(producto3)

print("\n Tu lista de compra es: ")
for producto in listas_compras:
	print (f"- {producto}")

print("\n ✔️ ¡Lista creada con exito!")
