from socketIO_client import SocketIO, BaseNamespace
import json


class Streamer(BaseNamespace):
    def on_connect(self):
        print('Streamer: connected')

    def on_disconnect(self):
        print('Streamer: disconnected')

    def on_refill(self, data):
        print(data)

    def on_dispense(self, data):
        print(data)


socket = SocketIO('api.pillup.org', 80)
stream_namespace = socket.define(Streamer, '/stream')
socket.wait()
