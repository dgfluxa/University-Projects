# Backend Proyecto Grupo 2

## Requisitos y pasos generales
- Python 3.8 a 3.6 (python -m virtualenv -p="C:\Users\Benja\AppData\Local\Programs\Python\Python38\python.exe" ./venv Para crear con version de python especifica) 
- Instalar Postgresql (pgAdmin opcional)
- Crear archivo .env (Con los datos en carpeta proyectogrupo2, y con la clave maestra de ustedes de psql)
- Crear base de datos en PSQL llamada "proyectogrupo2"
- Crear .venv  con python 3.8 a 3.6 (checkear con python --version dentro del venv)
- Crear migraciones y migrar

## Crear un entorno virtual

Se recomienda crear un entorno virtual usando 'virtualenv', para esto nos ubicamos en la carpeta 'backend' y ejecutamos los siguientes comandos.


### Instalar virtualenv:

```
pip install virtualenv
```

### Para crear un entorno virtual:

```
virtualenv venv
```

### Para activar el entorno virtual:

```
venv\Scripts\activate
```
### Alternativa en windows 10:

```
cd backend
python -m venv ./venv
.\venv\Scripts\activate
pip install --upgrade -r requirements.txt
```

Se recomienda activar el entorno virtual cada vez que se quiera correr la app.

## Para correr la app los comandos a seguir son:

### Instalar Librerías:

```
pip install --upgrade -r requirements.txt
```

### Crear migraciones:

```
python manage.py makemigrations
```

### Correr migraciones:

```
python manage.py migrate
```

### Mostrar migraciones hechas y pendientes:

```
python manage.py showmigrations
```

### Correr app:

```
python manage.py runserver 
python manage.py runserver --noreload
```
Se recomienda usar con --noreload, ya que sirve para que el updater funcione bien (sin duplicados). 

### Si se instalaron nuevas librerías correr el comando:

```
pip freeze > requirements.txt
```

Este comando copiará todas las librerias en el entorno virtual y las pegará en el archivo 'requirements.txt'. Esto es para que todos tengamos las mismas librerías.

## Servidor
### Comenzar server
```
sudo systemctl enable gunicorn.socket
sudo systemctl start gunicorn.socket
```

### Reiniciar server
```
sudo systemctl restart gunicorn
```

### Parar server
```
sudo systemctl disable gunicorn.socket
sudo systemctl stop gunicorn.socket
```

### Ver logs
```
sudo journalctl -e -f -u gunicorn
```