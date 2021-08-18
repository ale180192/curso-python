from django.urls import path

from . import views



urlpatterns = [
    path(route="productos", view=views.listar_productos),
    path(route="carro", view=views.crear_carrito),
    path(route="carro/<int:id>", view=views.actualizar_carrito),
    path(route="carro/<int:id>/checkout", view=views.checkout),
]