import requests
from pprint import pprint

# 5325797385
# mine_id = 5325797385

chat_id = 5325797385

TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'

data = {
    'chat_id':chat_id,
    'text':'Hi,Samandar'

}

response = requests.get(url = f'https://api.telegram.org/bot{TOKEN}/getUpdates')

print(response.json())

