from flask import Flask,render_template,send_from_directory
import os

app = Flask(__name__)

@app.route('/data/<path:path>')
def send_js(path):
    return send_from_directory('data', path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:sport>/<int:season>/')
def byseason(sport,season):
    return render_template('season.html', sport = sport, season = season)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
