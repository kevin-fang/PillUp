from app import create_app, socketio
from platform import system as st
from Controller import main_controller
import Routes


def main():

    app = create_app()
    main_controller()
    socketio.run(app, host='0.0.0.0', port=8080 if st() == 'Darwin' else 80)

if __name__ == '__main__':
    main()
