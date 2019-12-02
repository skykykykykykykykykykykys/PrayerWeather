from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/info', methods=['POST'])
def info():
     city = request.form['cityname']
     #country_code = request.form['country']
     r_weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9770ca72a55a683022867e21dfd84f9e')
     json_weather = r_weather.json()
     #temperature
     temp_k = float(json_weather['main']['temp'])
     temp_c = (temp_k - 273.15)
     #weather
     weather_status = str(json_weather["weather"][0]["main"])
     #Prayer
     r_pray = requests.get('http://muslimsalat.com/'+city+'.json')
     json_pray = r_pray.json()
     fajr = json_pray["items"][0]["fajr"]
     dzuhur = json_pray["items"][0]["dhuhr"]
     asr = json_pray["items"][0]["asr"]
     maghrib = json_pray["items"][0]["maghrib"]
     isha = json_pray["items"][0]["isha"]

     prayer_time = json_pray["items"]

     return render_template('result.html', temp=round(temp_c,2), weather=weather_status, prayer_time = prayer_time, city=city, fajr=fajr, dzuhur=dzuhur, asr=asr, maghrib=maghrib, isha=isha)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
     app.run(debug=True)