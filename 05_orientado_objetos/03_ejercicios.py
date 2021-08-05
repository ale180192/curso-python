"""
Definir una clase Producto que tenga las siguientes caracteristicas:
- Un atributo "nombre" donde se almacenara el nombre del producto.
- Un atributo "costo_unitario" donde se almacenara el costo del producto.
- Un atributo "stock" donde indicaremos la cantidad de existencia.
- Definir el metod magico __str__ para que muestre la informacion de sus atributos.
- Definir un metodo que nos permita actualzar su costo_unitario.
- Definir un metodo que nos permita decrementar la existencia en "n" cantidades, Tenemos que lanzar una
    exception personalizada(definir esta exception) cuando queramos disminuir el stock en una cantidad mayor al existente.
    Si la exception es lanzada el stock debe permanecer sin cambios.
- Definir un "metodo de clase/metodo estatico" que nos permita crear objetos tipo Producto a partir de una lista con diccionarios,
    cada diccionario tendra la informacion de un producto. Debera retornar una lista con objetos tipo Producto.

Definir una segunda clase CarritoCompras que tenga las siguientes caracteristicas:

- Un atributo "status" con un valor inicial de "en_proceso".

- Un atributo "productos_db" donde podamos cargar toda la informacion de nuestros productos actuales, este tendra la funcionalidad
    de tener en memoria la informacion de nuestros productos(simularemos que esta info viene de nuestra db).
    Esta informacion sera cargada al instanciarse. Debe ser una lista con elementos de tipo Producto.

- Un atributo "items" donde podamos tener todos los productos que hemos agregado al carrito, 
  asi como la cantidad de elementos de este producto.

- Un atributo "subtotal" para almacenar el subtotal del carrito, este sera la suma de todos
    los productos agregados al carrito. (costo_unitario * cantidad) para cada producto.

- Un atributo de clase "iva_porcentaje"  para almacenar el IVA que sera del 15 porciento

- Un atributo "impuestos" donde almacenaremos el valor que resulte de aplicar el iva_porcentaje al subtotal

- Un atributo "total" para almacenar el total, sera la suma de subtotal mas impuestos.

- un metodo que nos permita agregar un producto al carrito, este metodo tendra que validar contra "productos_db"
    que tengamos existencia, usar el metodo de producto para decrementar y atrapar la excepcion en caso que
    no haya stock. Debera retornar False si la operacion ha fallado, True de lo contrario.

- Un metodo "checkout" que nos retornara un diccionario con resumen de nuestro carrito
    (subtotal, impuestos, total, numero_productos)
    cada que se mande llamar se tendra que re calcular estos parametros.

- Un metodo "pagar" donde simularemos el pago del carrito, unicamente tendremos que
    imprimir un mensaje que diga que el carrito ha sido pagado y tambien cambiar el atributo "status" a pagado
- Sobrecargar el metodo __str__ para que se muestre la informacion de nuestro carrito(reutilizar el metodo checkout)

- Definir un metodo "get_producto_by_nombre" que recibira el nombre del producto a buscar en nuestra "db en memoria"
    productos_db y lo retornara. Lanzara una exception si el producto no existe.

Nota: Validar el funcionamiento de nuestro carrito, utilzando la lista productos que esta mas abajo y tambien
ejectuando el proceso de agregar elementos, y ver el checkout de nuestro carrito.
"""
# ejecucion de nuestro programa
productos = [
    {
        "nombre": "Computadora tech",
        "stock": 3,
        "costo_unitario": 4321
    },
    {
        "nombre": "Monitor 17 pulgadas",
        "stock": 2,
        "costo_unitario": 1490
    },
    {
        "nombre": "Teclado tech",
        "stock": 20,
        "costo_unitario": 200
    },
]

productos = Producto.obtener_productos_apartir_de_data_dict(data=productos)
carrito = CarritoCompras(productos_db=productos)
print(f"Este en nuestro carrito vacio: {carrito}")
print(f"Intentamo gregar 20 teclados al carrito")
producto_teclado = carrito.get_producto_by_nombre(nombre="Teclado tech")
print(f"Estock del teclado: {producto_teclado}")
success = carrito.agregar_item(producto=producto_teclado, cantidad=20)
assert success, "Tu programa debe dar True aqui"
msg = "teclado agregado exitosamente" if success else "Error al agregar al carrito los teclados"
print(msg)
print("agregando otro teclado al carrito")
success = carrito.agregar_item(producto=producto_teclado, cantidad=1)
assert not success, "Tu programa debe dar False aqui"
info = carrito.checkout()
print(f"El resumen del carrito es {info}")
assert int(info["total"]) == 4600, "El total debe ser 4600, validar el resultado."



