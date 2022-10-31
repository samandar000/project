import requests
import telegram
TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'

bot = telegram.Bot(TOKEN)
update = bot.getUpdates()[-1]
chat_id = update.message.chat.id
text = update.message.text
photo = update.message.photo

dog = requests.get('https://random.dog/woof.json')
dog_data = dog.json()['url']
data = {
    'chat_id':chat_id,
    'photo':dog_data
}
requests =requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data)

# new_message = -1
# while True:
#     updates = (TOKEN)
#     lastupdate = (updates)
#     chat_id,last_message_id,text= lastupdate
#     new_message = last_message_id



# import telegram
# import os

# TOKEN = os.environ['TOKEN']

# bot = telegram.Bot(TOKEN)
# update = bot.getUpdates()[-1]
# chat_id = update.message.chat.id
# text = update.message.text
# photo = update.message.photo
# # img = 'https://c.ndtvimg.com/2020-08/h5mk7js_cat-generic_625x300_28_August_20.jpg'
# f = open('20546709.jpg','rb')

# bot.sendPhoto(chat_id, photo=f)