from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

def proyectos(request):

    mis_proyectos = [
        {'titulo':'Crud postres con foto en Django',
         'ruta_imgen':'images/image.png',},
        {'titulo':'Crud de Alumnos con Django',
         'ruta_imgen':'images/crudalu.png',},
        {'titulo':'gestor de ordenes con Django',
         'ruta_imgen':'images/ordenes.png',},
    ]
    context = {'proyectos': mis_proyectos}
    return render(request, 'proyectos.html', context)

def experiencia_laboral(request):
    experiencia = [
        {'preparatoria': 'Cbtis 128',
         'carrera': 'Programacion',
         'fecha_inicio': '1989',
         'fecha_fin': '2025'},
        {'preparatoria': 'Conalep I Juarez',
         'carrera': 'Informatica',
         'fecha_inicio': '1991',
         'fecha_fin': '2022'},
    ]
    context = {'experiencia': experiencia}
    return render(request, 'experiencia_laboral.html', context)

def certificados(request):
    return render(request, 'certificados.html')

def contacto(request):
    return render(request, 'contacto.html')

