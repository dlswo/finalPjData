import requests

subscription_key = '91aaae09df914313bf08a3bdb7fdcfb0'
assert subscription_key

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

search_term = "제주도"



headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "license": "all", "imageType": "photo", "size": "large", "safeSearch": "Moderate"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

contentUrl = [img["contentUrl"] for img in search_results["value"][:5]]

print(contentUrl[0])
print(contentUrl[1])
print(contentUrl[2])
print(contentUrl[3])
print(contentUrl[4])