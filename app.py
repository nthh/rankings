from flask import Flask,render_template,send_from_directory


app = Flask(__name__)

@app.route('/data/<path:path>')
def send_js(path):
    return send_from_directory('data', path)

@app.route('/')
def home():
    return render_template('index.html')
