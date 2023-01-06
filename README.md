# Developing a Simple Webserver

# AIM:

Name:ROHIT JAIN .D
Ref:22005894
Dept:Artificial Intelligence and Data Science.
To develop a simple webserver to serve html programming pages.

## DESIGN STEPS:

### Step 1:

HTML content creation is done

### Step 2:

Design of webserver workflow

### Step 3:

Implementation using Python code

### Step 4:

Serving the HTML pages.

### Step 5:

Testing the webserver

## PROGRAM:  
```
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
```

## OUTPUT:
SERVER SIDE OUTPUT

![Screenshot from 2023-01-06 12-45-31](https://user-images.githubusercontent.com/118707073/210950787-0f804581-294b-4d8c-9b72-bf7d274e19d7.png)

CLIENT SIDE OUTPUT
![Screenshot from 2023-01-06 12-56-10](https://user-images.githubusercontent.com/118707073/210951628-d7317212-b198-444b-8fe2-8528eeb69af6.png)

## RESULT:
The program for implementing simple web is executed succesfully.
