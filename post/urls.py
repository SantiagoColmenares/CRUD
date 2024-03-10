from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('storage/<str:titulo>/<str:cuerpo>/<int:id>', views.storage, name="storage"),
    path('consultar/<int:id>', views.consultar, name="consultar"),
    path('modificar/<int:id>/<str:titulo>', views.modificar, name="modificar"),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('storageA/<str:nombre_A>/<str:correo>/', views.storageA, name="storageA")
]