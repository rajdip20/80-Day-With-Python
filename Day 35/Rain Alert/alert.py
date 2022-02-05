import requests
from twilio.rest import Client

api_key = "Enter Here"   # Enter openweathermap api key
account_sid = "Enter Here"  # Enter twilio account sid
auth_token = "Enter Here"   # Enter twilio account auth token
MY_LAT = 22.5697
MY_LON = 88.3697
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "units": "metric",
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂",
        from_="Your Virtual Twilio Number",
        to="__Enter Your Registered Phone Number__"
    )

    print(message.status)

# print(data["hourly"][0]["weather"][0]["id"])
