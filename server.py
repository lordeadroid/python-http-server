from http.server import BaseHTTPRequestHandler
import json

class Server(BaseHTTPRequestHandler):
  def do_GET(self):
    data = {"message": "hello world"}
    self.send_response(200)
    self.send_header("Content-type","application/json")
    self.end_headers()
    self.wfile.write(json.dumps(data).encode("utf-8"))