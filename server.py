import os
import http.server
import socketserver
import dateparser



from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        str = self.path
        slug = str.replace('https://datetimeparse-wm2zb.ondigitalocean.app/','')
        msg = dateparser.parse(slug)
        
        self.wfile.write(msg)


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
