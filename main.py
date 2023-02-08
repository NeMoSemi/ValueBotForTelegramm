import pymorphy2
import telebot
import requests
from telebot import types
from file_for_function import if_id_in_file, is_spam


token = '6029918707:AAEJvhZoUkXXbhSquqyNcC27pggBZH4ckMU'
bot = telebot.TeleBot(token)
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
all_valute = {'доллар': 'USD',
              'евро': 'EUR',
              'фунты': 'GBP',
              'чешская крона': 'CZK'}
morph = pymorphy2.MorphAnalyzer()


@bot.message_handler(commands=['start'])
def start(message):
    all_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in all_valute:
        button = types.KeyboardButton(i.capitalize())
        all_buttons.add(button)
    bot.send_message(message.chat.id, (f'Привет {message.from_user.first_name}! Меня зовут ConverterBot. Я помогу '
                                       f'тебе узнать курс валют! Для этого просто нажми на одно из названий валюты '
                                       f'и я отправлю тебе её курс относительно рубля, но помни: если'
                                       f'ты отправишь более 5 запросов за минуту, то будешь заблокирован на 10 минут.'
                                       f'(если возникают трудности пиши /help)'), reply_markup=all_buttons)
    with open('users_list.txt', mode='a', encoding='UTF-8') as file:
        if if_id_in_file(message.from_user.id):
            file.write(f'id={message.from_user.id} first_name={message.from_user.first_name} '
                       f'last_name={message.from_user.last_name} username={message.from_user.username} '
                       f'is_bot={message.from_user.is_bot}\n')



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'Для получения курса валюты нажми на кнопку с соответствующей валютой.'
                                      f'За отправку более чем 5 запросов в минуту вы будете заблокированны'
                                      f'системой на 10 минут')


@bot.message_handler(content_types=['text'])
def text_message(message):
    try:
        if is_spam(message.from_user.id) == False:
            standart_name_of_value = morph.parse(message.text)[0]
            bot.reply_to(message, f"Актуальный курс {standart_name_of_value.inflect({'gent'}).word.lower()} -"
                                  f" {data['Valute'][all_valute[message.text.lower()]]['Value']} руб.")
    except:
        bot.send_message(message.chat.id, "Ошибка, данной валюты несуществует")


bot.infinity_polling()