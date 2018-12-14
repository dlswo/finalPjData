from geopy.geocoders import GoogleV3

myApi = 'AIzaSyBAPR_JscpDtaLzmvYV-oAZGQAEp8kxBic'

geolocator = GoogleV3(api_key=myApi)
location = geolocator.geocode(query=search_blog_keyword, language='ko', exactly_one=False, timeout=5)
print(location[0].latitude, location[0].longitude)