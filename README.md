# Mayorga-Entrega_Final
Alumna: Vanesa Yasmin Mayorga

Link al video en YouTube: https://www.youtube.com/watch?v=iGns2sLIGZQ&t=1s

El NavBar contiene las opciones:
- Inicio
- Acerca de Mí
- Páginas
    - Profesores
    - Cursos
    - Estudiantes
- Panel de Administración

* Si el usuario no está logueado:
- Iniciar Sesión
- Registrarse

* Si el usuario está logueado:
- Nombre de usuario (que redirige a la página de perfil de usuario)
- Cerrar Sesión.

El menú "Páginas" redirige a una página con el path /pages/ donde también se pueden acceder a los formularios de Profesores, Cursos y Estudiantes.

Se agregó la opción "Panel de Administración" como parte del menú navbar, para acceder a la vista de administración de Django.

Para acceder a la vista de administración, se debe crear un super usuario, ya que tanto la DB como los archivos media fueron agregados al archivo .gitignore. Por esto mismo es que los formularios van a estar vacíos.

Existen 3 formularios para agregar datos en la base de datos, disponibles en los menúes Cursos, Profesores y Estudiantes.

Además, en el menú Estudiantes, se puede realizar un filtro por "Carreras" a través de otro formulario. Si el filtro no devuelve ningún resultado, va a mostrar un cartel que lo indique.

En cada formulario, las opciones de "Cancelar" vuelven a la vista original del menú.

Si el usuario intenta acceder a una página no existente, va a mostrar una página de error 404 personalizada. Esto fue posible por modificar la opción DEBUG en False en el settings.py, por lo tanto este proyecto debería correrse únicamente en un entorno de dev o test, pero no en producción.

El usuario puede modificar sus datos personales, incluyendo su imagen de perfil, o agregar una biografía, desde la opción "Editar Perfil", accesible desde la página del perfil de usuario. 

Además, desde la misma página el usuario puede cambiar su contraseña, y cerrar su sesión.