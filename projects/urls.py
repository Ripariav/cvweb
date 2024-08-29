from django.urls import path
from . import views

urlpatterns = [  
    path('', views.projectsview, name='projects')
]
