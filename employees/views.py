from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializer
from django.shortcuts import render

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

def home(request):
    return render(request, 'employees/home.html')
