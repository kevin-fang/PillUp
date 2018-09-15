from main import socketio
from NotificationCenter import NotificationCenter as Notification
import json


@Notification.notify_on('socket_stream')
def stream(data):

    try:
        data = json.dumps(data)
        socketio.emit('event', data, broadcast=True, namespace='/stream')
    except:
        pass


@socketio.on('connect', namespace='/stream')
def handle_connect():
    pass

