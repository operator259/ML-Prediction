import http.server
import socketserver

PORT = 8000
DIRECTORY = "http_directory"  # Folder Name to Serve Content

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving from '{DIRECTORY}' on port {PORT}")
    httpd.serve_forever()