# import requests


# TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'
# chat_id = 5325797385

# def send_button(chat_id,text,TOKEN):
#     url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

#     button1 = {'text':'😺CAT'}
#     button2 = {'text':'DOG'}

#     keyboard = [[button1,button2]]

#     reply_markup = {'keyboard':keyboard,'resize_keyboard':True}

#     data = {
#         'chat_id':chat_id,
#         'text':text,
#         'reply_markup':reply_markup
#     }
#     r = requests.post(url,json=data)
#     print(r.status_code)

# send_button(chat_id, 'hi' ,TOKEN)
