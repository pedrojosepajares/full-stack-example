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

## Ejecutando la aplicación
 Para ejecutar la aplición es necesario interpretar el programa "restaurantmanager.py"
 ```sh
python restaurantmanager.py
```
Una vez introducida la orden, el servidor comienza a esperar conexiones a través del puerto 5000. El usuario puede acceder a la interfaz de gestión de restaurantes y menús a través de la dirección http://localhost:5000/restaurants/ .

Para ejecutar la aplicación desde Docker, hay que generar un contenedor a partir de la imagen generada o descargada
 ```sh
docker run -i -t -p 5000:5000 restaurant-manager
```
Igualmente, el usuario puede acceder a la interfaz del sistema visitando la dirección http://localhost:5000/restaurants/ .



1. ¿Qué necesito antes de empezar?

	* SQLite: Base de datos SQL simple
		* Decargar "sqlite-autoconf-3200100.tar.gz" desde https://www.sqlite.org/download.html
		* tar xvfz sqlite-autoconf-3200100.tar.gz
		* cd sqlite-autoconf-3200100/
		* ./configure
		* make
		* sudo make install
		* cd ..
		* rm -rf  sqlite-autoconf-3200100 sqlite-autoconf-3200100.tar.gz

	* Python: instalado por defecto en las distribuciones de Ubuntu

	* Pip:
		* Instalación de pip: sudo apt install python-pip -y 

	* SQLAlchemy: Object-Relational Mapping (ORM) para Python
		* pip install SQLAlchemy
	
	* Flask
		* pip install Flask


2. Directorios

	* Templates : templates html utilizados por Flask.
	* Static : Flask comprueba en este directorio si existen ficheros CSS, JavaScript, de audio o de sonido para incluirlos en el proyecto.

3. ¿Cuál es la función de cada fichero?

	* database_setup.pyc: genera la base de datos restaurantmenu.db
	* lotsofmenus.py: puebla restaurantmenu.db


