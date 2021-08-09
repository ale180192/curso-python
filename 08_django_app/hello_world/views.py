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

@api_view(('GET',))
def hello_world_orm(request):
    from .models import Producto
    products  = Producto.objects.all()
    products_dict = [{"name": p.name, "price": p.price, "stock": p.stock} for p in products]
    return Response(data=products_dict, status=status.HTTP_200_OK)