from xml.etree.ElementInclude import include
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.Inicio),
    path('productor/', views.Productor, name='Productor'),
    path('asesortecnico/', views.AsesorTecnico, name='Asesor Tecnico'),
    path('agrocomercio/', views.AgroComercio, name='Agro Comercio'), 

]
