


# ejercicio numero 1
"""
crear una variable donde deberas asignar tu fecha de nacimiento como entero
declarar otra variable con tu nombre
en una tercera variable concatenar las dos variables anteriores e imprimir el resultado en consola utilizando interpolacion.
el mensaje debe tener el siguiente formato: mi nombre es <aqui tu nombre> y mi fecha de nacimiento es el año <aqui tu fecha de nacimiento>
"""
fecha_nacimiento = 1992
nombre = "Ale"
mensaje = f"mi nombre es {nombre} y mi fecha de nacimiento es el año {fecha_nacimiento}"
print(mensaje)



# ejercicio numero 2
"""
definir en una variable de tipo entero tu mes de nacimiento
tomando el mes actual como referencia imprimir en pantalla si ya cumpliste años en este año(2021)
el mensaje debe tener el siguiente formato: Este anio ya cumpli anios? True|False
"""
mes_nacimiento = 1
mes_actual = 7
ya_cumpli_anios = mes_nacimiento < mes_actual 
print(f"Este año ya cumpli años? {ya_cumpli_anios}")


# ejercicio numero 3
"""
definir una variable tipo boleana donde se indique si te gustan los gatos
definir una variable donde indique si te gustan los perros
definir una tercer variable donde se almacene el valor booleano de si te gustan los gatos y tambien los perros.
imprimir en consola un mensaje con el siguiente formato:
Es verdad que me gustan los gatos y los perros? <aqui el valor de tu tercer variable>
"""
amo_los_gatos = False
amo_los_perros = True
love_gatos_y_perros = amo_los_gatos and amo_los_perros
print(f"Es verdad que me gustan los gatos y los perros? {love_gatos_y_perros}")

# ejercicio numero 4
"""
usando el metodo input, metodo print y el operador de pertenencio "in"
hacer el codigo para que se pida ingresar el nombre y tu mes de 
cumpleaños(recuerda que este valor se recibe como string, tendras que hacer casting a int)
definir una lista llamada "primeros_seis_meses_anio"  con los siguientes elementos: 1, 2, 3 , 4, 5, 6
imprimir en consola un mensaje con el siguiente formato:
Hola mi nombre es <aqui tu nombre>. Cumplo años en los primeros seis meses del año? <valor booleano aqui>
"""
nombre = input("Cual es tu nombre? ")
mes = input("Cual es tu mes de nacimiento? ")
mes = int(mes)
primeros_seis_meses_anio = [1, 2, 3, 4, 5, 6]
cumplo_anios_en_los_primeros_seis_meses = mes in primeros_seis_meses_anio
mensaje = f"Hola mi nombre es {nombre}. Cumplo años en los primeros seis meses del año? {cumplo_anios_en_los_primeros_seis_meses}"
print(mensaje)

# ejercicio 5
"""
hacer lo mismo que el ejercicio 4 pero usar un diccionario llamado "mi_info" para almacenar
las entradas(nombre, mes de nacimiento).
"""
mi_info = {}
mi_info["nombre"] = input("Cual es tu nombre? ")
mi_info["mes"] = int(input("Cual es tu mes de nacimiento? "))
primeros_seis_meses_anio = [1, 2, 3, 4, 5, 6]
cumplo_anios_en_los_primeros_seis_meses = mi_info["mes"] in primeros_seis_meses_anio
mensaje = f"Hola mi nombre es {mi_info['nombre']}. Cumplo años en los primeros seis meses del año? {cumplo_anios_en_los_primeros_seis_meses}"
print(mensaje)