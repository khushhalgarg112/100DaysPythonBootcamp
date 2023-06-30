import requests
from twilio.rest import Client

api_key = '04fc3a252670479cd2189c226194a31a'
account_sid = 'AC47f7d48de5d76ea50ff0765acbaf333f'
auth_token = 'd439d9c124efed77af9a96e56db2f238'

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
    from_='+14178554309',
    body='its raining please keep your umbrella',
    to='+918307191801'
    )

    print(message.status)
