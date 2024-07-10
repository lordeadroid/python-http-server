from server import Server
from http.server import HTTPServer

def main():
  PORT = 8000
  server = HTTPServer(("localhost", PORT), Server)
  print("Started listening on PORT:", PORT)
  server.serve_forever()

main()
