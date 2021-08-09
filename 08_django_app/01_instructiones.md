
# API REST con django

## Hola mundo

Estando en el folder 08_django_app ejecutaremos los siguientes comandos

### nos ubicamos en el directorio correcto
```bash
cd 08_django_app/
```

### Instalamos y activamos nuestro entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalamos nuestro packete django
```bash
pip install django
```

### Creamos nuestro projecto el cual nombramos app
```bash
# el punto indica que se instalara sobre el directorio actual(no creara otro folder)
django-admin startproject app .
```

### Validamos funcione correctamente
Levantaremos el servidor web integrado de django, este servidor es util para la fase de desarrollo unicamente. Por defecto se levantara en localhost utilizando el puerto 8000, podemos validar que se ingresando en el navegador a la [url](http://127.0.0.1:8000) se muestre correctamente nuestro hola mundo.
```bash
python manage.py runserver
```

### Instalacion django-rest-framework(DRF)
DRF es una app de django que nos permite trabajar con API's REST directamente en django. [link a la doc oficial](https://www.django-rest-framework.org/)
```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

Agregamos nuestra app instalada al settings.py
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### Hola mundo con DRF
Vamos a crear un hola mundo con DRF, este sera un servicio/endpoint GET /hola_mundo el cual nos regresara un mensaje de hola mundo.
Creemos nuestra app de django que se llamara hola_mundo.
Es importante que tengamos el entorno virtual activado y estemos en la ruta correcta(08_django_app)

```bash
python manage.py startapp hola_mundo
```

Podemos observar que se crear un folder hola_mundo que tiene la siguiente estructura:

📦hola_mundo
 ┣ 📂migrations
 ┃ ┗ 📜__init__.py
 ┣ 📜__init__.py
 ┣ 📜admin.py
 ┣ 📜apps.py
 ┣ 📜models.py
 ┣ 📜tests.py
 ┗ 📜views.py


views.py: Es un archivo el cual tiene la capa web, es decir aqui habra funciones o clases que tienen la funcionalidad de atender todas las peticiones http que lleguen a nuestra API REST y dar una respuesta. Cuando llegue una peticion a nuestro servidor, django tomara el control, identificara el metodo(GET, POST, PUT, etc) y la URI, y con esto invocara la funcion/clase correcta a ejecutarse.

models.py: Este archivo contiene todos nuestros modelos, estos modelos son utilizados por el ORM para crear las tablas en nuestra base de datos.

tests.py: Este archivo contiene todas las pruebas unitarias/integracion de nuestro codigo, es totalmente opcional.

admin.py: Este archivo contiene el codigo necesario para poder habilitar el admin integrado de django para nuestra app, es totalmente opcional.

urls.py Este archivo es opciona pero recomendable por app. contiene el codigo que relaciona las URIS con nuestras funciones/clases.

**migrations**: Este folder contiene todos los archivos de migracion que son generados en automatico por el ORM de django, no tenemos que modificar manualmente estos archivos.

Todas las aplicaciones que usemos en nuestra app de django tenemos que agregarlas a la varibable INSTALLED_APPS del settings. asi que esta tambien la agregamos
\#app.setting.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'hello_world',
]
```


Primero vamos a definir nuestra funcion/clase que manejara la peticion y respuesta. Definimos una vista basada en clase y basada en funcion para ver las diferencias.

\#hello_world/views.py
```python
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(('GET',))
def hello_world_function(request):
    data = {
        "mensaje": "Hola mundo"
    }
    print("ok")
    return Response(data=data, status=status.HTTP_200_OK)


class HelloWorldClass(APIView):

    def get(self, request):
        data = {
            "message": "Hello world"
        }
        return Response(data=data, status=status.HTTP_200_OK)
```

Segundo creamos un archivo urls.py y agregamos el siguiente codigo.

\#hello_world/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path(route="hello_world_function", view=views.hello_world_function),
    path(route="hello_world_class", view=views.HelloWorldClass.as_view()),
]
```

Tercero. Agregamos todas las urls de nuestra app al proyecto principal **app**.

\#app/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route="hello_world/", view=include("hello_world.urls"))
]

```

Cuarto. Validamos que este funcionando correctamente nuestros dos endpoints.
```bash
curl --location --request GET 'http://127.0.0.1:8000/hello_world/hello_world_function'
curl --location --request GET 'http://127.0.0.1:8000/hello_world/hello_world_class'
```

<br>

## Usando el ORM
El ORM de django tiene soporte para una gran cantidad de motores de bases de datos, por defecto esta configurado para usar sqlite3 como motor. Esto lo podemos configurar en la variable diccionario **settings.DATABASES**.

<br>

## Ejemplo ORM
Vamos a definir un modelo, generar nuestros archivos de migracion y por ultimo ejecutar nuestras migraciones, estas ultimas nos generaran las tablas correspondientes.

<br>

\#hello_world/models.py

```python
from django.db import models

class Producto(models.Model):
    name = models.CharField(max_length=30)
    stock = models.PositiveSmallIntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

Despues generamos y ejecutamos las migraciones.
```bash
python manage.py makemigrations
python manage.py migrate
```

Observamos que **"python manage.py makemigrations"** nos genera un archivo **0001_initial.py** en el folder de migraciones de nuestra app. Este archivo tiene codigo python y es ejectutado cuando ejectutamos el comando **"python manage.py migrate"**. El ORM es muy inteligente y si ejecutamos nuestros comandos mas de una vez detectara que ya no es necesario volver a hacer algo mas.

Podemos modificar nuestro modelo Producto, tal vez agregar un nuevo campo. Para que esto se vea reflejado en nuestra db tenemos que de nuevo generar nuestro archivo de migraciones y ejecutar estas migraciones.

### Nuevo endopint que use nuestro modelo
generamos una nueva funcion en views.py llamada **hello_world_orm**, agregamos la ruta a nuestro archivo urls.py y ejecutamos por curl para ver el resultado.


\# hello_world/views.py
```python
.
.
.

@api_view(('GET',))
def hello_world_orm(request):
    from .models import Producto
    products  = Producto.objects.all()
    products_dict = [{"name": p.name, "price": p.price, "stock": p.stock} for p in products]
    return Response(data=products_dict, status=status.HTTP_200_OK)
```

\# hello_world/urls.py
```python
urlpatterns = [
    .
    .
    path(route="hello_world_orm", view=views.hello_world_orm),
]
```


Antes de hacer una peticion a nuestro nuevo endpoint tenemos que agregar registros a nuestra tabla Productos. Para esto podemos usar el modulo **admin.py** que tiene django para ejecutar comandos de forma interactiva.
```bash
python manage.py shell
#importamos nuestro modelo
from hello_world.models import Producto
# Creamos dos productos
producto = Producto.objects.create(name="laptop", stock=3, price=6500)
producto = Producto.objects.create(name="teclado", stock=20, price=220)
```

Hacemos la peticion al nuevo endpoint
```bash
curl --location --request GET 'http://127.0.0.1:8000/hello_world/hello_world_orm'
```



