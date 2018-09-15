from Utilities.NotificationCenter import NotificationCenter as Notification
from main import socketio
import json


@Notification.notify_on('dispense')
def dispense(data):
    try:
        data = json.dumps(data)
        socketio.emit('dispense', data, broadcast=True, namespace='/stream')
    except:
        pass


@Notification.notify_on('refill')
def dispense(data):
    try:
        data = json.dumps(data)
        socketio.emit('refill', data, broadcast=True, namespace='/stream')
    except:
        pass


@socketio.on('connect', namespace='/stream')
def handle_connect():
    pass

