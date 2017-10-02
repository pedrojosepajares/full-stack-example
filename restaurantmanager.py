from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Sesion para interactuar con la base de datos
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

############## RUTAS ##############

# Listar restuarantes
@app.route('/')
@app.route('/restaurants/')
def restaurantList():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurantlist.html', restaurants = restaurants)

# Nuevo restaurante
@app.route('/restaurants/new/', methods = ['GET', 'POST'])
def restaurantNew():
    if request.method == 'GET':
        return render_template('restaurantnew.html')
    if request.method == 'POST':
        restaurant = Restaurant(name = request.form['name'])
        session.add(restaurant)
        session.commit()
        print "Added restaurant " + restaurant.name
        return redirect(url_for('restaurantList'))

# Editar restaurante
@app.route('/restaurants/<int:restaurant_id>/edit/', methods = ['GET', 'POST'])
def restaurantEdit(restaurant_id):
    if request.method == 'GET':
        return render_template('restaurantedit.html', restaurant_id=restaurant_id)
    if request.method == 'POST':
        restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
        restaurant.name = request.form['name']
        session.add(restaurant)
        session.commit()
        print "Edited restaurant " + restaurant.name
        return redirect(url_for('restaurantList'))

# Borrar restaurante
@app.route('/restaurants/<int:restaurant_id>/delete/', methods = ['GET', 'POST'])
def restaurantDelete(restaurant_id):
    if request.method == 'GET':
        return render_template('restaurantdelete.html', restaurant_id=restaurant_id)
    if request.method == 'POST':
        restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
        session.delete(restaurant)
        session.commit()
        return redirect(url_for('restaurantList'))


# Listar menus de un restaurante
@app.route('/restaura      nts/<int:restaurant_id>/')
def menuList(restaurant_id):
    return "Listar menu de un restaurante"

# Nuevo item en el menu de un restaurante
@app.route('/restaurants/<int:restaurant_id>/new/')
def menuNew(restaurant_id):
    return "Nuevo menu en un restaurante"

# Editar item en el menu de un restaurante
@app.route('/restaurants/<int:restaurant_id>/<int:item_id>/edit/')
def menuEdit(restaurant_id, item_id):
    return "Editar menu de un restaurante"

# Borrar item en el menu de un restaurante
@app.route('/restaurants/<int:restaurant_id>/<int:item_id>/delete/')
def menuDelete(restaurant_id, item_id):
    return "Eliminar item del menu de un restaurante"



############## FUNCION PRINCIPAL ##############
if __name__ == '__main__':
    app.secret_key = "secret_key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)