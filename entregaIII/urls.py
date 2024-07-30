from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autores/', views.autor_list, name='autor_list'),
    path('autores/nuevo/', views.autor_create, name='autor_create'),
    path('autores/buscar/', views.autor_search, name='autor_search'),
    path('editoriales/', views.editorial_list, name='editorial_list'),
    path('editoriales/nuevo/', views.editorial_create, name='editorial_create'),
    path('editoriales/buscar/', views.editorial_search, name='editorial_search'),
    path('libros/', views.libro_list, name='libro_list'),
    path('libros/nuevo/', views.libro_create, name='libro_create'),
    path('libros/buscar/', views.libro_search, name='libro_search'),
]
