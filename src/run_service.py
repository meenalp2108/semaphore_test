from gevent.pywsgi import WSGIServer
from analysis_service.app import app

http_server = WSGIServer(('172.16.55.145',4000), app)
http_server.serve_forever()
