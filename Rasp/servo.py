from gpiozero import DistanceSensor, AngularServo
from time import sleep

#Configuring servos with pin numbers
serv_right = AngularServo(27)
serv_left = AngularServo(17)
serv_sticker = AngularServo(24)

#Put them at the init place
serv_right.angle = -3
serv_left.angle = -5
sleep(1)
serv_sticker.angle = -80
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
    serv_sticker.angle = 85
    sleep(2)
    serv_sticker.angle = -80
    sleep(2)


while True:

    # Testing servos. It should be deleted later on
    cart_1()
    sleep(1)

    cart_2()
    sleep(1)
    like()