from geopy.geocoders import Nominatim

geoLocator = Nominatim(user_agent="Psawesome")
location = geoLocator.geocode("Seoul, South Korea")

print(location.raw)
