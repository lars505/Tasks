from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate

from .models import Tasks, User

# Create your views here.'
lista = []
lista.append("Barrer")

# diccionarios
Tareas = {
    "Eliminadas":[],
    "Realizadas": []
}

def index(request):

    if request.user.is_authenticated:
        context = {
            "tasks": Tasks.objects.filter(
                estado = True, completado = False
            ),
            "realizada": Tasks.objects.filter( completado = True),
            "eliminadas": Tasks.objects.filter( estado = False)
        }
        print(context)
        return render(request, "listado/index.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def agregar(request):
    if request.method == "POST":
       titulo = request.POST['titulo']
       tarea = request.POST['tarea']
       Tasks.objects.create(
           titulo = titulo,
           descripcion = tarea,
           usuario = request.user
       )
       return redirect(to="index")
    return render(request, "listado/agregar.html")

def eliminar(requeste, id):
    task = Tasks.objects.get(id = id)
    task.estado = False
    task.save()
    return redirect(to="index")

def realizadas(request, id):
    task = Tasks.objects.get(id = id)
    task.completado = True
    task.save()
    return redirect(to="index")

def register_vista(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            return render(request, "listado/register.html",{
                'titulo':"register"
            } )
        
        user = User.objects.create_user(
            username = username,
            password = password
        )
        user.save()
        login(request, user)
        messages.success(request, 'Usuario registrado')
        return redirect(to="index")
    else:
        return render(request, "listado/register.html",{
                'titulo':"register"
            } )

def Login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvendo!')
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.warning(request, 'ingrese un usuario valido!')
            return render(request, "listado/login.html")
    else:
        return render(request, "listado/login.html")
    

def Logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))








