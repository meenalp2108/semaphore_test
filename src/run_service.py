from gevent.pywsgi import WSGIServer
from analysis_service.app import app

http_server = WSGIServer(('10.1.0.4',4000), app)
http_server.serve_forever()
