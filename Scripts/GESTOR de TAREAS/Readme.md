# Gestor de Tareas (Flask + React + Vite)

Este proyecto es un gestor de tareas tipo tablero Kanban desarrollado utilizando Flask para el backend y React con Vite para el frontend. La aplicación permite crear tareas, visualizarlas en un tablero dividido por estados y moverlas entre diferentes etapas del flujo de trabajo.

---

# Tecnologías utilizadas

**Backend**
- Python
- Flask
- SQLite
- Flask-CORS

**Frontend**
- React
- Vite
- JavaScript
- CSS

---

# Descripción general del sistema

El sistema se compone de dos partes principales:

**Backend:** expone una API REST que se conecta a una base de datos SQLite para almacenar las tareas.

**Frontend:** interfaz desarrollada en React que consume la API y muestra las tareas en un tablero tipo Kanban.

Cada tarea tiene un estado que determina en qué columna del tablero se muestra.

Estados de las tareas:

1. Por iniciar  
2. En proceso  
3. Terminadas  
4. En revisión  
5. Completas  

---

# Estructura del proyecto


GESTOR-DE-TAREAS

backend
│
├── app.py
└── tareas.db

frontend
│
├── src
│ ├── components
│ │ ├── TaskBoard.jsx
│ │ ├── TaskCard.jsx
│ │ └── TaskForm.jsx
│ │
│ ├── App.jsx
│ ├── App.css
│ └── main.jsx
│
├── index.html
├── package.json
└── vite.config.js


---

# Backend

El backend está desarrollado con Flask y funciona como una API que permite crear, consultar y actualizar tareas almacenadas en SQLite.

Archivo principal:


backend/app.py


---

## Conexión a la base de datos

La función encargada de establecer la conexión con SQLite es:

```python
def conectar_db():

Esta función crea la conexión y permite acceder a las columnas de las consultas utilizando nombres en lugar de índices.

Inicialización de la base de datos

La función:

def inicio_db():

crea la tabla tareas si aún no existe.

Estructura de la tabla:

id: identificador único de la tarea

titulo: nombre de la tarea

descripcion: descripción de la tarea

estado: número que representa el estado de la tarea

Obtener tareas

Ruta:

GET /tareas

Devuelve todas las tareas almacenadas en la base de datos en formato JSON.

Crear una tarea

Ruta:

POST /tareas

Recibe un JSON con los siguientes campos:

titulo
descripcion

La tarea se guarda con estado inicial 0 (Por iniciar).

Cambiar estado de una tarea

Ruta:

PUT /tareas/<id>

Actualiza el estado de una tarea específica.

Frontend

El frontend está desarrollado con React y utiliza Vite como herramienta de construcción y servidor de desarrollo.

La interfaz muestra un tablero Kanban con columnas que representan los diferentes estados de las tareas.

Componentes principales
App.jsx

Es el componente principal de la aplicación. Se encarga de renderizar el formulario para crear tareas y el tablero donde se muestran.

TaskBoard.jsx

Este componente:

obtiene las tareas desde la API

organiza las tareas según su estado

genera dinámicamente las columnas del tablero

La información se obtiene utilizando:

useEffect(() => {
 fetch("http://localhost:5000/tareas")
}, [])
TaskCard.jsx

Representa una tarea individual dentro del tablero.

Cada tarjeta muestra:

título

descripción

botones para mover la tarea entre estados

Los botones permiten:

mover la tarea al estado anterior

mover la tarea al siguiente estado

TaskForm.jsx

Este componente contiene el formulario para crear nuevas tareas.

Cuando se envía el formulario se realiza una petición:

POST /tareas

al backend para guardar la nueva tarea.

Estilos

Los estilos de la aplicación se encuentran en:

src/App.css

Incluyen:

fondo oscuro para la interfaz

columnas estilo tablero Kanban

tarjetas blancas para las tareas

botones para cambiar de estado

Ejecución del proyecto
Ejecutar el backend

Entrar en la carpeta backend:

cd backend

Instalar dependencias:

pip install flask flask-cors

Ejecutar el servidor:

python app.py

El backend quedará disponible en:

http://localhost:5000
Ejecutar el frontend

Entrar en la carpeta frontend:

cd frontend

Instalar dependencias:

npm install

Iniciar el servidor de desarrollo:

npm run dev

El frontend estará disponible en:

http://localhost:5173
Funcionamiento del sistema

El usuario crea una tarea desde el formulario.

El frontend envía los datos al backend mediante una petición POST.

El backend guarda la tarea en la base de datos SQLite.

El frontend consulta las tareas usando la API.

Las tareas se muestran en el tablero según su estado.

El usuario puede mover las tareas entre columnas usando los botones disponibles.

Posibles mejoras

Implementar autenticación de usuarios

Permitir editar y eliminar tareas

Implementar arrastrar y soltar (drag and drop)

Añadir actualización automática sin recargar la página

Mejorar la interfaz con frameworks de UI


YOHANAN CODING