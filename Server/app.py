from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from OpenSSL import SSL
from Utilities import database
from routes import mod

socketio = SocketIO()


def create_app(debug=False):

    context = SSL.Context(SSL.SSLv23_METHOD)
    context.use_privatekey_file('server.key')
    context.use_certificate_file('server.crt')

    app = Flask(__name__)
    CORS(app)
    app.debug = debug
    app.register_blueprint(mod)
    socketio.init_app(app)
    database.init()
    return app, context
