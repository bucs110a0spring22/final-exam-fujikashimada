import requests
import json

class Geolocation:

  def __init__(self, ip_address):
    '''
    Initializes url with user inputted IP address. 
  args: (str) IP address
  return: none
    '''
    self.url = f'https://geolocation-db.com/jsonp/{ip_address}'

  def get(self):
    '''
    Requests and pulls API through URL and returns a result based on the parameters. 
  args: none
  return: (str) Latitude and longitude of IP address
    '''
    r = requests.get(self.url)
    result = r.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    
    ip_lat = result.get('latitude')
    ip_long = result.get('longitude')
    return ip_lat, ip_long

   
    #print("latitude: ", ip_latitude)
    #print("longitude: ", ip_longitude)
    

    
