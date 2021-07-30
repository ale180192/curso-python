
#instruccion del
"""
Recordemos que en python todo son objetos(incluso los tipos primitivos int, str, etc):
* Las variables son referencias a esos objetos, no almacenan el valor asignado.
    unicamente hacen referencia al objeto como tal.
* La instruccion "del" elimina la referencia entre la variable y el objeto,
es decir si no existe otra variable que haga referencia a ese objeto,
el recolector de python liberara esa memoria asignada.
"""
mi_var = 5 # se crea un objeto "5" en la memoria y tmb una variable mi_var que apunta a ese objeto
otra_variable = mi_var # ahora existen dos referencias al objeto "5"
print(id(mi_var), id(otra_variable)) # vemos que apuntan al mismo objeto
otra_variable = 4 # se crea otro objeto "4" y otra_variable apunta a ese nuevo objeto
print(id(mi_var), id(otra_variable)) # vemos que apuntan al mismo objeto
# ahora de nuevo crea un nuevo objeto "10" y mi_var tiene una referencia a ese objeto
# que paso con el objeto "5" que creamos al inicio? bien ya no tiene ninguna
# referencia asi que el recolector de basura de python liberara esa memoria
mi_var = 10

print(mi_var)
del mi_var
# print(mi_var) # exception

midict = {"key1": "val1", "key2": "val2"}
del midict["key1"]
print(midict)

# del en listas
mi_lista = ["uno", "dos", "tres", "cuatro"]
del mi_lista[0]
print(mi_lista)
del mi_lista[:2]
print(mi_lista)