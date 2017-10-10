# Restaurant manager
Ejemplo donde una base de datos, un cliente y un servidor interactúan. El entorno de desarrollo es Python.

## Empezando
Instrucciones para que el usuario pueda tener el sistema corriendo en su máquina local.

### Prerrequisitos e instalación
El sistema se ha desarrollado en un entorno Ubuntu, por tanto éste es el sistema operativo más idoneo para ejecutarlo. Es necesario tener instalado en el sistema: python, pip, SQLAlchemy y Flask:

1. Python
    apt-get install -y python python-pip


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


