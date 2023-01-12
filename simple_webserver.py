
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>"
                               "SEC</title></head>", "utf-8"))
        self.wfile.write(bytes("<body bgcolor='#12E4CD'><b>Welcome to Saveetha Engineering College</br></b>"
                               "The Top Web Application Frameworks are:</br>"
                               "1. Angular JS</br>"
                               "2. React JS</br>"
                               "3. JavaScript</br>"
                               "4. Vue JS</br>"
                               "5. Django</br>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")