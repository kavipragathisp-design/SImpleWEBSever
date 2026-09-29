from http.server import HTTPServer, SimpleHTTPRequestHandler


class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        return super().do_GET()


HOST = "127.0.0.1"
PORT = 8000

server_address = (HOST, PORT)

http_server = HTTPServer(
    server_address,
    CustomRequestHandler
)

print(f"Server started successfully!")
print(f"Open your browser and visit: http://{HOST}:{PORT}")
print("Press Ctrl+C to stop the server.")

