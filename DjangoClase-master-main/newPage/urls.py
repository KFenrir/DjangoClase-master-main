from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("crud", views.crud, name="crud"),
    path("userAdd", views.userAdd, name="userAdd"),
    path("userDel/ <str:pk>", views.userDel, name="userDel"),
    path("userEdit/ <str:pk>", views.userEdit, name="userEdit"),
    path("userUpdate", views.userUpdate, name="userUpdate"),
    path("main", views.main, name="main"), 
    path("login",views.login, name="login"),
    path("gatos", views.gatos, name="gatos"),
    path("perros", views.perros, name="perros"),
    path("arnes_gatos", views.arnes_gatos, name="arnes_gatos"),
    path("bandana_gatos", views.arnes_gatos, name="badana_gatos"),
    path("collar_gatos", views.arnes_gatos, name="collar_gatos"),
    path("carrito", views.carrito, name="carrito"),
    path("catalogo", views.catalogo, name="catalogo"),
    path("registro", views.registro, name="registro"),
    path("tallas", views.tallas, name="tallas"),
    path("suscripciones", views.suscripciones, name="suscripciones"),
    path("nosotros", views.nosotros, name="nosotros"),
]
