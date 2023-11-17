# Practica5-Login-parte3

## Aplicación Web con Flask y Autenticación de Usuarios y Sesiones

### Descripción

En esta aplicación web Flask demostramos la autenticación de usuarios y la gestión de sesiones utilizando la extensión Flask-Login. Incluye funciones como inicio de sesión, cierre de sesión y acceso restringido a ciertas rutas según los roles de usuario que en este caso los asignamos en la base de datos con 'User.types'.
Las sesiones permiten que los sitios web recuerden la información sobre un usuario específico a medida que navegan entre páginas o realizan acciones en el sitio


### Uso
1. Ejecuta la aplicación Flask:

   ```bash
   flask run
   ```

2. Abre un navegador web y accede a `http://127.0.0.1:5000/` para ir a la página de inicio de sesión.

3. Utiliza el nombre de usuario y la contraseña que asignamos en la base de datos para iniciar sesión.

4. Ambas paginas puedne verse similares en ambos roles solo en administrador se le agrego la etiqueta 'Mr' antes del nombre.

### Estructura del Proyecto

- **app.py:** Archivo principal de la aplicación que contiene la configuración de la aplicación Flask, las rutas y la configuración.

- **models/ModelUsers.py:** Clase del modelo que maneja la autenticación del usuario y las interacciones con la base de datos.

- **templates/:** Plantillas HTML para diferentes páginas (inicio de sesión, inicio, administrador).

- **static/:** Contiene archivos CSS para el estilo.

### Configuración

- **Configuración del LoginManager:**
  
  ```python
  from flask_login import LoginManager, login_user, logout_user, login_required

  app = Flask(__name__)
  login_manager = LoginManager(app)
  ```

- **Método User Loader:**

  ```python
  @login_manager.user_loader
  def load_user(id):
      return ModelUsers.get_by_id(mysql, id)
  ```

- **Decorador Requerido para Administradores:**

  ```python
  from functools import wraps
  from flask import abort

  def admin_required(func):
      @wraps(func)
      def decorated_view(*args, **kwargs):
          if not current_user.is_authenticated or current_user.usertype != 1:
              abort(403)  # Acceso prohibido
          return func(*args, **kwargs)
      return decorated_view
  ```

