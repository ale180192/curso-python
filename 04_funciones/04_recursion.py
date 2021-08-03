
# funciones recursivas
"""
Definimos una funcion recursiva como una funcion
que se llama asi misma por un numero finito de veces,
debemos garantizar que exista una condicion que rompa el bucle
infinito de recursion.

* La tecnica divide y venceras se apoya en la recursion para
    solucionar problemos complejos, dividiendo estos en problemas
    mas pequeños que pueden ser resueltos de forma mas facil.

* Una forma de abordar el problema es dividiendo el problema original
    en problemas identicos de forma recursiva, esto es hasta llegar
    a un problema que podemos resolver de forma trivial, este problema
    es llamado caso base. cuando lleguemos al caso base debemos romper
    la recursion.
"""

# ejemplo de la serie de fibonnaci
"""
La sucesión comienza con los números 0 y 1,
A partir de estos, «cada término es la suma de los dos anteriores»
ejemplo de la serie: 0, 1, 1, 2, 3, 5, 8, 13, 21


para encontrar el n-esimo numero de la seri de fibonacci tenemos la
siguiente formula:
f(n) = f(n-1) + f(n-2)

es decir para encontrar el n-esimo valor tenemos que conocer los dos numeros
anteriores, y estos a la vez tienen que conocer sus dos numeros anteriores
volviendose un problema de recuersion hasta que llegamos al caso base
donde n < 2 regresar n -> (para n=1 es 1)
"""

# Encontrar el numero
def fib(n):
    print(f"llamada para n={n}")
    if n < 2:
        return n

    # return fib(n - 1) + fib(n - 2)
    n1 = fib(n - 1)
    n2 = fib(n - 2)
    print(f"numero fibonacci n-esimo {n} es: {n1 + n2}")
    return n1 + n2

res = fib(10)
print(res)

"""
Notas: para numeros grandes es realmente grande el costo computacional usando esta tecnica.
para f(n=50) se requieren realizar 20.365.011.073 sumas. No siempre la recursion sera la mejor
tecnica
"""

def fib_sin_recursion(n):
    f_list = [1, 2]
    if n < 2:
        return n

    for idx in range(2, n - 1):
        print("idx", idx)
        f_list.append(f_list[idx - 1] + f_list[idx - 2])

    return f_list[idx]

print(f"Resultado sin recursion: {fib_sin_recursion(100)}")

# comparasion de tiempos:
import time
sec_start = time.localtime().tm_sec
print(fib(22))
print(f"segundos: {time.localtime().tm_sec - sec_start}")

#################
sec_start = time.localtime().tm_sec
print(fib_sin_recursion(22))
print(f"segundos: {time.localtime().tm_sec - sec_start}")

