from django.shortcuts import render
from .models import Proyecto
# Create your views here.
def projectsview(request):
    proyectos = Proyecto.objects.all()  
    return render(request, 'projects/projects.html', {'proyectos': proyectos})