from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute-scripts')
def execute_scripts():
    os.system("python server.py & python client.py")
    return "Scripts executed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
