from gpiozero import DistanceSensor, AngularServo
from time import sleep

sensor = DistanceSensor(echo=17, trigger=4, max_distance=200)
serv_right = AngularServo(4)
serv_left = AngularServo(27)
# serv_sticker = AngularServo(25)


serv_right.angle = -3
serv_left.angle = -5
# serv_sticker.angle = 90
# sleep(3)
# serv_sticker.angle = -40


def cart_1():

    serv_right.angle = -90
    sleep(1)

    serv_right.angle = -3
    sleep(1)

def cart_2():
    serv_left.angle = 90
    sleep(1)

    serv_left.angle = -5
    sleep(1)


state = False

while True:


    distance = sensor.distance
    if distance == 0:
        distance = 400
    print(distance)

    if distance < 1 and state:
        cart_1()
        cart_2()
        state = False
    else:
        # state = True
        pass
