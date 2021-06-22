import requests
import os
from datetime import datetime

from requests import api

user_api = os.environ['current_weather_data']
location = input("enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

if api_data['cod'] == 404:
    print ("invalid city: {}, please check your city name".format(location))
else:
     #create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    datetime = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("----------------------------------------------------------")
    print("weather stats for - {} || {}".format(location.upper(),datetime))
    print("----------------------------------------------------------")

    print("current temperature is: {:,2f} deg C".format(temp_city))
    print("current weather desc  :",weather_desc)
    print("current humidity      :",hmdt,'%')
    print("current wind speed    :",wind_spd ,'kmph')