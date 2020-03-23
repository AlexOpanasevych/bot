import telebot as tbot
import random as rm
import os

TOKEN = os.environ['BOT_TOKEN']
API_URL = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN

bot = tbot.TeleBot(TOKEN)

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = tbot.types.InlineQueryResultArticle('1', 'Result1', tbot.types.InputTextMessageContent('1'))
        r2 = tbot.types.InlineQueryResultArticle('2', 'Result2', tbot.types.InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, (r, r2))
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    try:
        r = tbot.types.InlineQueryResultArticle('1', 'Google', tbot.types.InputTextMessageContent('google'), url='https://google.com', hide_url=True)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, "hello bitch")

@bot.message_handler(commands=['help'])
def start_msg(message):
    bot.send_message(message.chat.id, "/who - who dies from covid-19 today?\n")

@bot.message_handler(commands=['who'])
def start_msg(message):
    members_count = bot.get_chat_members_count(message.chat.id)
    print(members_count)
    bot.send_message(message.chat.id, 'developing...')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'ти уйобище':
        bot.send_message(message.chat.id, 'мамка твоя уйобище')
    if message.text.lower() == 'гендзюцу':
        with open('papi4_dota/gendzhycy.wav', 'rb') as f:
            bot.send_voice(message.chat.id, f, reply_to_message_id=message.chat.id)
    if message.text.lower() == 'на':
        with open('papi4_dota/HAAAAAA.wav', 'rb') as f:
            bot.send_voice(message.chat.id, f, reply_to_message_id=message.chat.id)
    if message.text.lower() == 'резать':
        with open('papi4_dota/budu rezat\'.wav', 'rb') as f:
            bot.send_voice(message.chat.id, f, reply_to_message_id=message.chat.id)
    if message.text.lower() == 'мусор':
        with open('papi4_dota/faking tresh.wav', 'rb') as f:
            bot.send_voice(message.chat.id, f, reply_to_message_id=message.chat.id)
    if message.text.lower() == 'соль':
        with open('papi4_dota/V SOLYANOGO.wav', 'rb') as f:
            bot.send_voice(message.chat.id, f, reply_to_message_id=message.chat.id)
    if message.text.lower() == 'бондар':
        with open('TY SHO.ogg', 'rb') as f:
            bot.send_voice(message.chat.id, f, reply_to_message_id=message.chat.id)
    if message.text.lower() == 'хуй':
        bot.send_message(message.chat.id, rm.choice(('Тобі по губам', 'мамці твоїй до рота', 'мені в зад')))
    if message.text == '300' or message.text.lower() == 'триста':
        bot.send_message(message.chat.id, 'отсоси у тракториста')

@bot.message_handler(content_types=['voice'])
def answer(message):
    bot.reply_to(message, 'знов записуєш свої ригачки')





bot.polling(True)
