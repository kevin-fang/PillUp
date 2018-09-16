from gpiozero import DistanceSensor, AngularServo
from time import sleep
from socketIO_client import SocketIO, BaseNamespace
import json

#Configuring servos with pin numbers
serv_right = AngularServo(27)
serv_left = AngularServo(17)
serv_sticker = AngularServo(25)

#Put them at the init place
serv_right.angle = -3
serv_left.angle = -5
sleep(1)
serv_sticker.angle = 87
sleep(1)


def cart_1():
    """
        This is the left servo
    """
    serv_left.angle = 90
    sleep(1)
    serv_left.angle = -5
    sleep(1)

def cart_2():
    """
        This is the right servo
    """
    serv_right.angle = -90
    sleep(1)
    serv_right.angle = -3
    sleep(1)
    
def like():
    """
        Raise sticker function
    """
    serv_sticker.angle = -90
    sleep(2)
    serv_sticker.angle = 87
    sleep(2)


class Streamer(BaseNamespace):
    def on_connect(self):
        print('Streamer: connected')

    def on_disconnected(self):
        print("Streamer: disconnected")

    def on_refill(self, data):
        data = json.loads(data)

    def on_dispense(self, data):
        data = json.loads(data)
        cartridge = data['medicine']['cartridge']
        if cartridge == 1:
            cart_1()
        elif cartridge == 2:
            cart_2()

socket = SocketIO('http://api.pillup.org', 80)
namespace = socket.define(Streamer, '/stream')
socket.wait()

