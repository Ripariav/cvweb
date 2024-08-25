from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Vista principal para la app main
]
