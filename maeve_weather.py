from WunderWeather import weather

api_key = ""

def getCurrentTemperature(here):
	here = "MD/Hagerstown"
	extractor = weather.Extract(api_key)
	[location,current] = extractor.features(here,(('geolookup',''),('now','')))
#	return "Current Temperature in {0} is: {1}" (location.data.city,current.temp_f)
	print("Current Temperature in {0} is: {1}" (location.data.city,current.temp_f))
