from gevent import monkey; monkey.patch_all(socket=True)

from app import create_app, socketio
from platform import system as st
from Controller import main_controller





def main():

    app, context = create_app()
    # main_controller()
    # app.run(ssl_context=context)
    socketio.run(app, host='0.0.0.0', port=8080 if st() == 'Darwin' else 80, certfile='server.crt', keyfile='server.key')

if __name__ == '__main__':
    main()
