import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    def __get_xtml(self):
        with open("5/sidebars/index.html", 'rb') as f:
            self.wfile.write(f.read())

    def do_GET(self):
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "application/json") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes("{'message': 'OK'}", "utf-8")) # Тело ответа

if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")