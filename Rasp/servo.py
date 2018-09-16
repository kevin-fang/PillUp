# from gpiozero import AngularServo, Motor
# from time import sleep
# from enum import Enum
# import keyboard as kb
#
# s = AngularServo(17, min_angle=-45, max_angle=45)
# m = Motor(27, 21, pwm=True)
#
# class Rotation(Enum):
#    left = -45
#    right = 45
#    straight = 0
#
# def turn(rotation, degree = None):
#
#    if degree:
#       s.angle = degree
#    else:
#       s.angle = rotation.value
#
#    straight = 0
#
# def turn(rotation, degree = None):
#    right = 45
#    if degree:
#       s.angle = degree
#    else:
#       s.angle = rotation.value
#
# s.angle = 0.0
# while True:
#    m.forward(float(input()))


import serial

arduinoSerialData = serial.Serial('/dev/cu.usbmodem14431', 9600)
