from django.shortcuts import render
# Create your views here.

from .weather_data import get_data
from.location import get_location_from_ip
from datetime import datetime,timedelta
def index(request):
    
    city_name=" "
    context = {}
    if request.method =="POST":

        city_name=request.POST.get('city_name')

        

    else:
        user_ip = "110.226.167.56"

        city_name,region,country = get_location_from_ip(user_ip)


    data2= get_data(city_name)

    today=datetime.today()

    dates=[]
    days=[]

    for i in range(7):
        day= today + timedelta(days=i)
        days.append(day.strftime('%A'))

        formatted_date =f"{int(day.strftime('%d'))} {day.strftime('%b')}"

        dates.append(formatted_date)

    
    
    if data2:

            context={
                'city': data2['city'],
            'country': data2['country'],
            'region': data2['region'],
            'current_temp': data2["current_temp"],
            'icon':data2['icon'],
            'current_condition': data2["current_condition"],
            'current_wind': data2["current_wind"],
            'direction': data2["direction"],
            'rain_chance': data2["rain_chance"],
            'forecast_max_temp':data2['forecast_max_temp'],
            'forecast_min_temp':data2["forecast_min_temp"],
            'forecast_condition':data2["forecast_condition"],
            'forecast_wind':data2["forecast_wind"],
            'forecast_humaidity':data2['forecast_humaidity'],
            'forecast_rain_chance':data2["forecast_rain_chance"],
            'forecast_uv':data2["forecast_uv"],
            'forecast_icon':data2['forecast_icon'],
            "dates":dates,
            "days":days
            }

            

    
        
    else:
            context = {'error': "Unable to retrieve weather data."}

    return render(request,'home.html',context)

def get_client_ip(request):
    """Helper function to get client IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print(ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def news(request):
     
     context={
          "name":"Teersingh",
     }

     return render(request,'name.html',context)