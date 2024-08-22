# import requests

# url="http://api.weatherapi.com/v1/forecast.json"
# api_key="f62f09e223fb4ce592640917240908"

# days=7

# # print(requests.get(url,params=api_key))
# def get_data(city_name):

#     params = {
#         'q':city_name,
#         'key':api_key,
#         'days':days,
#     }

#     response = requests.get(url,params=params)
    
    
#     if response.status_code == 200:

#         data = response.json()

#         city= data['location']['name']

#         country= data['location']['country']
#         region= data['location']['region']

        

#         current_temp =data['current']['temp_c']

#         current_condition= data['current']['condition']['text']

#         current_wind= data['current']['wind_kph']

#         direction=data['forecast']['forecastday'][0]['hour'][0]['wind_dir']

#         rain_chance= data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']

#         data1={
#             'city':city,
#             'country':country,
#             "region":region,
#             "current_temp":current_temp,
#             "current_condition":current_condition,
#             "current_wind":current_wind,
#             "direction":direction,
#             "rain_chance": rain_chance
#         }
        
        
#     else:
#         print(f"Error retrieving weather data: {response.status_code}") 

#     return data1
    

import requests

url = "http://api.weatherapi.com/v1/forecast.json"
api_key=''


days = 7

def get_data(city_name):
    params = {
        'q': city_name,
        'key': api_key,
        'days': days,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        data = response.json()
        
        city = data['location']['name']
        country = data['location']['country']
        region = data['location']['region']
        current_temp = data['current']['temp_c']
        current_condition = data['current']['condition']['text']
        current_wind = data['current']['wind_kph']
        direction = data['forecast']['forecastday'][0]['hour'][0]['wind_dir']
        rain_chance = data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
        icon=data['current']['condition']['icon']

        forecast_avghumidity_var=[]
        forecast_rain_chance_var=[]
        forecast_max_temp_var = []
        forecast_min_temp_var=[]
        forecast_condition_var=[]
        forecast_uv_var=[]
        forecast_wind_var=[]
        forecast_icon_var=[]

        for i in range(1,7):
                forcast_max_temp=data['forecast']['forecastday'][i]['day']['maxtemp_c']
                forcast_min_temp=data['forecast']['forecastday'][i]['day']['mintemp_c']
                forcast_wind=data['forecast']['forecastday'][i]['day']['maxwind_kph']
                forecast_rain_chance = data['forecast']['forecastday'][i]['day']['daily_chance_of_rain']

                forecast_condition = data['forecast']['forecastday'][i]['day']['condition']['text']
                forecast_uv= data['forecast']['forecastday'][i]['day']['uv']

                forecast_avghumidity=data['forecast']['forecastday'][i]['day']['avghumidity']

                forecast_icon=data['forecast']['forecastday'][i]['day']['condition']['icon']

                forecast_avghumidity_var.append(forecast_avghumidity)
                forecast_max_temp_var.append(forcast_max_temp)
                forecast_min_temp_var.append(forcast_min_temp)
                forecast_rain_chance_var.append(forecast_rain_chance)

                forecast_condition_var.append(forecast_condition)
                forecast_uv_var.append(forecast_uv)

                forecast_wind_var.append(forcast_wind)

                forecast_icon_var.append(forecast_icon)

        
                
        
                
        

        data1 = {
            'city': city,
            'country': country,
            'region': region,
            'current_temp': current_temp,
            'current_condition': current_condition,
            'current_wind': current_wind,
            'icon':icon,
            'direction': direction,
            'rain_chance': rain_chance,
            'forecast_max_temp':forecast_max_temp_var,
            'forecast_min_temp':forecast_min_temp_var,
            'forecast_condition':forecast_condition_var,
            'forecast_wind':forecast_wind_var,
            'forecast_humaidity':forecast_avghumidity_var,
            'forecast_rain_chance':forecast_rain_chance_var,
            'forecast_uv':forecast_uv_var,
            'forecast_icon':forecast_icon_var


        }
        print(forecast_icon)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        data1 = {}
    except KeyError as e:
        print(f"Key error: {e}")
        data1 = {}

    return data1


print(get_data('jaipur'))



    


