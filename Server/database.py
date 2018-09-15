from mongoengine import connect

def init():
    connect('mongo', host='mongodb://admin:admin9090@ds257732.mlab.com:57732/pillsup')