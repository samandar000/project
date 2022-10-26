import requests
from pprint import pprint
TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'

def get_updates(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = updates.json()
    return updates

def get_lastupdate(updates):
    last_update = updates['result'][-1]
    chat_id = last_update['message']['chat']['id']
    text = last_update['message']['text']
    message_id = last_update['message']['message_id']
    return chat_id,message_id,text

def Region(chat_id):    
    CITY = 'samarkand'
    city = requests.get('https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid=29af92d9f93c8cf795be3ab8bb4f6776')
    url= city.json()
    data1 = {
                'chat_id':chat_id,
                'text':url,
            }
        
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=data1)
    
def get_button(chat_id,text):
        
    button1 = {'text':'😺CAT'}
    button2 = {'text':'🐶DOG'}

    keyboard = [[button1,button2]]
    
    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
    data = {
            'chat_id':chat_id,
            'text':text,
            'reply_markup':reply_markup
        }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=data)
new_message = -1
while True:
    updates = get_updates(TOKEN)
    lastupdate = get_lastupdate(updates)
    chat_id,last_message_id,text= lastupdate

    if new_message != last_message_id:
        if text.lower()== 'samarkand' or 'bukhara':
            Region(chat_id)
            # get_button(chat_id)     
        new_message = last_message_id