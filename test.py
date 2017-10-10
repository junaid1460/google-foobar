import http.server as server
import socketserver as socket
from sys import argv
port = None
try:
    port = int(argv[1])
except:
    port = 9999
class Handler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # print(sir(self.request))
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"get")
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"post")
try:
    socket.TCPServer(('', port), Handler).serve_forever()
except:
    pass