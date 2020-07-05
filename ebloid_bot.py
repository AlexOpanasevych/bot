import telebot as tbot
import random as rm
import os
import sqlite3
from telebot import types

TOKEN = '1122130345:AAHVhkGhh_hs8BrllCiFVjgA2uRXAeW_OOE' # os.environ['BOT_TOKEN']
API_URL = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN

bot = tbot.TeleBot(TOKEN)
# conn = sqlite3.connect('users.db')
# c = conn.cursor()
# c.execute("INSERT INTO user VALUES (?)")

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('1'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, (r, r2))
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Google', types.InputTextMessageContent('google'), url='https://google.com', hide_url=True)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.message_handler(commands=['start'])
def start_msg1(message):
    bot.send_message(message.chat.id, "hello bitch")

@bot.message_handler(commands=['help'])
def start_msg2(message):
    bot.send_message(message.chat.id, "/who - who dies from covid-19 today?\n")

@bot.message_handler(commands=['who'])
def start_msg3(message):
    members_count = bot.get_chat_members_count(message.chat.id)
    print(members_count)
    bot.send_message(message.chat.id, 'developing...')

@bot.message_handler(commands=['register'])
def register(message):
    if message.from_user.username not in list_of_people:
        list_of_people.append(message.from_user.username)
        bot.send_message(message.chat.id, "Successfully added user @" + str(message.from_user.username))

@bot.message_handler(content_types=['text'])
def random_shots(message):
    drinks = ["горілка", "пиво", "віскі", "самогон", "вино", "шампанське"]
    cocktails = []
    drink_after = ['пивом', 'водою', 'ревом', 'вином', 'не запиває']
    if(message.text.lower() in drinks):
        username_or_first_name = '@' + message.from_user.username if message.from_user.username != None else message.from_user.first_name
        
        drinks_or_not = [" п'є ", ' пропускає '][rm.randint(0, 1)]

        sentence = ""
        if drinks_or_not != ' пропускає ':
            percentage = rm.random()
            if percentage < 1.0:
                count_of_stopkas = 1
            if percentage < 1.0 - 1.0/3.0:
                count_of_stopkas = 2
            if percentage < 1.0/3.0:
                count_of_stopkas = 3

            drink = message.text.lower()
            
            definition = (' стопку ' if count_of_stopkas == 1 else ' стопки ' if count_of_stopkas in range(2, 5) else ' стопок ') if drink != 'пиво' else (' стакан ' if count_of_stopkas == 1 else ' стакана ')
            
            drink = drink[:len(drink) - 1] + 'и' if drink == 'горілка' else drink[:len(drink) - 1] + 'а' if drink == 'пиво' or drink == 'вино' else drink if drink == 'віскі' else drink + 'у' if drink == 'самогон' else drink[:len(drink) - 1] + 'ого' if drink == 'шампанське' else ''
            
            drink_after_idx = ""
            result_drink_after = ''
            if drink != 'пива':
                drink_after_idx = rm.randint(0, len(drink_after) - 1)
                result_drink_after = (' і запиває ' + drink_after[drink_after_idx]) if drink_after_idx < len(drink_after) - 1 else " і не запиває "
            
            sentence += str(count_of_stopkas) + definition + drink +result_drink_after

        bot.send_message(message.chat.id, username_or_first_name + drinks_or_not + sentence)
    if message.text.lower() == 'ти уйобище':
        bot.send_message(message.chat.id, 'мамка твоя уйобище')
    if message.text.lower() == 'бондар':
        with open('TY SHO.ogg', 'rb') as f:
            bot.send_voice(message.chat.id, f, reply_to_message_id=message.chat.id)
    if message.text.lower() == 'хуй':
        bot.send_message(message.chat.id, rm.choice(('Тобі по губам', 'мамці твоїй до рота', 'мені в зад')))
    if message.text == '300' or message.text.lower() == 'триста':
        bot.send_message(message.chat.id, 'отсоси у тракториста')

    

# @bot.message_handler(content_types=['voice'])
# def answer2(message):
#     bot.reply_to(message, 'знов записуєш свої ригачки')

list_of_people = []

bot.polling(True)
