

"""
Definicion:
 - Python lambdas son pequeñas funciones anonimas que estan sujetas a una mas
    restrictiva pero mas consisa sintaxy que las funciones regulares de python

Sintaxis:
    - Unicamente pueden contener expresiones y no pueden incluir
        sentencias en su cuerpo.

        NO: return, pass, assert, raise, mivar=5, print("mensaje")
        SI: 1 + 1, a == True, a is None, a != b
    
    - Esta escrita como una sola linea de ejecucion.
    - No soporta anotaciones de tipo.
    - Puede ser inmediatamente ser invocada.

        (lambda x: x * x)(3)

Contras de lambdas:

    - Principalmente los problemas de legibilidad.
    - Posibilidad de abusar de su uso.


Recomendaciones respecto al uso de lambdas:
    - Usarlas en casos bien especificos, por ejemplo
        junto con las funciones de alto nivel, map() y filter()
    
    - Preferir siempre que se pueda las funciones clasicas de python
        en lugar de las funciones lambdas.
"""

# ejemplo de una funcion lambda.
my_func = lambda x, y: x + y
res = my_func(3, y=4)
print(res)

# puede ser invocada inmediatamente.
res = (lambda x, y: x + y)(x=3, y=5)
print(res)


# Funciones integradas de alto nivel que toman las ventajas
# de las lambdas.

# funcion map(). Usamos la funcion integrada map() cuando
# queremos aplicar la misma operacion a todos los elementos
# de nuestras estructuras iterables(listas, tuplas, diccionarios)

nombres = ["maria", "juan", "pedro"]

nombres_cap = list( # convertimos a lista ya que se regresa un iterador.
    map(lambda item: item.capitalize(), nombres)
)
print(nombres_cap)

# ejemplo con diccionario. Podemos observar que no es legible.
nombres = {"key1": "val1", "key2": "val2"}
nombres_cap = dict( # convertimos a dict ya que se regresa un iterador.
    map(
        lambda item: ( item[0], item[1].capitalize() ),
        nombres.items()
    )
)
print(nombres_cap)


# funcion integrada filter. Esta funcion agrega al iterador/lista generado
# todos los elementos que en la expresion evaluada sean True
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
numeros_pares = list(
    filter(lambda numero: (numero % 2) == 0, numeros)
    )
print(numeros_pares)


# Alternativas a las funciones lambda
"""
Para muchos casos practicos podemos remplazar la funcion lambda
con la funcionalidad "comprension de listas", esta es una sintaxis
que nos permite crear listas a partir de otras listas, tuplas o cualquier
objeto iterable.

* la unica diferencia es que para listas muy grandes y la memoria es un problema
    la comprension de listas nos generara una lista con todos los valores
    mientras que las funciones map(), filter() y parecidas nos generaran un iterable
    que unicamente cuando iteremos cada elemento este se cargara en memoria.

"""
# creemos una lista por comprension
numeros = [numero for numero in range(0, 11)]
print(numeros)

# aplicamos capitalize a todos los elementos de nuestra lista.
# Sustituimos la funcion map()
nombres = ["maria", "juan", "pedro"]
nombres_cap = [nombre.capitalize() for nombre in nombres]
print(nombres_cap)

# una lista con numeros pares. sustituimos a la funcion filter
numeros_pares = [
    numero for numero in range(0, 11) if (numero % 2) == 0
]
numeros_pares_fill_none = [
    numero if (numero % 2) == 0 else None for numero in range(0, 11) 
]
print(numeros_pares_fill_none)
print(numeros_pares)


"""
Conclusiones:
El PEP 8 de python nos dice lo siguiente sobre las funciones lambdas:
 - Siempre use una sentencia "def" en lugar de una sentencia de asignacion
    que liga una expresion lambda directamente a un identificador.

    def my_func(x):  -------> SI
        return x

    my_func = lambda x: x -----> NO

Limitar el uso de funciones lambda y solo hacer uso de ellas con las funciones
integradas de mas alto nivel como map(), filter() o similares.
"""

