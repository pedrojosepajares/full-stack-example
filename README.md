# Restaurant manager
Ejemplo de sistema para la gestión de un conjunto de restaurantes con sus menús donde una base de datos, un cliente y un servidor interactúan. El entorno de desarrollo es Python.

## Empezando
Instrucciones para que el usuario pueda tener el sistema corriendo en su máquina local.

### Prerrequisitos
El sistema se ha desarrollado en un entorno Ubuntu, por tanto éste es el sistema operativo más idoneo para ejecutarlo. Es necesario tener instalado en el sistema: Python, Pip, SQLAlchemy y Flask:

1. Python y Pip
	```sh
	apt-get install -y python python-pip
	```
2. SQLAlchemy y Flask
	```sh
	pipi pip install SQLAlchemy Flask
	```
Si el usuario desea cambiar el esquema de la base de datos, tambíen es necesario tener instalado [SQLite](https://www.sqlite.org/), siguiendo las instrucciones de su página web.

La aplicación se puede ejecutar de una forma muy sencilla utilizando [Docker](https://www.docker.com/). Docker se puede instalar siguiendo las instrucciones de [este](https://www.muylinux.com/2016/04/19/tutorial-docker) sencillo tutorial o siguiendo las instrucciones de su sitio web oficial.

### Instalación
Para ejecutar el programa con Python no es necesario realizar instalación. Para ejecutarlo desde un contenedor Docker es necesario contruir la imagen a partir del fichero Dockerfile que se encuentra en el directorio "Docker"
	
```sh
docker build -t restaurant-manager ./Docker/
```

O también, el usuario puede descargar la imagen preconstruida desde mi [repositorio DockerHub](https://hub.docker.com/r/pedrojosepajares/)
```sh
docker pull pedrojosepajares/restaurant-manager
```

## Ejecutando la aplicación
 Para ejecutar la aplición es necesario interpretar el programa "restaurantmanager.py"
 ```sh
python restaurantmanager.py
```
Una vez introducida la orden, el servidor comienza a esperar conexiones a través del puerto 5000. El usuario puede acceder a la interfaz de gestión de restaurantes y menús a través de la dirección http://localhost:5000/restaurants/ .

Para ejecutar la aplicación desde Docker, hay que generar un contenedor a partir de la imagen generada
 ```sh
docker run -i -t -p 5000:5000 restaurant-manager
```
o si la imagen se ha descargado desde mi repositorio
 ```sh
docker run -i -t -p 5000:5000 pedrojosepajares/restaurant-manager
```

Igualmente, el usuario puede acceder a la interfaz del sistema visitando la dirección http://localhost:5000/restaurants/ .

## Desarrollo
El proyecto ha sido realizado utlizando el apoyo proporcionado por los cursos de [Udacity](https://www.udacity.com/)

## Construido con
Las tecnologías utilizadas para la construcción de este proyecto son:
* [Python](https://www.python.org/)
* [SQLite](https://www.sqlite.org/) 
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Flask](http://flask.pocoo.org/)
* [Docker](https://www.docker.com/)

## Autores
* Pedro José Pajares Ramírez
