import auth
import task_manager
import logging
from datetime import datetime
# Configuración del log
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    print("Bienvenido al Gestor de Tareas")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    if auth.login(username, password):
        logging.info(f"Usuario {username} ha iniciado sesión.")
        while True:
            print("\n1. Añadir Tarea")
            print("\n2. Ver Tareas")
            print("\n3. Actualizar Tarea")
            print("\n4. Eliminar Tarea")
            print("\n5. Archivar Tareas Completadas")
            print("\n6. Ver Tareas Archivadas")
            print("\n7. Salir")
            option = input("Seleccione una opción: ")

            if option == "1":
                title = input("Título de la tarea: ")
                description = input("Descripción: ")
                due_date = input("Fecha de vencimiento (YYYY-MM-DD): ")
                label = input("Etiqueta: ")
                task_manager.add_task(title, description, due_date, label)
                logging.info(f"Tarea '{title}' añadida por {username}.")
            
            elif option == "2":
                status = input("Filtrar por estado (pending, in_progress, completed) o presione Enter: ")
                label = input("Filtrar por etiqueta o presione Enter: ")
                due_date = input("Filtrar por fecha de vencimiento antes de (YYYY-MM-DD) o presione Enter: ")

                # Validar formato de fecha
                try:
                    if due_date:
                        due_date = datetime.strptime(due_date, '%Y-%m-%d')
                    else:
                        due_date = None
                except ValueError:
                    print("Formato de fecha inválido, use YYYY-MM-DD.")
                    due_date = None

                task_manager.list_tasks(status, label, due_date)

            
            elif option == "3":
                title = input("Título de la tarea a actualizar: ")
                new_status = input("Nuevo estado (pending, in_progress, completed) o presione Enter: ")
                new_due_date = input("Nueva fecha de vencimiento (YYYY-MM-DD) o presione Enter: ")
                new_label = input("Nueva etiqueta o presione Enter: ")
                task_manager.update_task(title, new_status, new_due_date, new_label)
                logging.info(f"Tarea '{title}' actualizada por {username}.")
            
            elif option == "4":
                title = input("Título de la tarea a eliminar: ")
                task_manager.delete_task(title)
                logging.info(f"Tarea '{title}' eliminada por {username}.")
            
            elif option == "5":
                task_manager.archive_completed_tasks()
                logging.info(f"Tareas completadas archivadas por {username}.")
            
            elif option == "6":
                task_manager.list_archived_tasks()
            elif option == "7":
                print("Cerrando sesión...")
                logging.info(f"Usuario {username} cerró sesión.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    else:
        logging.warning(f"Intento de inicio de sesión fallido para usuario {username}.")
        print("Nombre de usuario o contraseña incorrectos.")

if __name__ == "__main__":
    while True:
        main()
