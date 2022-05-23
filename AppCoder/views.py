from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import FormularioProductor

def Inicio(request):
    return render(request,'AppCoder/inicio.html')

def Productor (request):
    return render(request,'AppCoder/productor.html')

def AsesorTecnico(request):
    return render(request,'AppCoder/asesortecnico.html')

def AgroComercio (request):
    return render(request,'AppCoder/agrocomercio.html')

def formularioProductor(request):
    if request.method == 'POST':
        
        miFormulario= FormularioProductor (request.POST)

        if miFormulario.is_valid():

            informacion=miFormulario.cleaned_data

            registro=  Productor(cultivo=informacion['cultivo'], provincia=informacion['provincia'])

            registro.save()

            return render(request,'AppCoder/inicio.html')

    else:

        miFormulario=FormularioProductor() 
    

    return render(request,'AppCoder/productorFormulario.html', {'miFormulario':miFormulario})





    
    
    return render(request,'AppCoder/agroFormulario.html')

