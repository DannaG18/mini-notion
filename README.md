# Mini-Notion

Mini-Notion es una aplicación simple de gestión de tareas diseñada para organizar actividades y proyectos de manera eficiente. Este proyecto está inspirado en Notion, ofreciendo funcionalidades básicas para crear, editar, y administrar tareas.

![image-20241217002339668](C:\Users\danna\AppData\Roaming\Typora\typora-user-images\image-20241217002339668.png)

## Características

- **Gestión de tareas**: Crear, actualizar, y eliminar tareas fácilmente.
- **Importación y exportación archivos JSON**: Transforma información a este formato.
- **Interfaz de usuario amigable**: Una UI simple para interactuar con las tareas.
- **Persistencia de datos**: Uso de SQLite para almacenar las tareas de manera local.
- **Control de versiones**: Configuración de un repositorio Git para rastrear cambios en el proyecto.

![image-20241217002407832](C:\Users\danna\AppData\Roaming\Typora\typora-user-images\image-20241217002407832.png)

![image-20241217002420029](C:\Users\danna\AppData\Roaming\Typora\typora-user-images\image-20241217002420029.png)

## Estructura del Proyecto

El proyecto incluye los siguientes archivos y carpetas principales:

- **app/**: Contiene los archivos fuente de la aplicación.
  - **controllers/**: Maneja la lógica de control de la aplicación.
  - **models/**: Define las estructuras de datos y conecta con la base de datos.
  - **utils/**: Contiene utilidades y funciones auxiliares.
  - **views/**: Maneja la interfaz de usuario y las interacciones.
- **tasks.db**: Base de datos SQLite para almacenar tareas.
- **requirements.txt**: Lista de dependencias del proyecto.
- **README.md:** Documentación del proyecto.

## Requisitos Previos

Asegúrate de tener instalados los siguientes requisitos:

- Python 3.8 o superior.
- pip (gestor de paquetes de Python).

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <URL del repositorio>
   ```
   
2. Navega al directorio del proyecto:
   ```bash
   cd mini-notion
   ```
   
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```
2. Abre tu navegador y ve a `http://localhost:8501` para usar la aplicación.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto.
- **Streamlit**: Framework para construir interfaces interactivas.
- **SQLite**: Base de datos utilizada para el almacenamiento de tareas.
- **SQLAlchemy**: ORM utilizado para interactuar con la base de datos.

## Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección:
   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commits:
   ```bash
   git commit -m "Añadir nueva funcionalidad"
   ```
4. Haz un push a tu rama:
   ```bash
   git push origin mi-nueva-funcionalidad
   ```
5. Abre un pull request.



---

**Autor:** Danna G. Alvarez

Si tienes preguntas o sugerencias, no dudes en contactarme.