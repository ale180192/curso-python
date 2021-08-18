### paquetes de terceros
 * El Python Package Index, abreviado como **PyPI** es el repositorio oficial de terceros.

 * **pip** es un sistema gestor de paquetes escrito en python el cual es usado para instalar y gestionar los paquetes de software de python. Por defecto esta conectado al repositorio **PyPI**.

* El modulo **venv** provee soporte para crear **"entornos virtuales"** peso ligero con su propio directorio de sitios(directorio donde se instalan los paquetes), cada entorno virtual tiene su propio binario de python(el cual sera la misma version que el binario usado para crear el entorno virtual). A partir de la version 3.3 este modulo es incorporado por defecto. Crear entornos virtuales nos da la capacidad de trabajar con muchos projectos a la vez, tener versiones especificas del mismo paquete en diferentes entornos.

#### Crear un entorno virtual en linux/mac
```bash
python3 -m venv /path/to/new/virtual/environment
```

<br>

#### Crear el entorno virtual en windows
Este comando nos permite crear un entorno virtual.
```bash
# Opcion 1
c:\>c:\Python35\python -m venv c:\path\to\myenv

# Opcion 2
c:\>python -m venv c:\path\to\myenv
```

#### Activar el entorno virtual
Una vez que hemos creado nuestro entorno virtual tenemos que activarlo para poder usarlo, una vez que esta activado todos los paquetes que instalemos se instalaran en nuestro entorno virtual, en general todas las operaciones que hagamos con pip afectaran a este entorno. de igual forma cuando ejecutemos el binario de python se mandara llamar el del entorno virtual.

<table>
    <thead>
    <tr>
        <th>Plataforma</th>
        <th>Shell</th>
        <th>Comando</th>
    </tr>
    </thead>
    <tbody>
        <tr>
            <td>POSIX</td>
            <td>bash/zsh</td>
            <td>$ source venv/bin/activate</td>
        </tr>
        <tr>
            <td></td>
            <td>PowerShell Core</td>
            <td>$ <venv>/bin/Activate.ps1</td>
        </tr>
        <tr>
            <td>Windows</td>
            <td>cmd.exe</td>
            <td>C:\> <venv>\Scripts\activate.bat</td>
        </tr>
        <tr>
            <td></td>
            <td>PowerShell</td>
            <td>PS C:\> <venv>\Scripts\Activate.ps1</td>
        </tr>
    </tbody>
</table>


#### Instalar un paquete de terceros con **pip**
Podemos intalar cualquier paquetes de tercero que se encuentre en el repositorio oficial **PyPI** unicamente con el siguiente comando.

```bash
pip install <nombre paquete>
```

### Generar un archivo de todas las dependencias.
Podemos generar un archivo de texto con todas las dependencias de nuestro entorno virtual, es decir, el archivo tendra todos los paquetes que hemos instalado asi como su version.

```bash
pip freeze > <nombre_archivo.txt>
```

### Instalar dependencias a partir de un archivo de texto.
Si tenemos un archivo con todas las dependencias podemos instalar todas ellas con un unico comando.

```bash
pip install -r <archivo.txt>
```

#### Ejemplo

Veamos un ejemplo completo:

```bash
# Creamos nuestro entorno virtual
python -m venv .venv

# Activamos nuestro entorno virtual
source .venv/bin/activate

# Instalamos un paquete
pip install django

# Gereramos nuestro archivo de dependencias
pip freeze > requeriments.txt

# Instalamos las dependencias a partir de un archivo.txt
pip install -r requeriments.txt

# desactivar entorno virtual
deactivate
```
