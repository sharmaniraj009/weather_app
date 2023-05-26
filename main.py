import requests
import json
import datetime
from dotenv import load_dotenv
import os

load_dotenv('.env')
api = os.getenv('api')

#todays date
date = str(datetime.date.today())

# city = input("enter a city : ")
city = 'vapi'


url_weather = f'https://api.weatherapi.com/v1/forecast.json?key={api}&q={city}&days=1&aqi=yes&alerts=yes'
url_astronomy = f'https://api.weatherapi.com/v1/astronomy.json?key={api}&q={city}&dt={date}'


#request to api
results = requests.get(url_weather)
results_astro = requests.get(url_astronomy)

#convert json to dict
weatherdict = json.loads(results.text)
weatherdict_astro = json.loads(results_astro.text)


city_name = weatherdict["location"]["name"]
temp_c = weatherdict["current"]["temp_c"]
humidity = weatherdict["current"]["humidity"]
cloud = weatherdict["current"]["cloud"]  # returns an integer of no use to me
condition = weatherdict["current"]["condition"]["text"]


sunrise = weatherdict_astro["astronomy"]["astro"]["sunrise"]
sunset = weatherdict_astro["astronomy"]["astro"]["sunset"]
moonrise = weatherdict_astro["astronomy"]["astro"]["moonrise"]
moon_phase = weatherdict_astro["astronomy"]["astro"]["moon_phase"]

print(f"{datetime.datetime.now()}")
print(f"{city_name} Temperature is {temp_c} degree centigrade and humidity is {humidity}. The weather is : {condition}.")
print(f"Sunrise at {sunrise}. Sunset at {sunset}.")
print(f"Moon rise at {moonrise}. Today is {moon_phase}")

