from xml.etree.ElementInclude import include
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.Inicio, name='Inicio'),
    path('productor/', views.Productor, name='Productor'),
    path('asesortecnico/', views.AsesorTecnico, name='Asesor Tecnico'),
    path('agrocomercio/', views.AgroComercio, name='Agro Comercio'), 
    #path('formularioproductor/',views.nuevo_productor),
    path ('busquedaproductor/', views.busquedaProductor, name='Busqueda productor'),
    path ('buscar/',views.buscar),

]
