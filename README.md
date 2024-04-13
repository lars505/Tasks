
# Task

¡Bienvenido a Tasks!


Proyecto básico de listar tareas, terminar las tareas y eliminar las tareas, con la finalidad de enseñar a ocupar los modelos de Django en una base de datos de PostgreSQL 

## Instalación

Instrucciones sobre cómo instalar y configurar el proyecto en tu entorno local.

1. Clona este repositorio en tu máquina local.
   ```bash
   git clone https://github.com/lars505/Tasks.git
   ```

2. Instala las dependencias.
   ```bash
   pip install -r requirements.txt
   ```

3. Crea un archivo para el manejo de las variables de entorno
   ```bash
   .env
   ```
4. Agrega la variable de entorno DATABASE_URL y asígnale la cadena de conexión.
   ```bash
   DATABASE_URL=[cadena de conexion]
   ```
  5. Realiza las migraciones de la base de datos.
	   ```bash
	 python manage.py migrate
	   ```

## Uso

Explicación de cómo utilizar el proyecto y sus características principales.

1. Ejecuta el servidor local.
   ```bash
   python manage.py runserver
   ```

2. Accede a [http://localhost:8000](http://localhost:8000) en tu navegador.
3. Regístrate y Listo!

## Contribuir

Instrucciones para contribuir al proyecto, ya sea reportando problemas, proponiendo nuevas características o enviando pull requests.

1. Crea un fork del repositorio.
2. Crea una nueva rama para tu contribución.
   ```bash
   git checkout -b feature/nueva-caracteristica
   ```
3. Haz tus cambios y asegúrate de que las pruebas pasen.
4. Haz un commit de tus cambios.
   ```bash
   git commit -m "Agrega nueva característica"
   ```
5. Sube tu rama al repositorio remoto.
   ```bash
   git push origin feature/nueva-caracteristica
   ```
6. Abre un pull request en GitHub.



## Contacto

Si tienes preguntas o sugerencias sobre el proyecto, contáctame en [task.lars50593@gmail.com].
