import requests
import os
from twilio.rest import Client
import datetime as dt
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

today_day = dt.date.today()

STOCK_PRIZE_API = "7E0SD3VG#FDV0S8N0V#"
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey={STOCK_PRIZE_API}'
r = requests.get(url)
data = r.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_Closing = data_list[0]["4. close"]
print(yesterday_Closing)
before_yesterday = data_list[1]["4. close"]
print(before_yesterday)
difference = float(yesterday_Closing)- float(before_yesterday)
up_down = ""
if difference >0:
    up_down= "⬆️"
else:
    up_down="⬇️"
percentage = round(abs(difference)/float(yesterday_Closing)*100)
print(percentage)
if percentage >1:
    NEWS_API = "a5898357c0c34ab9b0c#2ca47f8e541ce8#"
    url2 =f"https://newsapi.org/v2/everything?q=tesla&apiKey={NEWS_API}"
    res = requests.get(url2)
    for i in range(0,3):
        news_Data_title = res.json()["articles"][i]["title"]
        news_Data_description = res.json()["articles"][i]["description"]
        ACC_SID = "AC47f7d48de5d76ea50f#3f0765acbaf333f#"
        AUTH_TOKEN = "4ce91d0bc63a01f15#2cb29fe17ef564b9#"
        client = Client(ACC_SID, AUTH_TOKEN)

        message = client.messages.create(
                                    body=f"{STOCK}: {up_down}{percentage}% \nHeadline: {news_Data_title}. \n\n Brief: {news_Data_description}",
                                    from_='+14178554309#',
                                    to='+918307191801'
                        )

        print(message.status)
else:
    print("NO news")
