import json
import time
import conf
import requests
def get_bitcoin_price():
    url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=BTC,INR"
    response=requests.request("GET",url)
    response=json.loads(response.text)
    current_price=response["INR"]
    return current_price
def send_telegram_alert(message):
    url="https://api.telegram.org/"+conf.telegram_bot_id+"/sendMessage"
    data={
        "chat_id":conf.telegram_chat_id,
        "text":message
         }
    try:
        response=requests.request("POST",url,params=data)
        print("This is the Telegram URL")
        print(url)
        print("This is Telegram response")
        print(response.text)
        telegram_data=json.loads(response.text)
        return telegram_data
    except Exception as e:
        print("An error occured while sending message via Telegram.")
        print(e)
        return False
while True:
    selling_price=2140300
    current_price=get_bitcoin_price()
    if current_price>=selling_price:
        message="Alert! The the Bitcoin has exceeded the selling price."
        telegram_status=send_telegram_alert(message)
        print("The telegram status is : "+str(telegram_status))
    time.sleep(30)