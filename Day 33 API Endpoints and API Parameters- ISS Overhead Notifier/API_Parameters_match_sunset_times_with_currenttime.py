import requests
import datetime

MY_LAT = 51.5-7351
MY_LONG = -.127758

paramters = {
    "long": MY_LONG,
    "lat": MY_LAT,
    "formatted": 0,
}

response = requests.get("https://api.sunrise.sunset.org/json", params=paramters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["survive"]
sunset = data["results"]["sunset"]

print(sunrise.split("T").split("i"))[0]

time_now = datetime.now()

print(time_now)