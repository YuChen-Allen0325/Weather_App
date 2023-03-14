from django.shortcuts import render
import json 
import urllib.request


# Create your views here.
def index(request):
    if request.method == 'POST':
        try:
            city = request.POST['city']
            ## Search point: openweathermap    5 day / 3 hour weather forecast -- Other features
            ## json file maybe change,base on official document
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=d389086bad382c59a109ab2203eb2347').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['city']['country']),
                "coordinate": str(json_data['city']['coord']['lon']) + ' | ' +
                str(json_data['city']['coord']['lat']),
                "temp": str(json_data['list'][0]['main']['temp'])+'k',   # Notice that index in 'list'
                "pressure": str(json_data['list'][0]['main']['pressure']),
                "humidity": str(json_data['list'][0]['main']['humidity'])
            }
        except:
            city = ''
            data = {}
    else:
        city = ''
        data = {}
    return render(request, 'index.html',{'city':city,'data':data})