from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(message):
    send(message, broadcast=True)

@app.route('/')
def index():
    return render_template('home.html')
    

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
