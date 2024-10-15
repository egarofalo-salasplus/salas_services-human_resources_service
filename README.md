# Human Resources Service

El proyecto **Human Resources Service** es una aplicación Django diseñada para gestionar y organizar información de recursos humanos en una empresa. Este proyecto está dividido en varias aplicaciones específicas que representan áreas fundamentales como empleados, empresas, departamentos y registros. Cada aplicación contiene modelos que se encargan de almacenar la información relacionada y su administración está disponible en el panel de administración de Django.

## Aplicaciones

### 1. Companies
La aplicación **companies** se encarga de gestionar la información de las empresas y sus direcciones. Los modelos principales son:

- **Company**: Representa una empresa dentro de la organización.
- **Address**: Contiene la información de la dirección de una empresa.

### 2. Employees
La aplicación **employees** gestiona la información relacionada con los empleados. Los modelos principales son:

- **Employee**: Contiene información detallada de cada empleado, como nombre, dirección, empresa, etc.
- **JobHistory**: Historial de puestos de trabajo del empleado.
- **JobPosition**: Información sobre el puesto de trabajo que ocupa un empleado.
- **Area**: Áreas dentro de un departamento.
- **WorkCenter**: Centros de trabajo donde operan los empleados.

### 3. Departments
La aplicación **departments** se encarga de gestionar los departamentos de la organización. El modelo principal es:

- **Department**: Representa un departamento dentro de la empresa, asociado a una compañía específica.

### 4. Records
La aplicación **records** almacena información sobre la actividad de los empleados. Los modelos principales son:

- **TimeRecord**: Registros de tiempos de fichaje de los empleados.
- **Allocation**: Imputaciones de tiempo y tareas realizadas por los empleados.
- **EmployeeLeave**: Información sobre bajas de empleados.
- **Evaluation**: Evaluaciones de desempeño de los empleados.

## Administración
El proyecto cuenta con una interfaz de administración personalizada donde se han realizado las siguientes mejoras:

- En la vista de administración de **departments**, se muestra el nombre del departamento y el nombre de la empresa asociada, en lugar de mostrar solo el ID de la compañía.
- En la vista de edición de departamentos, el nombre de las empresas se muestra correctamente en la lista desplegable, haciendo que la experiencia de edición sea más intuitiva.
- Se han agregado vistas y acciones personalizadas, como exportar empleados a CSV, que facilitan la gestión de la información.

## Requisitos de Instalación
- Python 3.8+
- Django
- SQL Server (Base de datos utilizada)
- Bibliotecas necesarias: `django-pyodbc-azure`, `psycopg2` (si estás usando PostgreSQL en lugar de SQL Server)

Puedes instalar los requerimientos utilizando el archivo `requirements.txt`:
```sh
pip install -r requirements.txt
```

## Configuración de Base de Datos
Este proyecto está configurado para utilizar SQL Server como base de datos principal. Los parámetros de conexión a la base de datos se gestionan mediante variables de entorno para mayor seguridad y flexibilidad. Puedes configurar las siguientes variables de entorno:

- `DB_NAME`: Nombre de la base de datos.
- `DB_USER`: Usuario de la base de datos.
- `DB_PASSWORD`: Contraseña del usuario.
- `DB_HOST`: Dirección del host de la base de datos.
- `DB_PORT`: Puerto de la base de datos (opcional).

Asegúrate de que estas variables estén configuradas correctamente antes de ejecutar la aplicación.

## Uso
Para comenzar a usar la aplicación, primero realiza las migraciones necesarias:
```sh
python manage.py makemigrations
python manage.py migrate
```
Luego, puedes crear un superusuario para acceder al panel de administración:
```sh
python manage.py createsuperuser
```
Finalmente, ejecuta el servidor:
```sh
python manage.py runserver
```
Accede al panel de administración desde `http://127.0.0.1:8000/admin/`.

## Estructura del Proyecto
El proyecto está estructurado en varias aplicaciones para dividir la lógica de negocio de una forma clara y ordenada:

- **companies**: Gestión de empresas y direcciones.
- **employees**: Gestión de empleados, historial de puestos y centros de trabajo.
- **departments**: Gestión de departamentos de la empresa.
- **records**: Gestión de fichajes, imputaciones, bajas y evaluaciones de empleados.

## Contribución
Si deseas contribuir al proyecto, puedes clonar el repositorio y crear tus propias ramas de desarrollo. Se aceptan pull requests para mejoras y correcciones.

## Contacto
Para cualquier duda o consulta, puedes contactar al desarrollador principal o revisar la documentación del proyecto.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Puedes ver más detalles en el archivo `LICENSE` adjunto.