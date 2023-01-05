from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<title>SIMPLE WEBSERVER</title>
</head>
<body>
<h1>WELCOME TO MY FIRST WEBSERVER</h1>
</body>
</html>
"""

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())


server_address = ('',80)
httpd = HTTPServer(server_address, HelloHandler)
print("my server is running...")
httpd.serve_forever()