# Servidor HTTP
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# Obtencion de informacion en formularios
import cgi
# Gestion de DB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

class webserverHandler(BaseHTTPRequestHandler):
    # Genera una nueva sesion para interactuar con la base
    # de datos restaurantmenu.db
    def newSession(self):
        engine = create_engine('sqlite:///restaurantmenu.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind = engine)
        return DBSession()
    

    def do_GET(self):
        try:
            #Nueva sesion en la DB y lectura de restaurantes
            session = self.newSession()

            # Menu principal
            if self.path.endswith("/restaurants"):
                # Peticion GET gestionada con exito
                self.send_response(200)
                # Con la cabecera se indica que se va a responder con texto
                self.send_header('Content-type', 'text/html')
                # Se envia una linea en blanco para indicar el fin del envio de
                #cabeceras
                self.end_headers()

                # Obtencion de todos los restaurantes
                restaurants = session.query(Restaurant).all()
                
                # Generacion y envio de la salida
                output = ""
                output += "<html><body><h1>Restaurants</h1>"
                output += "<br><a href='/new'>Nuevo restaurante</a><br><br>"
                for restaurant in restaurants:
                    output += restaurant.name + "<br>"
                    output += "<a href='/" + str(restaurant.id) + "/edit'>Edit</a><br>"
                    output += "<a href='/" + str(restaurant.id) + "/delete'>Delete</a><br><br>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            # Adicion
            if self.path.endswith("/new"):
                # Peticion GET gestionada con exito
                self.send_response(200)
                # Con la cabecera se indica que se va a responder con texto
                self.send_header('Content-type', 'text/html')
                # Se envia una linea en blanco para indicar el fin del envio de
                #cabeceras
                self.end_headers()

                #Generacion y envio de la salida
                output = ""
                output += "<html><body>"
                output += "<form method='POST' enctype='multipart/form-data' action='restaurants'>"
                output += "New restaurant name<br>"
                output += "<input name='name' type='text'>"
                output += "<input type='submit' value='Submit'>"
                output += "</form>"
                self.wfile.write(output)
                return
            

            # Borrado          
            if self.path.endswith("/delete"):
                # Peticion GET gestionada con exito
                self.send_response(200)
                # Con la cabecera se indica que se va a responder con texto
                self.send_header('Content-type', 'text/html')
                # Se envia una linea en blanco para indicar el fin del envio de
                #cabeceras
                self.end_headers()

                #Nombre del restaurante
                path_parts = self.path.split('/') # Separacin del path
                restaurant_id = path_parts[1] # id del restaurantes
                restaurant = session.query(Restaurant).filter_by(id = restaurant_id) # restaurante que coincide con id
                name = restaurant[0].name # nombre del restaurante

                #Generacion y envio de la salida
                output = ""
                output += "<html><body>"
                output += "<form method='POST' enctype='multipart/form-data' action='"
                output += self.path + "'>"
                output += "You are going to delete " + name + ". Are you sure?<br>"
                output += "<input type='submit' value='Submit'>"
                output += "</form>"
                self.wfile.write(output)
                return

            # Edicion
            if self.path.endswith("/edit"):
                # Peticion GET gestionada con exito
                self.send_response(200)
                # Con la cabecera se indica que se va a responder con texto
                self.send_header('Content-type', 'text/html')
                # Se envia una linea en blanco para indicar el fin del envio de
                #cabeceras
                self.end_headers()

                #Generacion y envio de la salida
                output = ""
                output += "<html><body>"
                output += "<form method='POST' enctype='multipart/form-data' action='edit'>"
                output += "Edit restaurant<br>"
                output += "<input name='name' type='text'>"
                output += "<input type='submit' value='Submit'>"
                output += "</form>"
                self.wfile.write(output)
                return
        
        
        except IOError:
            print ("Error")

    def do_POST(self):
        try:
            #Nueva sesion en la DB y lectura de restaurantes
            session = self.newSession()

            # Adicion
            if self.path.endswith("/restaurants"):
                # Respuesta satisfactoria a POST
                self.send_response(301)
                self.end_headers()
                # Lectura de la informacion del formulario
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                
                # Adicion del restaurante a la DB 
                restaurant = Restaurant(name = (fields.get('name'))[0])
                session.add(restaurant)
                session.commit()

                # Obtencion de todos los restaurantes
                restaurants = session.query(Restaurant).all()
                # Generacion y envio de la salida
                output = ""
                output += "<html><body><h1>Restaurants</h1>"
                output += "<br><a href='/new'>Nuevo restaurante</a><br><br>"
                for restaurant in restaurants:
                    output += restaurant.name + "<br>"
                    output += "<a href='/" + str(restaurant.id) + "/edit'>Edit</a><br>"
                    output += "<a href='/" + str(restaurant.id) + "/delete'>Delete</a><br><br>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            #Borrado
            if self.path.endswith("/delete"):
                # Respuesta satisfactoria a POST
                self.send_response(301)
                self.end_headers()
                # Lectura de la informacion del formulario
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':                
                    #Peticion del restasurante a la DB y borrado
                    path_parts = self.path.split('/') # Separacin del path
                    restaurant_id = path_parts[1] # id del restaurantes
                    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one() # restaurante que coincide con id
                    session.delete(restaurant)
                    session.commit()
                
                print "Alcanzo la salida"

                # Obtencion de todos los restaurantes
                restaurants = session.query(Restaurant).all()
                # Generacion y envio de la salida
                output = ""
                output += "<html><body><h1>Restaurants</h1>"
                output += "<br><a href='/new'>Nuevo restaurante</a><br><br>"
                for restaurant in restaurants:
                    output += restaurant.name + "<br>"
                    output += "<a href='/" + str(restaurant.id) + "/edit'>Edit</a><br>"
                    output += "<a href='/" + str(restaurant.id) + "/delete'>Delete</a><br><br>"
                output += "</body></html>"
                self.wfile.write(output)
                self.path = "/restaurants"
                print output
                return
            
            #Edicion
            if self.path.endswith("/edit"):

                print "POST en edit"

                # Respuesta satisfactoria a POST
                self.send_response(301)
                self.end_headers()
                # Lectura de la informacion del formulario
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    # Obtencion del nombre a partir del formulario
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    name = (fields.get('name'))[0]
                    # Peticion del restaurante a la DB
                    path_parts = self.path.split('/') # Separacin del path
                    restaurant_id = path_parts[1] # id del restaurantes
                    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one() # restaurante que coincide con id
                    # Cambio de nombre y actualizacion en la DB
                    restaurant.name = name
                    session.add(restaurant)
                    session.commit()
                return

        except:
            pass

def main():

    try:
        port = 9999
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()
    
    # El servidor se detiene cuando el usuario presiona Ctrl+C
    except KeyboardInterrupt:
        print "Stopping web server..."
        server.socket.close()


if __name__ == '__main__':
    main()