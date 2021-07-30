

# definicion de una variable y asignacion.
"""
* las variables se definen sin definir un tipo de dato.
* las varialbles se pueden reasignar con un tipo de dato totalmente diferente.
"""
nombre = "Pedro"
print("Nombre original: ", nombre)
nombre = "Juan"
print("Nuevo nombre: ", nombre)
nombre = 2021

# tipos de datos.
"""
* todo en python son objectos, incluso los tipos primitivos.
* usamos la funcion type para obtener el tipo de dato
"""

# string
nombre = "Ale"
print("la variable nombre es de tipo:", type(nombre))
print("Su valor es: ", nombre)
print()

# int
numero_dias = 3
print("la variable costo es de tipo:", type(numero_dias))
print("Su valor es: ", numero_dias)
print()

# float
paridad_dolar_peso = 22.234
print("la variable paridad_dolar_peso es de tipo:", type(paridad_dolar_peso))
print("Su valor es: ", paridad_dolar_peso)
print()

# booleano
es_lunes = False # True
print(f"la variable es_lunes es de tipo: {es_lunes}")
print(f"su valor es: {es_lunes}")

# lista
"""
Es una estructura mutable.
"""
dias_de_la_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print("la variable dias_de_la_semana es de tipo:", type(dias_de_la_semana))
print("Su valor es: ", dias_de_la_semana)
print("Su primer elemento es: ", dias_de_la_semana[0])
dias_de_la_semana[0] = "LUNES"
print("Su nuevo valor del primer elemento es: ", dias_de_la_semana[0])
print()

# tupla
"""
Es una estructura inmutable.
"""
dias_de_la_semana = ("lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
print("la variable dias_de_la_semana es de tipo:", type(dias_de_la_semana))
print("Su valor es: ", dias_de_la_semana)
print("Su primer elemento es: ", dias_de_la_semana[0])
print()
# dias_de_la_semana[0] = "LUNES"

# diccionario
"""
elementos clave-valor
"""
contacto_informacion = {"nombre": "Juan", "telefono": 5542876523}
print("la variable contacto_informacion es de tipo:", type(contacto_informacion))
print("Su valor es: ", contacto_informacion)
print("El nombre del contacto es: ", contacto_informacion["nombre"])
contacto_informacion["telefono"] = 1111111111
print("El nuevo numero del contacto es: ", contacto_informacion["telefono"])
contacto_informacion["email"] = "pedro@email.com"
print("El email es: ", contacto_informacion["email"])
print()

# operaciones con cadenas
primer_nombre = "Juan"
segundo_nombre = "Perez"
email = "juan@email.com"
nombre_completo = primer_nombre + " " + segundo_nombre # concatenacion
info_contacto = f"Nombre: {nombre_completo}, email: {email}" # interpolacion
print("informacion de contacto: ", info_contacto)
print(f"Informacion en minusculas: {info_contacto.lower()}")
print(f"Informacion en mayusculas: {info_contacto.upper()}")
"""
accesos a los indices de las listas/cadenas
indice 0 para primer elemento
para seleccionar rango el primer indice indica el inicio, incluyendolo
el segundo indice indica el final, no incluyendolo
"""
print(f"primeros 10 caracteres: {info_contacto[:10]}")
print(f"Rango de caracteres: {info_contacto[8:12]}") # intervalo -> [start, end)
print(f"Ultimos 10 caracteres: {info_contacto[-10:]}")
total_caracteres = len(info_contacto)
print(f"Total de caracteres: {total_caracteres}")




