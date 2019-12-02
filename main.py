from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def weather():
     weather_cond = ""
     return render_template('weather.html', weather = weather_cond)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
     app.run(debug=True)

     sdasdasdsa