from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tasks', views.tasks, name='tasks'),
    path('agregar',views.agregar, name="agregar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('realizada/<int:id>', views.realizadas, name="realizada"),
    path('register', views.register_vista, name="register"),
    path('login', views.Login_view, name="login"),
    path('logout', views.Logout_view, name="logout"),
   
]
