from flask import Flask, render_template
from flask_socketio import SocketIO
import asyncio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

players = {}

def messageReceived():
    print("The message was received!")

# format of the received player info...
# username:name
# location:(x, y)
# ie a string as the username and location as a tuple or array of size 2
@socketio.on('update player')
def handle_players_moved(playerloc, methods=['GET', 'POST']):
    print('received my event: ' + str(json))

    # update the list of players
    # you need to update the player

    socketio.emit('players moved', json, callback=messageReceived)

@socketio.on('hello')
def say_hello(data):

    socketio.emit('receive', 'this is string data')
    print(data)

@app.route('/')
def sessions():
    # return app.send_static_file('index.html')
    socketio.emit('hello', 'hi')
    return render_template('index.html')
    # return url_for('static', filename='index.html')

# @app.route('/')

if __name__ == "__main__":  
    socketio.run(app, debug=True)