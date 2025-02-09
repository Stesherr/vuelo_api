# Backend de Gestión de Reservas de Vuelos

Este proyecto es un backend construido con FastAPI para gestionar reservas de vuelos. Permmite buscar vuelos, realizar reservas, cancelarlas y administrar usuarios con autenticación JWT.

## Tecnologías Utilizadas
- FastAPI (Framework backend)
- MySQL (Base de datos)
- SQLAlchemy (ORM para interactuar con la BD)
- JWT (JSON Web Tokens) (Autenticación segura)
- Passlib (Hashing de contraseñas)
- Python 3.12.x
- Visual Studio 

## Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Stesherr/vuelo_api.git
```

### 2. Abrir el proyecto en un entorno de desarrollo de Python (Recomendado: Visual Studio)

### 3. Instalar Dependencias
```bash
pip install -r dependencias.txt
```
### 4. Crear y Configurar la Base de Datos
Ejecutar el script que esta en el archivo 'vuelo_db.sql' en MySQL

Modificar 'database.py' para conextar MySQL:
```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://usuario:contraseña@localhost/reservas_vuelos"
```
Reemplazar usuario y contraseña por las credenciales de tu base de datos.

Cargar Datos de Vuelos a la Base de Datos
```bash
python cargar_datos.py
```

### 5. Ejecutar el Servidor
```bash
uvicorn main:app --reload
```
El backend estará disponible en 'http://127.0.0.1:8000'

## Endpoints Disponibles

### **Autenticación**

- POST /api/usuarios → Registrar un usuario

- POST /token → Iniciar sesión (JWT)

### **Gestión de Vuelos**

- GET /api/vuelos?origen=XXX&destino=YYY&fecha=AAAA-MM-DD → Buscar vuelos

### **Reservas**

- POST /api/reservas → Reservar un vuelo (requiere JWT)

- DELETE /api/reservas/{id} → Cancelar una reserva (requiere JWT)

- GET /api/usuarios/{usuario_id}/reservas → Listar reservas de un usuario (requiere JWT)

## Notas Adicionales
- Asegúrate de que MySQL esté corriendo antes de ejecutar el proyecto.
- La base de datos no tiene ningun registro de usuario o reserva previo.