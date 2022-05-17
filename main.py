from IPGeolocationAPI import Geolocation
from DailyWeatherAPI import DailyWeather
import requests
import json


def main():
  ip_address = input("Enter your IP address: ")
  geo1 = Geolocation(ip_address)
  print (geo1.get())

  new_iplat, new_iplong = (geo1.get())
  weather1 = DailyWeather(new_iplat, new_iplong)
  print (weather1.get())
                
main()


#This is the code without classes and different files just so the code works. The hashtaged out code above is the attempted code. As mentioned in the README it would not allow me to input the latitude and longitude values as floats which was required by the API. 
ip_address = input("Enter your IP address: ")
address_url = 'https://geolocation-db.com/jsonp/' + ip_address
r = requests.get(address_url)
result = r.content.decode()
result = result.split("(")[1].strip(")")
result  = json.loads(result)

ip_latitude = result.get('latitude')
ip_longitude = result.get('longitude')
print("latitude: ", ip_latitude)
print("longitude: ", ip_longitude)

weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={ip_latitude}&longitude={ip_longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_hours&temperature_unit=fahrenheit&timezone=America%2FNew_York'

r = requests.get(weather_url)
result = r.json()

print(result)