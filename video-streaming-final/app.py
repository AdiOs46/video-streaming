from flask import Flask, render_template
from threading import Thread
from subprocess import Popen
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_call')
def video_call():
    os.system("python server.py & python client.py")
    return "Video calling functionality started."

@app.route('/screen_share')
def screen_share():
    os.system("python server_ss.py & python client_ss.py")
    return "Screen sharing functionality started."

@app.route('/text_chat')
def text_chat():
    os.system("python server_chat.py & python client_chat.py")
    return "Texting functionality started."

if __name__ == '__main__':
    app.run(debug=True)
