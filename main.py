import requests
import json
from flask import Flask, render_template

longitude = 144.9578
latitude = -37.8082
apiKey = "37bed561bf48e9084076d98cb79237af"

# url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely&appid={apiKey}"

# data = requests.get(url=url)
# with open('data.json', 'w+') as f:
#     f.write(data.text)

# data = json.loads(open('data.json', 'r+').read())
# print(len(data['hourly']))

# # len(data['daily']) --> 8
# # len(data['hourly']) --> 48

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/7days')
def last7days():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
    data = requests.get(url=url)
    info = json.loads(data.text)
    keys = ['1', '2', '3', '4', '5', '6', '7', '8']
    day = []
    min = []
    max = []
    night = []
    evening = []
    morning = []
    for i in info['daily']:
        day.append(i['temp']['day']-273)
        min.append(i['temp']['min']-273)
        max.append(i['temp']['max']-273)
        night.append(i['temp']['night']-273)
        evening.append(i['temp']['eve']-273)
        morning.append(i['temp']['morn']-273)
        
    return render_template('data.html', keys=keys, day=day, min=min, max=max, night=night, eve=evening, morning=morning)

@app.route('/hours')
def last48hours():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,daily&appid={apiKey}"
    data = requests.get(url=url)
    info = json.loads(data.text)
    keys = []
    day = []
    g = 1
    for i in info['hourly']:
        keys.append(str(g))
        day.append(i['temp']-273)
        g+=1
        
    return render_template('hours.html', keys=keys, data=day)

if __name__ == "__main__":
    app.run(debug=True)