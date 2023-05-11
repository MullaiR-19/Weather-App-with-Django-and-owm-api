from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

#def home(request):
 #  return render(request, 'weather_front_end.html')


def WeatherSearch(request):
    try:    
        city = request.GET['flocation']
    except:
        city = 'chennai'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    city = city+"+weather"
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    try:
        soup = BeautifulSoup(res.text,'html.parser')   
        location = soup.select('#oFNiHe')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()       
        info = soup.select('#wob_dc')[0].getText().strip() 
        weather = soup.select('#wob_tm')[0].getText().strip()
        humidity = soup.select('#wob_hm')[0].getText().strip()
    except:
        update = "City or Place not Found" 

    return render(request, 'weather_front_end.html',{'loc_':location, 'time_':time, 'info_':info, 'temp_':weather, 'hum_':humidity})
