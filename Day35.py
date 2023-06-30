import requests
from twilio.rest import Client

api_key = 'api'
account_sid = 'AC47f7d48de5d76ea50ff0765acbaf333f'
auth_token = 'twilio auth token'

parameter = {
    "lat": 29.353861,
    "lon": 76.495880,
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameter)
response.raise_for_status()
data = response.json()["weather"][0]["id"]
if data < 700:

    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='your twilio number',
    body='its raining please keep your umbrella',
    to='Number where to send message'
    )

    print(message.status)
