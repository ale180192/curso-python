# parametros indeterminados "args" y "kwargs"
"""
Los parametros indeterminados nos permiten decir explicitamente
en la definicion de una funcion que esta puede recibir una cantidad
indefinida ya se de parametros posicionales(args) o de parametros por
nombre(kwargs -> key-word-args)

Nota: args y kwargs son solo nombres por convenencia, se puede usar cualquier
nombre que nosotros queramos.
"""
# ejemplo args
def sumar_elementos(*args):
    suma = 0
    for arg in args:
        suma += arg

    return suma

print(sumar_elementos(2, 3, 5))
print(sumar_elementos(2, 3, 5, 8, 9))

# descomprimir estructuras. 
"""
con el operador "*" indicamos que se debe descomprimir la lista/tupla y
pasar los elementos como parametros posicionales. NO se pasa un solo argumento(la lista),
se pasan todos los elementos de la lista como argumentos.
"""
mis_numeros = [3, 4, 5]
res = sumar_elementos(*mis_numeros)
print(res)


# ejemplo kwargs
def imprimir_info(**kwargs):
    if kwargs.get("nombre"):
        print(f"Nombre: {kwargs['nombre']}")

    if kwargs.get("direccion"):
        print(f"Direccion: {kwargs['direccion']}")
imprimir_info(nombre="Juan", direccion="queretaro")
imprimir_info(direccion="queretaro")

# descomprimir estructura para un diccionario.
"""
En este caso usamos doble astedisco "**" y el diccionario
se descomprime en argumentos por nombre(key-value).
"""
info = {"nombre": "Maria", "direccion": "CDMX"}
imprimir_info(**info)


#####################################################
# decoradores. 
#####################################################
"""
Es un patron que nos permite agregar funcionalidad extra a nuestras
funciones en python.
"""
# ejemplo. 
# * log es una funcion que recibe un objeto callable(invocable), este objeto
#       es una funcion. las funciones tambien son objetos en python.
# * esta funcion retorna un objeto invocable(funcion)
def log(func):
    def wrapper(*args):
        print("call to func")
        return func(*args)

    return wrapper

# funcion normal
def suma(a, b):
    return a + b

# invocamos nuestra funcion log, que recibe una funcion
# y retorna una funcion
suma_con_log = log(suma)
print(suma_con_log(3, 5))

# sintaxis preferida es usar "@" para aplicar los
# decoradores. Es mas legible y la funcion que aplica
# la funcionalidad extra esta en la misma definicion.

@log
def suma(a, b):
    return a + b

print(suma(2,3))
