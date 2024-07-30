from django.shortcuts import render, redirect
from .models import Autor, Editorial, Libro
from .forms import AutorForm, EditorialForm, LibroForm

def home(request):
    return render(request, 'entregaIII/home.html')

# Autores
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'entregaIII/autor_list.html', {'autores': autores})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'entregaIII/autor_form.html', {'form': form})

def autor_search(request):
    query = request.GET.get('q')
    if query:
        autores = Autor.objects.filter(nombre__icontains=query)
    else:
        autores = Autor.objects.all()
    return render(request, 'entregaIII/autor_search.html', {'autores': autores})

# Editoriales
def editorial_list(request):
    editoriales = Editorial.objects.all()
    return render(request, 'entregaIII/editorial_list.html', {'editoriales': editoriales})

def editorial_create(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editorial_list')
    else:
        form = EditorialForm()
    return render(request, 'entregaIII/editorial_form.html', {'form': form})

def editorial_search(request):
    query = request.GET.get('q')
    if query:
        editoriales = Editorial.objects.filter(nombre__icontains=query)
    else:
        editoriales = Editorial.objects.all()
    return render(request, 'entregaIII/editorial_search.html', {'editoriales': editoriales})

# Libros
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'entregaIII/libro_list.html', {'libros': libros})

def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'entregaIII/libro_form.html', {'form': form})

def libro_search(request):
    query = request.GET.get('q')
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()
    return render(request, 'entregaIII/libro_search.html', {'libros': libros})
