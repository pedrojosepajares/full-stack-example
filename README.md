# full-stack-example
Ejemplo donde una base de datos, un cliente y un servidor interactúan. El entorno de desarrollo es Python. También se ha utilizado Flask.

1. ¿Qué necesito antes de empezar?

	1. SQLite: Base de datos SQL simple
		1. Decargar "sqlite-autoconf-3200100.tar.gz" desde https://www.sqlite.org/download.html
		2. tar xvfz sqlite-autoconf-3200100.tar.gz
		3. cd sqlite-autoconf-3200100/
		4. ./configure
		5. make
		6. sudo make install
		7. cd ..
		8. rm -rf  sqlite-autoconf-3200100 sqlite-autoconf-3200100.tar.gz

	2. Python: instalado por defecto en las distribuciones de Ubuntu

	3. SQLAlchemy: Object-Relational Mapping (ORM) para Python
		- Instalación de pip: sudo apt install python-pip -y
		- pip install SQLAlchemy



2. ¿Cuál es la función de cada fichero?

	1. database_setup.pyc: genera la base da datos restaurantmenu.db
	2. lotsofmenus.py: puebla restaurantmenu.db


