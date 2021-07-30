# Usando la sentencia "if-else" realizar lo siguiente:
"""
declarar una varialbe "nombre" donde debes poner tu nombre.
imprimir en terminal si tu nombre tiene mas de 5 caracteres o no.
"""


# Usando la sentencia "if-elif-else" realizar lo siguiente:
"""
Declarar una variable "nombre" donde debes asinar tu nombre.
imprimir en terminal si tu nombre tiene entre 1 y 3 caracteres
o entre 3 y 5 caracteres o mas de 5 caracteres.
"""

# Usando el operador terneario realizar lo siguiente:
"""
* definir la siguiente lista: mi_lista = [1, 3, 5]
* asignar a una variable el mensaje:
    "mi lista tiene 3 o menos elementos" si mi lista tiene 3 o menos elementos
    o por lo contrario asignar el mensaje: "mi lista tiene mas de 3 elementos"
    si "mi_lista" tiene mas de 3 elementos.
* imprimir en terminal el mensaje
"""

# Usando el bucle "while" realizar lo siguiente:
"""
Declarar la siguiente lista: lenguajes = ["c++", "java", "python", "sql", "javascript"]
iterar la lista e imprimir unicamente el elemento "python" con un mensaje que diga;
"hemos encontrado el elemento python :) " e inmediatamente terminar el bucle while
"""

# Usando el bucle "for" realizar lo siguiente:
"""
Declarar la siguiente lista: mi_lista = ["google", "facebook", "microsoft", "apple", "spacex"]
iterar toda la lista e imprimir cada elemento
"""

# Usando el bucle "for" realizar lo siguiente:
"""
Declarar las siguientes listas:
companias_tech = ["google", "facebook", "microsoft", "apple", "spacex", "twitter", "neuralink"]
nombres_cortos = []
nombres_largos = []
agregar todos los elementos de la lista "companias_tech" que tengan menor a 6 caracteres a la lista nombres_cortos
mientras que los que tengan 6 o mas caracteres deberan ser agregados a la lista nombres_largos.
Imprimir en terminal cuantos elementos tiene cada lista.
"""
companias_tech = ["google", "facebook", "microsoft", "apple", "spacex", "twitter", "neuralink"]
nombres_cortos = []
nombres_largos = []
for compania in companias_tech:
    if len(compania) < 7:
        nombres_cortos.append(compania)
    else:
        nombres_largos.append(compania)
print(nombres_largos)
print(nombres_cortos)

# Usando el bucle "for" realizar lo siguiente:
"""
declarar el siguiente diccionario: 
info_usuario = {"nombre": "Maria", "email": "maria@email.com", "edad": 42}
* iterar el diccionario e imprimir en terminal tanto la key como el valor de
cada elemento del diccionario
"""

# Usando el bucle "for" y la funcion "range()" realizar lo siguiente:
"""
imprimir en terminal los numeros del 10 al 15
"""


##############################################################################
# Ejercicios mas complejos
##############################################################################

# Definir una lista con 3 usuarios donde cada usuario sera un diccionario el cual
# tendra la siguiente informacion: nombre, email, edad
# imprimir en terminal la informacion de cada usuario con el siguiente formato:
# "El usuario <nombre de usuario> tiene el email <email aqui> y tiene <aqui su edad> años"



"""
De la lista de usuarios anterior, debemos hacer lo siguiente:
* Agregar a todos los usuarios una nueva key "longitud_nombre"
donde almacenaremos el numero de caracteres de su nombre.
* hacer una validacion donde "si longitud_nombre es mayor a 5 caracteres"
    tenemos que eliminar la key "email" del usuario
* imprimir en terminal la lista con los cambios que acabamos de hacer -> print(mi_lista)
* iterar la lista que acabamos de actualizar y agregar una nueva key "tiene_email", debera
ser True si el usuario tiene la key "email" y False de lo contrario
* imprimir de nuevo toda la lista -> print(mi_lista)
"""
usuarios = [
    {"nombre": "Maria", "email": "maria@gmail.com", "edad": 55},
    {"nombre": "Juan", "email": "juan@gmail.com", "edad": 17},
    {"nombre": "Alberto", "email": "alberto@gmail.com", "edad": 55},
]
for user in usuarios:
    user["longitud_nombre"] = len(user["nombre"])
    if user["longitud_nombre"] > 5:
        del user["email"]
print(usuarios)
for user in usuarios:
    user["tiene_email"] = True
    if not user.get("email"):
        user["tiene_email"] = False
print(usuarios)