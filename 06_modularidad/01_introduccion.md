# Modularidad
La programación modular se refiere al proceso de dividir una tarea de programación grande y difícil de manejar en subtareas o módulos separados, más pequeños y más manejables. Luego, los módulos individuales se pueden unir como bloques de construcción para crear una aplicación más grande.

### Ventajas de modularizar una aplicacion grande

* Simplicidad: En lugar de preocuparnos de todo el problema en cuestion, podemos hacer pequeños modulos que resuelvan problemas especificos.

* Mantenibilidad: Si separamos estos pequeños modulos en dominios bien definidos y delimitados, logramos tener una interdependencia minima, lo que nos garantiza que modificar un modulo afectara en lo mas minimo en otras zonas de nuestro codigo. Logramos tener un minimo acoplamiento.

* Reusabilidad: Podemos reutilizar estas funcionalidades especificas asi logrando tener codigo duplicado o evitando reinventar la rueda. Usar paquetes de terceros es una manera rapida y eficiente de crear nuestro producto.

* Espacios de nombres: Tener espacios de nombres es una buena idea para evitar tener colisiones entre identificadores. el zen de pytho dice lo siguiente: "Los espacios de nombres son una gran idea, hagamos mas de ellos!"


### Modulos de python
Un módulo es un objeto de Python con atributos nombrados arbitrariamente que tu puedes enlazar y hacer referencia. Definir un modulo en python es extremadamente sencillo, basta con crear un archivo con extension .py y listo, tenemos nuestro modulo.

#### Nuesto modulo puede contener lo siguiente:

* clases
* funciones
* varialbles
* codigo ejecutable

Veamos un ejemplo.

\# carrito_compra.py 
```python
IVA_MEX = 15
IVA_BRA = 10

class CarritoCompra:
    
    def __init__(self):
        pass

def validar_carrito_compra(carrito: CarritoCompra):
    pass

```

### Sentencia import
Con la sentencia import podemos utilizar nuestro modulo carrito_compra.py en cualquier otro archivo de codigo python(otro modulo)

```python
# sintaxis
import module1[, module2[,... moduleN]

# nuestro ejemplo particular
import carrito_compra
```

Lo que hace el interprete de python al encontrarse con la sentencia import es buscar este modulo en una lista de directorios, especificamente en el siguiente orden:

* El directorio desde donde se ejecuto el script de entada o el actual directorio si el programa se esta ejecutando interactivamente.

* En la lista de directorios definidos por la varialbe de entorno PYTHONPATH, esta variable es dependiente del sistema operativo pero deberia imitar la variable de entorno
PATH(la cual nos dice donde estan nuestro ejecutables en el OS)

* Una serie de directorios definidos en la instalacion de nuestro interprete python.

La ruta de busqueda resultante es accesible en la variable de python sys.path, la cual es obtenida del modulo sys.

```python
import sys
sys.path
```


### Hacer visible nuestro modulo python para que pueda ser importado correctamente
Para lograr que nuestro modulo de python pueda ser importado correctamente tenemos estas opciones:

* Poner nuestro modulo en el mismo directorio de  donde estamos ejectuando nuestro script de entrada.
* Agregar en tiempo de ejecucion el directorio de nuestro modulo. esto agregando este directorio a la variable path. Esta tecnica es utilizada por la mayoria de frameworks ya que permite que nosotros podamos instalar nuestro codigo en cualquier directorio y en tiempo de ejecucion agregar el directorio raiz.

```python
import sys, os

PATH_ENTRYPOINT_FILE = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(PATH_ENTRYPOINT_FILE)
sys.path.append(BASE_DIR)
print(sys.path)
```