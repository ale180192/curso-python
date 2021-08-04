# ejercicios

# 1.- Definir una funcion que reciba como parametro una lista de strings de ciudades
#   y retorne la misma lista pero con los elementos en mayusculas.
# Nota: la lista de ciudades es que tu prefieras

ciudades = [ "Puebla", "Tijuana", "Queretaro",]
def upper_lista(ciudades):
    for ciudad in ciudades:
        # yield genera un "generator" que sera retornado en cada invocacion de la funcion
        yield ciudad.upper() 

ciudades = list(upper_lista(ciudades))
print(ciudades)

# 2.- Agregar las anotaciones de tipo a la funcion antes declarada.
from typing import Sequence, Tuple

def upper_lista(ciudades: Tuple[str, ...]) -> Sequence:
    for ciudad in ciudades:
        # yield genera un "generator" que sera retornado en cada invocacion de la funcion
        yield ciudad.upper() 


# 3.- deninir la siguiente lista -> nombres = ["maria", "juan", "pedro"]
#   Usando recursion, definir una funcion que imprima un mensaje de bienvenida
#   para cada uno de los nombres de la lista.
# Tip: El caso base es cuando tenemos una lista vacia(terminamos la recursion aqui) 
nombres = ["maria", "juan", "pedro"]
def mensaje_bienvenida(nombres):
    if len(nombres) == 0:
        return

    print(f"bienvenido {nombres[0]}")
    mensaje_bienvenida(nombres[1:])

mensaje_bienvenida(nombres)



# 4.- Definir la siguiente lista:
# dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
# Usar la funcion lambda y la funcion map() para truncar los elementos a los primeros
#   5 caracteres. Imprimir en consola el resultado
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dias_semana = list(
    map(lambda dia: dia[:5], dias_semana)
)
print(dias_semana)


# 5.- Usando la lista del ejercicio anterior.
#   Usar la funcion lambda y la funcion filter para "filtrar" todos los elementos
#   que contengan el caracter "a" en el elemento(dia de la semana).
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dias_semana = list(
    filter(lambda dia: "a" in dia, dias_semana)
)
print(dias_semana)

# 6.- Realizar el ejercicio 4 pero usar listas de comprension en lugar de lambdas.
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dias_semana = [dia[:5] for dia in dias_semana]
print(dias_semana)

# 7.- Realizar el ejercicio 5 pero usar listas de comprension en lugar de lambdas.
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dias_semana = [dia for dia in dias_semana if "a" in dia]
print(dias_semana)


# 8.- definir una funcion "suma(a, b)" que reciba dos parametros de tipo entero y retorne la suma
#   de estos dos numeros. Definir un decorador "@doble" para que la funcion retorne
#   el doble del resultado, es decir, suma(3, 5) debera retornar un valor de 16( (3+5)*2 )

def log(func):
    def wrapper(*args):
        res = func(*args)
        return res * 2

    return wrapper

@log
def suma(a, b):
    return a + b

print(suma(2, 4))
