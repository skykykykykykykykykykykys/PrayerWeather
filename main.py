from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def weather():
     return render_template('weather.html', temp=temp_f)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
     app.run(debug=True)