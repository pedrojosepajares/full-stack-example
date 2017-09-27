# full-stack-example
Ejemplo donde una base de datos, un cliente y un servidor interactúan. El entorno de desarrollo es Python. También se ha utilizado Flask.

############################
Prerrequisitos:

1. SQLite: Base de datos SQL simple
	- Decargar "sqlite-autoconf-3200100.tar.gz" desde https://www.sqlite.org/download.html
	- tar xvfz sqlite-autoconf-3200100.tar.gz
	- cd sqlite-autoconf-3200100/
	- ./configure
	- make
	- sudo make install
	- cd ..
	- rm -rf  sqlite-autoconf-3200100 sqlite-autoconf-3200100.tar.gz

2. Python: instalado por defecto en las distribuciones de Ubuntu

3. SQLAlchemy: Object-Relational Mapping (ORM) para Python
	- Instalación de pip: sudo apt install python-pip -y
	- pip install SQLAlchemy

############################


"database_setup.pyc" genera una base de datos y "lotsofmenus.py" la puebla.


