from django.shortcuts import render
from django.http import HttpResponse
import pyowm
from datetime import datetime as dt

apiKey= 'b7446f6af77392d0695d0989baf220de'
owmConnect = pyowm.OWM(apiKey)
weatherManager = owmConnect.weather_manager()

time = dt.now()
time = time.strftime("%H:%M:%S")

#def home(request):
 #  return render(request, 'weather_front_end.html')


def WeatherSearch(request):
    try:    
        city = request.GET['flocation']
    except:
        city = 'chennai'
    place = city+', IN'
    try: 
        weatherData = weatherManager.weather_at_place(place)
        data = weatherData.weather
        location = place.title()
        time = dt.now()
    
        temperature = weatherData.weather.temperature("celsius")["temp"]
        humidity = weatherData.weather.humidity
        time = time.strftime("%H:%M:%S")
        info = data.detailed_status
        return render(request, 'weather_front_end.html',{'loc_':location, 'time_':time, 'info_':info, 'temp_':temperature, 'hum_':humidity})
    except:
        location= "City or Place not Found" 
        time=None
        info=None
        humidity=None
        temperature = None
        return render(request, 'weather_front_end.html',{'loc_':location, 'time_':time, 'info_':info, 'temp_':temperature, 'hum_':humidity})
