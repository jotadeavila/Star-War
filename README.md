# Star Wars GraphQL API

API GraphQL en Django sobre Star Wars


# Tecnologías

- Python 3.14 / Django 6.0
- GraphQL con Graphene-Django
- Relay para paginación
- MySQL 8.0 con Docker
- pytest para tests

# Requisitos

- Docker & Docker Compose

# Instalación

- Clonar repositorio

# Levantar api con Docker
docker-compose up --build -d

# Acceder a la API
# GraphQL Playground: http://localhost:8000/graphql/
# Adminer (DB): http://localhost:8090


## Instalación Manual (Desarrollo)

# 1. Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Levantar MySQL con Docker
docker-compose up -d db adminer

# 4. Migraciones y datos
python manage.py migrate
python manage.py load_data

# 5. Iniciar servidor
python manage.py runserver