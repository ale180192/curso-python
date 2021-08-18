from django.urls import path, include

urlpatterns = [
    path(route="hello_world/", view=include("hello_world.urls")),
    path(route="eccomerce/", view=include("eccomerce.urls"))
]
