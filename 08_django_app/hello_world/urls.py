from django.urls import path

from . import views

urlpatterns = [
    path(route="hello_world_function", view=views.hello_world_function),
    path(route="hello_world_class", view=views.HelloWorldClass.as_view()),
    path(route="hello_world_orm", view=views.hello_world_orm),
]