# full-stack-example
Ejemplo donde una base de datos, un cliente y un servidor interactúan. El entorno de desarrollo es Python. También se ha utilizado Flask.

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

	* SQLAlchemy: Object-Relational Mapping (ORM) para Python
		* Instalación de pip: sudo apt install python-pip -y
		* pip install SQLAlchemy
	
	* Flask
		* pip install Flask



2. ¿Cuál es la función de cada fichero?

	* database_setup.pyc: genera la base de datos restaurantmenu.db
	* lotsofmenus.py: puebla restaurantmenu.db


