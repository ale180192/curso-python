

# Definicion de una funcion
"""
Las funciones en python definen con la palabra clave
reservada def mas el nombre de la funcion.
* puede tener o no argumentos
* puede retornar o no un objeto
* el bloque de codigo de la funcion lleva una tabulacion.
* Parametros son los valores en la definicion de la funcion, en este caso son a y b
* los argumentos son los valores que pasamos en la invocacion de la funcion.
"""
def suma_numeros(a, b):
    print("inicio de la funcion")
    return a + b

# invocacion de una funcion
resultado = suma_numeros(7, 10)
print(f"el resultado de la suma es {resultado}")


# ejemplo de una funcion que suma todos los numeros de una lista
def sumar_elementos(lista_numeros):
    suma = 0
    for item in lista_numeros:
        suma += item

    return suma

mi_lista = [3, 5, 9, 28]
suma = sumar_elementos(mi_lista)
print(f"el resultado de sumar_elementos() es {suma}")

# invocacion de la funcion usando argumento por nombre.
# * Es mas legible el codigo
suma = sumar_elementos(lista_numeros=mi_lista)

# argumentos posicionales y por nombre
"""
Todos los argumentos posicionales deberan ir a la izquierda respetando la posicion
mientras que todos los argumentos por nombre deberan ir a la derecha sin importar la posicion.
"""
def imprimir_info_usuario(nombre, ciudad, calle):
    print(f"El usuario {nombre} vive en la calle {calle} y ciudad de {ciudad}")

# estamos cambiando el order de los argumentos por nombre(calle y ciudad)
imprimir_info_usuario("Maria", calle=4, ciudad="Queretaro")


##########################################################
# Valores por defecto en los parametros
"""
* Podemos definir parametro con valores por defecto en nuestras funciones.
* Todos los parametros que tengan un valor por defecto en la definicion se vuelven
en automatico como parametros opcionales en la invocacion.
* No counfundir parametros por defecto con los argumentos por nombre en la invocacion,
ya que podemos usar parametros por defecto y en la invocacion pasar los argumentos
de forma posicional.
"""
def total_despues_de_impuestos(monto, iva=15, aplicar_descuento=True):
    descuento_default = 20
    subtotal = monto - descuento_default if aplicar_descuento else monto
    subtotal = 0 if subtotal < 0 else subtotal # numeros negativos
    print(subtotal)
    iva = (subtotal * iva) / 100.0
    return subtotal + iva

total = total_despues_de_impuestos(100, iva=20, aplicar_descuento=True)
print(f"el total es: {total}")

# forma posicional
total = total_despues_de_impuestos(100, 20, False)
print(f"el total es: {total}")


##########################################################
# argumentos pasados por valor o por referencia
"""
Recapitulemos como funciona la asignacion en python( asignacion de variables, atributos de objetos y colecciones(listas/tuplas/diccionarios) )

* Si el objetivo de asignacion es un identificador(nombre de variable), entonces
    este nombre de variable es enlazado al objeto, y si el nombre ya esta enlazado a un objeto
    entonces es re-enlazado al nuevo objeto.

a = 5 # "a" referencia al objeto "5"
a = 7 # se crea el objeto "7 " y "a" ahora referencia al objeto "7"
b = a # b esta enlazado al mismo objeto "7" que a. tienen la misma direccion de memoria
b = 1 # creamos un nuevo objeto "1" y lo ligamos a b. Nunca se modifica la direccion a la que referencia.

* Si el objetivo de asignacion es un atributos de objeto,
    el objeto es el encargado de actualizar el atributo directamente,
    es decir, se actualiza el valor de la direccion de memoria.
    
user1 = User(nombre="Maria")
user2.nombre = "Juan" # aqui se actualiza directamente la memoria referenciada por user.nombre

user2 = user1 # los dos apuntan a la misma memoria(user1 y user2 son variables a fin de cuentas)
user2.nombre # Se acutualiza directamente la direccion de memoria, por lo tanto se actualiza user1 y user2

* para las colecciones se tiene el mismo concepto que para los atributos de objetos(siempre y cuando sean objetos mutables)

"""

# ejemplo asignacion variables
a = 5 
a = 7 
b = a 
b = 1
print(f"a: {a}, b: {b}")

# ejemplo asignacion atributos de objetos
class User:
    nombre = "ale"

user1 = User()
user1.nombre = "Maria"
user2 = user1
user2.nombre = "pedro"

print(user1.nombre, user2.nombre)

# ejemplo asignacion colecciones
lista_a = [1, 2, 3]
lista_b = lista_a
print(id(lista_a), id(lista_b))
lista_a.append(9)
lista_b.append(8)
print(lista_a)
print(lista_b)

"""
En python no existe el concepto pasar por valor o referencia.
    * los argumentos son pasados por asignacion.
    * cuando se pasa un argumento se crea una asignacion nueva dentro del alcance de la funcion,
        un alcance local. Ya vimos anteriormente como funciona la asignacion para variables, colecciones
        y para atributos de objetos.
    * Como resumen podemos hacer una analogia y decir que si pasamos un objeto/coleccione y modificamos sus
        atributos/elementos es como si fueran pasados por referencia, mientras que si pasamos las variables
        y las modificamos directamente(modificar el identificador) es como si fueran pasadas por valor
"""


# ejemplo de variables
def incrementar(valor):
    # se crea una asignacion con alcance local -> valor = <argumento recibido>
    valor += 1 # ya hemos visto que se creara un objeto "21" nuevo y se enlazara con valor
    return valor

var1 = 20
res = incrementar(var1)
print(f"var1: {var1}")



# ejemplo de atributos de objetos
class User:
    nombre = "Maria"

def update_nombre(user, nombre):
    # nombre = user -> asignacion varible
    user.nombre = nombre # ya hemos visto como funciona la asignacion de atributos

user = User()
update_nombre(user, "Pedro")
print(user.nombre)


# ejemplo de colecciones(listas)
def add_numeros(mi_lista, numeros):
    for item in numeros:
        mi_lista.append(item)

mi_lista = [1, 8, 4]
add_numeros(mi_lista, [11, 12, 13])
print(mi_lista)




# Recomendacion para manejar estos casos.
"""
* Retornar siempre el nuevo valor por la funcion y asignarlo a nuestra variable,
    asi no nos tenemos que preocupar si este fue modificado por referencia o por valor.
* Otros lenguajes tienen la necesidad de pasar por referencia ya que no pueden retornar
    mas de un parametro, con python se puede hacer muy facilmente
"""
def add_numeros(mi_lista, numeros):
    for item in numeros:
        mi_lista.append(item)

    success = True
    return mi_lista, success # return a list (li_lista, success)

mi_lista = [1, 8, 4]
mi_lista, success = add_numeros(mi_lista, [11, 12, 13])
print(mi_lista)