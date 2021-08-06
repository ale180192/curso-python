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

Una ves que nuestro modulo ha sido importado podemos haceder a cada una de sus clases, variables o funciones mediante la notacion de punto. El modulo importado es un espacion de nombres y para acceder a todos sus elementos tenemos que usar la notacion punto. por ejemplo carrito_compra.CarritoCompra


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

#### Ejemplo

**Para este ejemplo hemos declarado nuestro modulo carrito_compra.py, tambien tenemos nuestro script de entrada entrypoint.py. vamos a ejecutarlo .....**

<br>
<br>

### Sentencia from \<module> import \<objeto1>, \<objeto2>, ...., \<objetoN>

Esta sentencia es una alternativa a import la cual nos da la flexibilida de importar directamente los objetos del modulo. Con esta sentencia podemos referenciar directamente los objetos sin nesecidad de usar la notacion punto.
Estos objetos pueden ser desde variables hasta modulos, veremos mas adelante que un paquete contiene modulos.


```python
# importando objetos de un modulo
from <module_name> import <object (s)>

# importando modulos de un paquete
from <paquete> import <modulo1>, <modulo2>, ..., <moduloN>

#Podemos indicar un alias a nuestro import.
from <paquete> import <modulo1> as mi_alias
```

#### Ejemplo:
**Veamos este concepto en nuestro ejemplo ...**

<br>
<br>


### La variable \__name__

Cuando un modulo es ejecutado directamente como punto de entrada, se ejecutaran todas las sentencias del modulo, lo mismo pasara cuando el modulo sea importado. Si queremos distinguir cuando nuestro modulo esta siendo importado o ejecutado directamente como punto de entrada podemos usar la variable \__name__

El interprete de python en tiempo de ejecucion asignara el valor \__main__ a nuestra variable \__name__, de esta forma podemos hacer la distincion antes mencionada.

```python
if __name__ == "__main__":
    # estas sentencias se ejecutaran unicamente cuando
    # nuestro modulo se ejectuado como punto de entrada.
    print("modulo ejecutato como punto de entrada ... pytho modulo.py")
```


## Paquetes en python

Los paquetes en python nos permiten agrupar de forma jerarquica nuestros modulos. De igual forma podemos acceder a todos los modulos de nuestro paquete usando la notacion de punto. Incluso podemos definir subpaquetes dentro de nuestros paquetes.

Definir nuestros paquetes es realmente sencillo, solo tenemos que crear un folder y agregar un archivo/modulo \__init__.py, este modulo es importado(y por lo tanto ejectuado) cuando importamos nuestro paquete. Podemos poner sentencias de inicializacion de nuestro modulo o puede ser un modulo vacio.

A partir de python 3.3 ya no es obligatorio nuestro modulo \__init__, solo es opcional en caso de que necesitemos hacer tareas de inicializacion.

```
📦paquete
 ┣ 📂sub_paquete
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜module3.py
 ┣ 📜__init__.py
 ┣ 📜modulo1.py
 ┗ 📜modulo2.py
```

#### Ejemplo:
**Veamos un ejemplo de nuestro paquete "paquete"**

<br>
<br>

### Sentencia: from <paquete> import *

Con esta sentencia podemos importar todos los modulos de nuestro paquete, si existe algun sub paquete este sera importado(sus modulos de este subpaquete no.

La afirmacion anterior tiene una condicion, la condicion es que se importaran todos los modulos que esten declarados en el modulo de inicializacion \__init__.py como sigue:

<br>

paquete/\__init__.py
```python
__all__ = [
        'modulo1',
        'modulo2',
        ]
```

entrypoint.py
```python
# Esta sentencia de importacion importara modulo1 y modulo2
from paquete import *
```

### Sentencia: from paquete.modulo1 import *

Con esta sentencia de igual forma importamos todos los objetos que se encuentren en nuestro modulo, esta importacion se limita a los restringidos 
por la variable \__all__

<br>

paquete/modulo1.py
```python

__all__ = ["foo", "bar"]

def foo():
    print("foo")

def bar():
    print("bar")

def private_method():
    print("private method")
```

entrypoint.py
```python
# Esta sentencia de importacion importara foo() y bar()
from paquete.modulo1 import *
```



