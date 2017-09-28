from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                # Peticion GET gestionada con exito
                self.send_response(200)
                # Con la cabecera se indica que se va a responder con texto
                self.send_header('Content-type', 'text/html')
                # Se envia una linea en blanco para indicar el fin del envio de
                #cabeceras
                self.end_headers()

                # Generacion y envio de la salida
                output = ""
                output += "<html><body>Hello!</body></html>"
                self.wfile.write(output)
                print output

        except IOError:
            print ("Error")

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