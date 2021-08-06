# El pdb(Python Debugger)
El pdf define un interactivo debuger de codigo fuente para programas de python.

pdb tiene las siguientes caracteristicas:
* Soporta puntos de ruptura(breakpoints)
* avances de linea por linea en el codigo fuente
* inspeccion de los stack frames(la informacion de todo el stack de la subrutina)
* Evaluacion arbitraria de codigo python en el contexto de algun stack frame.


## Ejecutar nuestro debuger.
Existen dos formas de ejecutar nuestro debuger:

* Importando el modulo pdb en un script de python y ejecutando este script directamente. Veamos un ejemplo

* Desde la linea de comandos invocando el modulo y pasando como parametro el script que queremos debugear


### Primera forma
<br>

mi_script.py
```python
class User:

    def __init__(self, nombre, semestre) -> None:
        self.nombre = nombre
        self.semestre = semestre

    def get_nombre(self):
        return self.nombre


def func():
    user = User("Juan", 5)
    nuevo_nombre = "Maria"
    user.nombre = nuevo_nombre
    if len(user.nombre) >= 4:
        print("El nombre tiene mas de 4 caracteres")
        user.nombre = user.nombre[:4]

    print(f"nombre es: {user.nombre}")


```
<br>

debug_mi_script.py
```python
import pdb
pdb.run('mi_script.py')
```
<br>

\# ejecutamos directamente nuestro script debug_mi_script.py
```bash
python 07_apendice/debug_mi_script.py 
```

Nota: Se activa el modo iteractivo del debuger de forma automatica, esperando nuestras instrucciones.

### Las instrucciones mas importantes son las siguientes:

<br>

> La [documentacion oficial](https://docs.python.org/3/library/pdb.html) tiene todas las instrucciones a detalle.

* h(elp): Nos dice los comandos disponibles.
* d(own): Nos adentramos en un interno nuevo stack frame.
* u(p): Salimos a un nivel externo del stack frame.
* s(step): Ejecuta la actual linea, si es una llamada a una funcion ejecuta la primer linea de la funcion y se detiene.
* n(ext): Identico a step pero ejecuta toda la funcion y se detiene en la siguiente linea.
* c(ont(inue)): Se ejecuta hasta encontrar el siguiente breakpoint.
* pp expression: Evalua la expresion en el actual contexto.


## Segunda forma

```bash
python3 -m pdb python3 -m pdb 07_apendice/mi_script.py
```

## Usando el debuger de **Visual Studio Code**

La mejor forma hacer debug en nuestros scripts es sin duda usando las herramientas graficas que nos proporcionan los IDE's.

Visual Studio Code cuenta con un debuger para python. Para ejecutarlo tenemos que hacer lo siguiente:

* Tener abierto nuestro script
* Ir al menu Run -> Start debug. Se nos preguntara que es lo que queremos debuguear, seleccionamos **pytho file**
* En automatico nuestro script sera ejecutado deteniendose en el primer breakpoint que hayamos definido.
