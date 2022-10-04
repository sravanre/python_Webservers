import http.server
import socketserver

PORT = 8999

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Good moring sravan , we are serving at port", PORT)
    httpd.serve_forever()