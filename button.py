import requests
import telegram
TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'
bot = telegram.Bot(TOKEN)


def get_updates(TOKEN):
    update = bot.getUpdates(TOKEN)[-1]
    return update


def get_lastupdate(update):
    chat_id = update.message.chat.id
    text = update.message.text
    message_id = update.message.message_id
    return chat_id,message_id,text


def dog(chat_id,text):
    Dog = requests.get('https://random.dog/woof.json')
    dog_data = Dog.json()['url']
    data = {
            'chat_id':chat_id,
            'photo':dog_data,
            'text':text
            }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',json=data)


def cat(chat_id,text):    
    Cat = requests.get ('https://aws.random.cat/meow')
    url= Cat.json()['file']
    data1 = {
                'chat_id':chat_id,
                'photo':url,
                'caption':text
            }
        
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',json=data1)


def get_button(chat_id):
        
    button1 = {'text':'😺CAT'}
    button2 = {'text':'🐶DOG'}

    keyboard = [[button1,button2]]
    
    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
    data = {
            'chat_id':chat_id,
            # 'text':text,
            'reply_markup':reply_markup
        }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=data)
        
    return reply_markup 


# 


new_message = -1
while True:
    updates = get_updates(TOKEN)
    lastupdate = get_lastupdate(updates)
    chat_id,last_message_id,text= lastupdate

    if new_message != last_message_id:
        if text.lower()=='😺cat' or 'cat':
            cat(chat_id,text)
            get_button(chat_id)
        if text.lower()=='🐶dog' or 'dog':
            dog(chat_id,text)
            get_button(chat_id)
        

        new_message = last_message_id











































# def send_alternative(chat_id):
#     data = {
#         'chat_id':chat_id,
#         'text':'Iltimos dog yoki cat so`zini kiriting!'
#         }
#     requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',json=data)
        