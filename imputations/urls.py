from django.urls import path
from . import views

urlpatterns = [
    path('', views.imputations_view, name='imputations'),
    # Otras rutas
]