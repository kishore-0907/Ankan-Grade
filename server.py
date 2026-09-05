import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        req_path = self.path.split('?')[0].rstrip('/')
        if req_path in ('/login', 'login'):
            self.path = '/login.html'
        elif req_path in ('/dashboard', 'dashboard', ''):
            self.path = '/index.html'
        return super().do_GET()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving Nyaya Evaluator at http://localhost:{PORT} from {DIRECTORY}")
        sys.stdout.flush()
        httpd.serve_forever()
