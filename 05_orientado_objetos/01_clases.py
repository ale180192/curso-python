

# Clases en python
"""
Las clases nos proveen un medio para la construccion
de datos y funcionalidad en un mismo lugar. Creando nuevas
clases podemos crear nuevos tipos de datos.

- El mecanismo de clases de python agrega clases con un minimo
    de nueva sintaxis y semantica. Es muy facil la curva de aprendizaje
    por su minimalismo(Esto sin perder funcionalidad).

- Clases de python proveen todas las funcionalidades estandar de la
    programacion orientada a objetos(POO):

"""
class A():
    lista = []
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        

# definicion
class User:
    # variables de clase.
    pais = "México" # objeto inmutable(int, str, tuple, float)
    materias_inscritas = [] # objeto mutable(list, dict, y la mayoria de objetos declarados por nosotros inmutables)

    # constructor
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def _get_address(self):
        """
        El guion bajo indica que este metodo debe ser privado.
        Solo es un acuerdo pero aun asi el metodo sigue siendo 
        publico.
        """
        return f"full_address = {self.direccion}, {self.pais}"

    def get_info(self):
        full_address = self._get_address()
        return f"Nombre: {self.nombre}, direccion: {full_address}"

# instanciacion
user = User(nombre="Maria", direccion="Puebla")

# mandar llamar sus metodos.
print(user.get_info())

# acceder a sus atributos
print(user.nombre)
user.nombre = "Pedro"
print(user.nombre)

user2 = User("sdgf", "sdfg")
user2.pais = "brasil" # al ser inmutable se crea un nuevo objeto y user2.pais apunta al nuevo objeto "brasil"
print(user2.pais)
print(user.pais)

# ahora modificamos la variable de clase mutable(lista)
user2.materias_inscritas.append("Estructuras de datos")
user.materias_inscritas.append("POO")
print(user.materias_inscritas)
print(user2.materias_inscritas)

######################################
# Herencia
######################################

class Vehiculo:
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    def encender(self):
        print("Run run ...")


class Carro(Vehiculo):

    def __init__(self, modelo, puertas):
        super().__init__(modelo)
        self.puertas = puertas

    def reversa(self):
        print("Avanzando hacia atras ...")


bocho = Carro(modelo="Bocho", puertas=2)
bocho.encender()
bocho.reversa()

# podemos instanciar Vehiculo directamente
vehiculo = Vehiculo(modelo="vehiculo generico")
vehiculo.encender()

######################################
# metodos estaticos                  #
######################################

class User:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @classmethod
    def get_total_users(id):
        return 89


total_users = User.get_total_users()
print(total_users)

######################################
# metodos megicos                    #
######################################
"""
Los métodos mágicos de las clases Python son aquellos que comienzan y terminan con dos caracteres subrayados.

- Al ser sobrecargados en las clases modifican cierto comportamiento de estos objetos

- El metodo magico mas usado es el metodo __init__

- Todos reciben como primer parametro una referencia al mismo objeto

"""

class User:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __iter__(self):
        for c in self.name:
            yield c

user = User("Maria")
print(user)
print(len(user))
print(user["name"])
user["direccion"] = "queretaro"
print(user.direccion)

for c in user:
    print(c)


######################################
# Clases Abstractas                  #
######################################
from abc import ABC, abstractclassmethod
import abc
class Vehiculo(ABC):
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    @abstractclassmethod
    def encender(self):
        print("Run run ...")


class Carro(Vehiculo):

    def __init__(self, modelo, puertas):
        super().__init__(modelo)
        self.puertas = puertas

    def reversa(self):
        print("Avanzando hacia atras ...")

# NO podemos instanciar Vehiculo directamente
vehiculo = Vehiculo(modelo="vehiculo generico")

bocho = Carro(modelo="Bocho", puertas=2)
bocho.encender()
bocho.reversa()
