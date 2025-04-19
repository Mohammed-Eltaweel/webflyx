from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Content-Security-Policy", "frame-ancestors 'self' https://sandbox-buy.paddle.com")
        super().end_headers()



if __name__ == "__main__":
    server_address = ("", 5000)
    httpd = HTTPServer(server_address, CustomHandler)
    print("Serving on port 5000...")
    httpd.serve_forever()
