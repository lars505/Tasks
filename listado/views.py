from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate

from .models import Tasks, User

import json

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

        usuario = User.objects.get(username = request.user)
        context = {
            "tasks": Tasks.objects.filter(
                estado = True, 
                completado = False,
                usuario = usuario
                
            ),
            "realizada": Tasks.objects.filter( completado = True, usuario = usuario),
            "eliminadas": Tasks.objects.filter( estado = False, usuario = usuario)
        }
        print(context)
        return render(request, "listado/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))
    
def tasks(request):
    usuario = User.objects.get(username = request.user)

    tasks =  Tasks.objects.filter( estado = True,  completado = False, usuario = usuario ).values()
    data = {
        "tasks" : list(tasks)
    }
    return JsonResponse(data)



def agregar(request):
    if request.method != "POST":
        return JsonResponse({ "error" : "La peticion no es de tipo POST"})
        
    data = json.loads(request.body)

    Tasks.objects.create(
        titulo = data['titulo'],
        descripcion = data['descripcion'],
        usuario = request.user
    )
    return JsonResponse({'mensaje':'Tarea agregada!'})

def eliminar(requeste, id):
    task = Tasks.objects.get(id = id)
    task.estado = False
    task.save()
    messages.success(requeste, 'Tarea eliminada')
    return redirect(to="index")

def realizadas(request, id):
    task = Tasks.objects.get(id = id)
    task.completado = True
    task.save()
    messages.success(request, 'Tarea realizada')
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
            messages.warning(request, 'Ingrese un usuario o contraseña valido!')
            return render(request, "listado/login.html")
    else:
        return render(request, "listado/login.html")
    
def Logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada')
    return HttpResponseRedirect(reverse("index"))








