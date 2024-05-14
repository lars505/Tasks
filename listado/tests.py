from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tasks

User = get_user_model()

class PruebasModeloTasks(TestCase):

    def setUp(self):
        # Configura un usuario y una tarea de prueba que se utilizarán en los casos de prueba
        self.usuario = User.objects.create_user(username='usuarioprueba', password='contraseña123')
        self.tarea = Tasks.objects.create(
            titulo='Tarea de Prueba',
            descripcion='Esta es una descripción de prueba para la tarea',
            completado=False,
            estado=True,
            usuario=self.usuario
        )

    def test_creacion_tarea(self):
        # Verifica que una tarea se haya creado correctamente con los valores proporcionados
        self.assertEqual(self.tarea.titulo, 'Tarea de Prueba')
        self.assertEqual(self.tarea.descripcion, 'Esta es una descripción de prueba para la tarea')
        self.assertFalse(self.tarea.completado)
        self.assertTrue(self.tarea.estado)
        self.assertEqual(self.tarea.usuario.username, 'usuarioprueba')

    def test_metodo_str_tarea(self):
        # Verifica el método __str__ del modelo Tasks
        self.assertEqual(str(self.tarea), 'Tarea de Prueba - False')

    def test_valores_por_defecto_tarea(self):
        # Verifica que los valores predeterminados para los campos completado y estado sean correctos
        tarea = Tasks.objects.create(
            titulo='Otra Tarea',
            descripcion='Otra descripción de tarea',
            usuario=self.usuario
        )
        self.assertFalse(tarea.completado)
        self.assertTrue(tarea.estado)

    def test_actualizacion_tarea(self):
        # Verifica que los cambios en una tarea se guarden correctamente
        self.tarea.completado = True
        self.tarea.save()
        tarea_actualizada = Tasks.objects.get(id=self.tarea.id)
        self.assertTrue(tarea_actualizada.completado)

    def test_eliminacion_tarea(self):
        # Verifica que una tarea se elimine correctamente
        tarea_id = self.tarea.id
        self.tarea.delete()
        with self.assertRaises(Tasks.DoesNotExist):
            Tasks.objects.get(id=tarea_id)
