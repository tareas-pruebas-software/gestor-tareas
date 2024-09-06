# Gestor de Tareas

## Descripción
El **Gestor de Tareas** es una aplicación de línea de comandos diseñada para ayudar a los usuarios a gestionar sus tareas diarias. Permite crear, consultar, actualizar y eliminar tareas, así como organizarlas mediante etiquetas y gestionarlas por estados (pendiente, en progreso, completada). También incluye funcionalidades de autenticación y registro de logs para mejorar la seguridad y el seguimiento de actividades dentro del sistema.

## Características
- **CRUD de Tareas**: Crear, consultar, actualizar y eliminar tareas fácilmente.
- **Filtrado y Búsqueda**: Filtra tareas por estado, etiqueta, y fecha de vencimiento.
- **Gestión de Estados**: Marca tareas como "pendiente", "en progreso" o "completada", y archiva las completadas para futura referencia.
- **Autenticación**: Asegura el acceso mediante autenticación de usuarios con nombre de usuario y contraseña.
- **Logs**: Registra todas las operaciones importantes realizadas dentro del sistema (para Java se usa Log4J).
- **Tareas Archivadas**: Consulta de tareas completadas y archivadas.

## Requisitos
- **Python 3.0 o superior**
- Sistema operativo compatible con Python

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tareas-pruebas-software/gestor-tareas
   ```

2. Ejecuta el programa:
  ```bash
  python3 main.py
  ```
## Uso
Una vez ejecutado el programa, aparecerá un menú en la línea de comandos con las siguientes opciones:

1. **Crear nueva tarea.**
2. **Ver todas las tareas.**
3. **Filtrar tareas por estado, etiqueta, o fecha de vencimiento.**
4. **Ver tareas archivadas.**
5. **Actualizar o eliminar una tarea.**
6. **Cerrar sesión.**

### Usuarios predeterminados
- **admin**: contraseña "123"
- **Vicente**: contraseña "1234"

Para agregar nuevos usuarios, puedes editar la variable `users` en el archivo `auth.py`.

## Cómo contribuir

Si deseas contribuir al proyecto en el repositorio [gestor-tareas](https://github.com/tareas-pruebas-software/gestor-tareas), sigue estos pasos:

1. **Haz un fork** del repositorio en GitHub:
   - Ve a la página del repositorio [gestor-tareas](https://github.com/tareas-pruebas-software/gestor-tareas).
   - Haz clic en el botón "Fork" en la esquina superior derecha de la página.

2. **Clona tu fork** en tu máquina local:
   - Reemplaza `tuusuario` con tu nombre de usuario en GitHub en el siguiente comando:
     ```bash
     git clone https://github.com/tuusuario/gestor-tareas.git
     ```

3. **Crea una nueva rama** para tu funcionalidad o corrección:
   - Cambia `nombre-de-tu-rama` por un nombre descriptivo de tu rama:
     ```bash
     git checkout -b nombre-de-tu-rama
     ```

4. **Realiza los cambios** necesarios en tu entorno local. 

5. **Haz commit de tus modificaciones**:
   - Añade tus cambios al área de preparación:
     ```bash
     git add .
     ```
   - Crea un commit con un mensaje descriptivo:
     ```bash
     git commit -m "Descripción de los cambios realizados"
     ```

6. **Sube tus cambios** a tu fork en GitHub:
   - Asegúrate de estar en la rama correcta y sube tus cambios:
     ```bash
     git push origin nombre-de-tu-rama
     ```

7. **Crea un Pull Request**:
   - Ve a la página de tu fork en GitHub.
   - Verás un botón para "Compare & pull request" en tu rama recién subida.
   - Añade una descripción detallada de los cambios y envía el Pull Request al repositorio original.

8. **Participa en la revisión**:
   - Revisa los comentarios y sugerencias en tu Pull Request y haz los ajustes necesarios.

¡Gracias por tu interés en contribuir al proyecto!

## License

[MIT](https://choosealicense.com/licenses/mit/)