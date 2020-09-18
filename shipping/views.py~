from geopy.distance import great_circle
import requests



#http://ipinfo.io/json/197.210.71.115
#6.4474, 3.3903  --home lagos
#9.0579,7.4951    --work abuja
#10.5105, 7.4165   kaduna


def GetDistance():
	ip_data= requests.get('http://ipinfo.io/json').json()
	client_latlon = ip_data['loc']
	#base_latlon = (6.4474, 3.3903)
	base_latlon = (10.5105, 7.4165)
	#base_latlon = (9.0579,7.4951)
	
	
	return great_circle(client_latlon, base_latlon).miles

		
	
