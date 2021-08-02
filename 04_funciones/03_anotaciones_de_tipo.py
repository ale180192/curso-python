# Anotaciones de tipo
"""
Las anotaciones de tipo nos permiten especificar el tipo de dato
de los parametros de las funciones, asi como el tipo de dato de retorno.

Es totalmente y opcional y nos da las siguientes ventajas:

* Este tipado que agregamos puede ser utilizado por herramientas de terceros
    como IDEs, linters, checadores de tipo, etc

* En una manera de autodocumentar nuestras funciones, con lo cual
    podemos tener un codigo mas legible.

Para esto tenemos el paquete "typing"
"""
from typing import (
    Tuple,
    List,
    Optional,
    Dict,
)

# tipado, estructura basica
# python no hace ninguna validacion de que los argumentos
# que se pasen a la funcion sean del tipo especificado con
# las anotaciones de tipo. Esto probablemente te lo diga tu IDE
# mientras escribes tu codigo.
def sumar_numeros(a: int, b: int) -> int:
    return a + b


# Anotaciones para colecciones(listas/tuplas)
# Los 3 puntos indican que todos los elementos son de tipo int.
def sumar_lista(lista_numeros: Tuple[int, ...]) -> int:
    suma = 0
    for item in lista_numeros:
        suma += item

    return suma


class User:
    name = "default"

# Optional
# Optional indica que se puede regresar el parametro indicado o None en lugar
def get_user_info(
    id: int
) -> Tuple[bool, Optional[User]]:
    # return True, User()
    return True, None
