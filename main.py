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
@socketio.on('player_update')
def handle_player_moved(playerloc, methods=['GET', 'POST']):
    print('We received the data of a single player.' + str(playerloc))
    # playerloc has the format name:[x,y].

    # you need to update the global player list, called players
    # update it with the entry which contains the player for which
    # the player location change occured (it's in the data stored above)
    # hint: players is a dictionary type

    socketio.emit('players_moved', players, callback=messageReceived)

@socketio.on('connected')
def send_positions(data):
    json = {'tim':[1,2], 'john':[1,2]}
    socketio.emit('players_moved', json)
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