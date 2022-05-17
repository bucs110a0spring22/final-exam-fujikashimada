import requests


class DailyWeather:
  def __init__(self, new_iplat, new_iplong):
    '''
    Initializes URL
    args: (float) latitude and longitude     coordinates from the geolocation API is inputed here. 
    return: none
    '''
    self.url = f'https://api.open-meteo.com/v1/forecast?latitude={new_iplat} &longitude={new_iplong}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_hours&temperature_unit=fahrenheit&timezone=America%2FNew_York'
  def get(self):
    '''
    Requests and pulls API through URL and returns a result based on the parameters 
    args: none 
    return: (str) weather data, daily temperature and precipitation
    '''
    r = requests.get(self.url)
    weather_result = r.json()

    return weather_result



