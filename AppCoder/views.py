from itertools import product
from urllib import request
from django.shortcuts import render, redirect
from AppCoder.models import Productores
from AppCoder.forms import FormProductor
from django.http import HttpResponse

def Inicio(request):
    return render(request, 'AppCoder/inicio.html')

def Productor (request):

     if request.method == "POST":
        mi_form = FormProductor(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            produc= Productores(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                provincia=info["provincia"],
                descripcion=info["descripcion"],
            )
            produc.save()
            return redirect("Inicio")

     mi_form = FormProductor()
    
     return render(request, "AppCoder/productor.html",{"form": mi_form})

def AsesorTecnico(request):
    return render(request,'AppCoder/asesortecnico.html')

def AgroComercio (request):
    return render(request,'AppCoder/agrocomercio.html')
    
def busquedaProductor(request):

    return render(request,"AppCoder/busquedaproductor.html")

def buscar (request):

   if request.GET["nombre"]:

       nombre=request.GET["nombre"]
       productores=Productores.objects.filter(nombre__icontains=nombre)

       return render (request, 'AppCoder/resultadosbusqueda.html', {"nombre":nombre, "productores":productores})

   else:

        respuesta = "No enviaste datos"

   return HttpResponse(respuesta)

