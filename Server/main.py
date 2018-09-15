from app import create_app, socketio


def main():
    app = create_app()
    socketio.run(app, port=8080)

if __name__ == '__main__':
    main()
