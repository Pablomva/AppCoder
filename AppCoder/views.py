from django.http import HttpResponse
from django.shortcuts import render

def Inicio(request):
    return render(request,'AppCoder/inicio.html')

def Productor (request):
    return render(request,'AppCoder/productor.html')

def AsesorTecnico(request):
    return render(request,'AppCoder/asesortecnico.html')

def AgroComercio (request):
    return render(request,'AppCoder/agrocomercio.html')

