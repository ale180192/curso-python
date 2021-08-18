from django.http import response
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Producto, Carro

@api_view(["GET"])
def listar_productos(request):
    productos = Producto.objects.all()
    productos_dict = [{
        "nombre": p.nombre,
        "stock": p.stock,
        "costo_unitario": p.costo_unitario
    } for p in productos
    ]
    return Response(data=productos_dict)

@api_view(["POST",])
def crear_carrito(request):
    data = request.data
    carro = Carro.objects.create(**{
        "subtotal": data["subtotal"],
        "impuestos": data["impuestos"],
        "total": data["total"],
        "status": data["status"],

    })
    return Response(data={"id": carro.id})
       

@api_view(["PUT"])
def actualizar_carrito(request, id):
    """
    from eccomerce.models import Producto as P
    P.objects.create(nombre="laptop", stock=23, costo_unitario=6789)
    """
    items = request.data.get("items")
    carro = Carro.objects.get(pk=id)
    carro.items.clear()
    productos = [Producto.objects.get(pk=item) for item in items]
    for producto in productos:
        carro.items.add(producto)
        
    return Response(data={"id": carro.id})


@api_view(["GET"])
def checkout(request, id):
    """
    from eccomerce.models import Producto as P
    P.objects.create(nombre="laptop", stock=23, costo_unitario=6789)
    """
    carro = Carro.objects.get(pk=id)
    carro.actualizar_costos()
    info = {
        "total": carro.total,
        "subtotal": carro.subtotal,
        "impuestos": carro.impuestos,
        "items": len(carro.items.all()),
    }
    return Response(data={"data": info})

