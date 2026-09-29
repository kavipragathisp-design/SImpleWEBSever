from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
<title>My Webserver</title>
</head>

<body>

<h1>Student Details</h1>

<p><b>Name:</b> KAVI PRAGATHI S P</p>
<p><b>Register Number:</b> 26010384</p>

<h2>Laptop Specifications</h2>

<p><b>Name:</b> Acer (TL15-53M-G2)</p>
<p><b>Processor:</b> Intel(R) Core(TM) 5 210H (2.20 GHz)</p>
<p><b>RAM:</b> 16GB</p>
<p><b>Storage:</b> 477 GB</p>
<p><b>OS:</b> Windows 11 Home Single Language</p>

</body>
</html>
"""

class myhandler (BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('',8000)
httpd = HTTPServer (server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()