from django.urls import path
from . import views

urlpatterns = [
    path('', views.boards_view, name='boards'),
    # Otras rutas
]