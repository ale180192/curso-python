

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


