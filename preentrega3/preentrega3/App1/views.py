from django.shortcuts import render
from django.http import HttpResponse
from App1.models import Guitarra
from App1.forms import GuitarrasFormulario

def inicio(request):
    return render(request, 'App1/inicio.html')
def guitarras(request):
    return render(request, 'App1/guitarras.html')
def guitarrasInfo(request):
    return render(request, 'App1/guitarrasInfo.html')

def guitarrasFormulario(request):
     if request.method == "POST":
        miFormulario = GuitarrasFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            guitarra = Guitarra(int(informacion['id']),str(informacion['nombre']),str(informacion['color']))
            guitarra.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = GuitarrasFormulario()
             
     return render(request, "App1/guitarrasFormulario.html", {"miFormulario": miFormulario})



def busquedaInstrumento(request):
    return render(request, 'App1/busquedaInstrumento.html')

def buscar(request):
     if request.GET['color']:
          color = request.GET['color']
          colores= Guitarra.objects.filter(color__icontains=color)

          return render(request,'App1/resultadosBusqueda.html', {"colores":colores, "color": color })
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)


    


# Create your views here.
