from django.urls import path
from . import views

urlpatterns = [  
    path('', views.blogview, name='blog'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]
