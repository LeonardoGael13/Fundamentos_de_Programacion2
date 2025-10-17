from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass

class Bicicleta(Vehiculo):
    pass

# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
bici1= Bicicleta("Specialized Rockhopper", "MTB", "2015", "Negro")
auto2= Auto("Toyota", "Corolla", "2022", "Gris Metalico")
moto2= Moto("Yamaha", "MT-07", "2023", "Azul Oscuro")
camion2= Camion("Volvo", "FH16", "2021", "Blanco")
bici2= Bicicleta("Trek", "Marlin 7", "2024", "Rojo")
#Otra instancia

# Visualización
print()
print(auto1)
print()
print(moto1)
print()
print(camion1)
print()
print(bici1)
print()
print(auto2)
print()
print(moto2)
print()
print(camion2)
print()
print(bici2)
print()