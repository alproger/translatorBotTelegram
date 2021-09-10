from google_trans_new import google_translator
import telebot
from telebot import types

bot_token = 'your bot token' # you can get token from botFather in Telegram
bot = telebot.TeleBot(token=bot_token)
translator = google_translator()

#languages of users can translate
lang_dict = {
    '🇺🇿Узбекский':'uz',
    '🇷🇺Руский':'ru',
    '🇦🇪Арбский':'ar',
    '🇫🇷Французкий':'fr',
    '🇹🇷Туретский':'tr',
    '🇧🇴Испанский':'es',
    '🇩🇪Немецкий':'de',
    '🇬🇧Англизкий':'en',
    '🇮🇹Италянский':'it' }

# inline buttons for choosing language for translate
lang_btns = types.InlineKeyboardMarkup(row_width=2)
uzbtn = types.InlineKeyboardButton(text='🇺🇿Узбекский', callback_data='uz')
rubtn = types.InlineKeyboardButton(text='🇦🇪Арбский', callback_data='ar')
frbtn = types.InlineKeyboardButton(text='🇷🇺Руский', callback_data='ru')
arbtn = types.InlineKeyboardButton(text='🇫🇷Французкий', callback_data='fr')
trbtn = types.InlineKeyboardButton(text= '🇹🇷Туретский', callback_data='tr')
esbtn = types.InlineKeyboardButton(text='🇧🇴Испанский' , callback_data='es')
debtn = types.InlineKeyboardButton(text='🇩🇪Немецкий', callback_data='de')
itbtn = types.InlineKeyboardButton(text= '🇮🇹Италянский', callback_data='it')
enbtn = types.InlineKeyboardButton(text= '🇬🇧Англизкий', callback_data= 'en')
lang_btns.add(uzbtn,rubtn,arbtn,frbtn,trbtn,esbtn,debtn,itbtn,enbtn)

#message_hendler for hendling /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,text='Привет я бот переводчик.\nОтпрайте мне текст я перевожу')

mes = ['',0]

#message_hendler for hendling message of users send to translate
@bot.message_handler()
def messager(message):
    mes[0] = message.text
    mes[1] = message.chat.id
    bot.send_message(message.chat.id,text=f'Ваш текст : {message.text}'
                                          f'\n\nвыберите язык перевода',reply_markup=lang_btns)


#callback_query_hendler for inlinebuttons users can choose and translate text
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    message_chat_id  = mes[1]
    message_text = mes[0]
    if call.data == 'uz':
        translated_message = translator.translate(message_text,lang_tgt='uz')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇺🇿Узбекского языка\n\n' \
                       f'🇺🇿 {translated_message}'
        bot.send_message( message_chat_id,text=message_send)

    elif call.data == 'ru':
        translated_message = translator.translate(message_text,lang_tgt='ru')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇷🇺Руского языка\n\n' \
                       f'🇷🇺 {translated_message}'
        bot.send_message( message_chat_id,text=message_send)

    elif call.data == 'ar':
        translated_message = translator.translate(message_text,lang_tgt='ar')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇦🇪Арбского языка\n\n' \
                       f'🇦🇪 {translated_message}'
        bot.send_message(message_chat_id, text=message_send)

    elif call.data == 'fr':
        translated_message = translator.translate(message_text,lang_tgt='fr')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇫🇷Французкого языка\n\n' \
                       f'🇫🇷 {translated_message}'
        bot.send_message(message_chat_id, text=message_send)

    elif call.data == 'tr':
        translated_message = translator.translate(message_text,lang_tgt='tr')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇹🇷Туретского языка\n\n' \
                       f'🇹🇷 {translated_message}'
        bot.send_message(message_chat_id, text=message_send)

    elif call.data == 'es':
        translated_message = translator.translate(message_text,lang_tgt='es')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇧🇴Испанского языка\n\n' \
                       f'🇧🇴 {translated_message}'
        bot.send_message(message_chat_id, text=message_send)


    elif call.data == 'de':
        translated_message = translator.translate(message_text,lang_tgt='de')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇩🇪Немецкого языка\n\n' \
                       f'🇩🇪 {translated_message}'
        bot.send_message(message_chat_id, text=message_send)

    elif call.data == 'it':
        translated_message = translator.translate(message_text,lang_tgt='it')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇮🇹Италянского языка\n\n' \
                       f'🇮🇹 {translated_message}'
        bot.send_message(message_chat_id, text=message_send)

    elif call.data == 'en':
        translated_message = translator.translate(message_text,lang_tgt='en')
        message_send = f'Ваш текст: {message_text}\n\n' \
                       f'перевод на 🇬🇧Англизкого языка\n\n' \
                       f'🇬🇧 {translated_message}'
        bot.send_message(message_chat_id, text=message_send)

print('working...')

bot.polling(none_stop=True)
