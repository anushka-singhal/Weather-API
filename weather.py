import requests

city = input("Enter the name of the city")
url = f"https://deapi.weatherapi.com/v1/current.json?key=your key&q={city}"
r = requests.get(url)
print(r.text)