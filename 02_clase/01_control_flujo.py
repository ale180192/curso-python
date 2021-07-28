"""
sentencia if
"""
if 30 > 20:
    print("30 es mayor a 20")

mes_nacimiento = 1
mes_actual = 7
if mes_nacimiento > mes_actual:
    print("este año ya cumpli años :) ")


"""
sentencia if else
"""
mes_nacimiento = 1
mes_actual = 7
if mes_nacimiento > mes_actual:
    print("este mes ya cumpli años :) ")

else: # es opcional esta sentencia.
    print("este año aun no cumplo años :c ")


meses = ["enero", "febrero", "noviembre", "diciembre"]
mes_nacimiento = "enero"
if mes_nacimiento in meses:
    print("Mi mes de nacimiento se encuentra en la lista")
else:
    print("Mi mes de nacimiento no se encuentra en la lista")


"""
Sentencia if-elif-else .... switch
"""
mes_nacimiento = "Marzo"
if mes_nacimiento == "Enero":
    print("mi mes de nacimiento es Marzo.")
elif mes_nacimiento == "Febrero":
    print("mi mes de nacimiento es Febrero.")
elif mes_nacimiento == "Marzo":
    print("mi mes de nacimiento es Marzo")
else: 
    print("mi mes de nacimiento no es Enero, Febrero ni Marzo.")

"""
sentencias if else anidadas
"""
mes_nacimiento = 1
dia_nacimiento = 18
if mes_nacimiento == 1:
    print("tu mes de nacimiento es Enero.")
    if dia_nacimiento <= 15:
        print("cumples años los primero 15 dias del mes.")
    else:
        print("Cumples años los ultimos dias del mes.")
else:
    print("No cumples años en Enero")

"""
Operador terniario
"""
dia_actual = "Lunes"
es_lunes_hoy = True if dia_actual == "Lunes" else False
mensaje = "Hoy es lunes" if es_lunes_hoy else "Hoy no es Lunes"
print(mensaje)


"""
valor None
"""
mi_lista = []
if None:
    print("None es evaluado como True")
else:
    print("None es evaluado como False")

if mi_lista is None:
    print("la lista esta vacia")

if not mi_lista:
    print("lista vacia")


"""
acceso seguro a keys de un dict
"""
contacto = {
    "nombre": "Juan",
    "direccion": {
        "calle": "av. chapultepec.",
        "colonia": "Chapultepec primera seccion"
    }
}
print(f"La colonia es: {contacto['direccion']['colonia']}")
contacto = {
    "nombre": "Juan",
    "direccion": None
}
colonia = contacto["direccion"]["colonia"] if contacto["direccion"] else "Colonia desconocida."
print(f"La colonia es: {colonia}")
