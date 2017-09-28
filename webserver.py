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

                # Obtención de todos los restaurantes
                restaurants = session.query(Restaurant).all()
                
                # Generacion y envio de la salida
                output = ""
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name + "<br>"
                    output += "<a href='/" + restaurant.id + "/edit'>Edit</a><br>"
                    output += "<a href='/" + restaurant.id + "/delete'>Delete</a><br><br>"
                output += "<a href='/new'>Nuevo restaurante</a><br>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            # Adición
            if self.path.endswith("/new"):
                # Peticion GET gestionada con exito
                self.send_response(200)
                # Con la cabecera se indica que se va a responder con texto
                self.send_header('Content-type', 'text/html')
                # Se envia una linea en blanco para indicar el fin del envio de
                #cabeceras
                self.end_headers()

                


                return
            

            # Edición           
            if self.path.endswith("/edit"):
                # Peticion GET gestionada con exito
                self.send_response(200)
                # Con la cabecera se indica que se va a responder con texto
                self.send_header('Content-type', 'text/html')
                # Se envia una linea en blanco para indicar el fin del envio de
                #cabeceras
                self.end_headers()



        except IOError:
            print ("Error")

def do_POST(self):
    try:
        # Respuesta satisfactoria a POST
        self.send_response(301)
        self.end_headers()

        # Lectura de la informacion del formulario
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            messagecontent = fields.get('message')

        print messagecontent
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