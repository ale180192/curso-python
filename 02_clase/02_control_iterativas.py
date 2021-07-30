# while loop
"""
while <expr>:
    <statement(s)>

"""
n = 5
while n < 0:
    print(n)
    n -= 1


# iterando lista/tupla con while(no es la mejor opcion pero se puede hacer)
dias_semana = ["lunes", "martes", "miercoles", "jueves"]
contador = 0
while contador < len(dias_semana):
    print(dias_semana[contador])
    contador += 1

# break y continue para alterar la iteracion de bucle
"""
break: con break terminamos completamente el bucle
y el programa continua en la primer sentencia siguiente al
bloque del cuerpo del bucle(una tabulacion hacia atras).

continue: Con continue la actual iteracion es terminada e imediatamente
saltamos al inicio de del bucle re evaluando la condicion.

Nota: estas sentencias aplican tanto para los bucles while como for
"""
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        print("n es 5, terminamos el bucle")
        break

print("aqui continua el flujo del programa.")

# continue. vamos a imprimir unicamente los numeros pares.
n = 13
while n > 0:
    print("###############################")
    n -= 1
    print(f"evaluando el numero: {n}")
    if (n % 2) == 0:
        print(f"{n} es numero par ... continue")
        continue
    
    print("esto solo se mostrara para numero impares.")


######################################################
# bucle for
"""
for <actual elemento> in <nombre de la estructura a iterar>:
    <statement(s)>
"""
# vamos a iterar una lista/tupla
lenguajes_programacion = ["python", "java", "c++", "c#", "php", "go", "c"]
for lenguaje in lenguajes_programacion:
    print(lenguaje)


# vamos a iterar un diccionario.
info_usuarios = {"Maria": {"edad": 18}, "Juan": {"edad": 13}}
for key, value in info_usuarios.items():
    print(f"{key} tiene {value['edad']} años")


# vamos a iterar un rango especifico
"""
range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3.
"""
for i in range(1, 10):
    print(i)


# podemos observar como podemos crear estructuras de datos complejas.
lenguajes = {
    "python": {
        "usos": ["web", "aplicaciones escritorio", "ciencia de datos"],
        "tipado_dinamico": True
    },
    "java": {
        "usos": ["web", "aplicaciones escritorio", "aplicaciones android"],
        "tipado_dinamico": False
    },
    "c++": {
        "usos": ["aplicaciones de alto rendimiento", "web", "aplicaciones escritorio"],
        "tipado_dinamico": False
    }
}
for key, value in lenguajes.items():
    tipado_mensaje = "tipado dinamico" if value['tipado_dinamico'] else 'tipado estatico'
    msg = f"El lenguaje de programacion {key} " \
        f"es un lenguaje de programacion de {tipado_mensaje} " \
        f"el cual tiene los siguientes usos: {value['usos']}"
    print(msg)
    print()


# mas sobre tuplas
numeros_impares = []
for numero in range(11):
    if not (numero % 2) == 0:
        numeros_impares.append(numero)

print(f"los numero impares son: {numeros_impares}")
# metodo count en tuplas. cuantos elementos existen en la lista
numeros_impares.append(3)
numeros_impares.append(3)
numero_repeticiones = numeros_impares.count(3)
print(f"el numero 3 se repite {numero_repeticiones} veces")

# metodo index. retorna el indice del argumento, el primero en encontrar
index = numeros_impares.index(5)
print(f"el numero 5 tiene el index {index}")

# metodo pop. Remove and return item at index (default last).
val = numeros_impares.pop()
print(f"el ultimo elemento es el {val}")
print(f"numeros impares: {numeros_impares}")


## mismas operaciones con diccionarios
# update. agrega o actualiza una key en el diccionario 
midict = {"key1": "val1", "key2": "val2"}
print(midict)
midict.update({"key3": "val3"})
print(midict)
# pop. retorna y elimina la key especificada
# val = midict.pop("key1")
val = midict["key1"]
print(midict)
print(val)

# acceso seguro a diccionarios
midict = {"key1": "val1", "key2": "val2"}
key1 = midict.get("key1")
print(key1)
key3 = midict.get("key3")
print(key3)

# acesso seguro a diccionarios anidados
user = {
    "name": "Maria",
    "direccion": {
        "ciudad": "queretaro"
    }
}
ciudad = user["direccion"]["ciudad"]
print(ciudad)
# raise exception
user = {
    "name": "Maria",
    "direccion": None
}
# ciudad = user["direccion"]["ciudad"]

# forma segura cuando el key no existe o es None
ciudad = "CDMX"
if user.get("direccion") and user.get("direccion").get("ciudad"):
    ciudad = user.get("direccion").get("ciudad")
print(f"ciudad metodo largo: {ciudad}")

# forma corta
ciudad = user.get("direccion").get("ciudad") \
    if user.get("direccion") and user.get("direccion").get("ciudad") else "CDMX"
print("forma corta ciudad: ", ciudad)