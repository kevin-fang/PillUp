from flask import Flask
import database
from flask_socketio import SocketIO
from routes import mod
from flask_cors import CORS

socketio = SocketIO()


def create_app(debug=False):

    app = Flask(__name__)
    CORS(app)
    app.debug = debug
    app.register_blueprint(mod)
    socketio.init_app(app)
    database.init()
    return app
