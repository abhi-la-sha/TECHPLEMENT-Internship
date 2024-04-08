import datetime as dt
import requests

Base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "a6450cfd75bca81e23153cefb7098171"
city = input("Enter city name : ")

def kelvin_to_celsius(kelvin):
  celsius= kelvin - 273.15
  return celsius

url = Base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

temp_kelvin= response['main']['temp']
temp_celsius= kelvin_to_celsius(temp_kelvin)

feels_like_kelvin= response['main']['feels_like']
feels_like_celsius= kelvin_to_celsius(feels_like_kelvin)

humidity=response['main']['humidity']
description= response['weather'][0]['description']
sunrise_time=dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time=dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])


print("The Temperature in", city, "is", temp_celsius, "°C")
print("The Temperature in", city, "Feels like", feels_like_celsius, "°C")
print("The Humidity in", city, "is", humidity, "%")
print("The General weather in", city, "is", description)
print("The Sun rises in", city, "at", sunrise_time, "local time")
print("The Sun sets in", city, "at", sunset_time, "local time")