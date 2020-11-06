import datetime
import telebot
from telebot import types
bot = telebot.TeleBot('1270195113:AAF5Ez7-56YoMlyZ-7Twgyl9LKE4CUhmtU4')
@bot.message_handler(content_types=['text'])


def sells_today(message):
    if message.text == "/start":    
        bot.send_message(message.chat.id, "Привет!!!\nЭто бот, который определяет продавца воды\n\nЧтобы начать воспользуйтесь кнопками или командами \n\nСписок доступных команд можно вызвать с помощью /help")
        but_message(message)
    elif message.text == "/help":  
        bot.send_message(message.chat.id, "/who_sells_today - рассчитывает, кто продавец сегодня \n\n/who_sells_at_date - рассчитывает, кто продавец в заданный день")
    elif message.text == "/who_sells_today":
        day_calculator(datetime.datetime.now().date(), message)
        but_message(message)
    elif message.text == "/who_sells_at_date":
        msg = bot.send_message(message.chat.id, "Введите дату нужного дня в формате:\n\n*01 01 1999*", parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, date_func)
        but_message(message)
    else:
        bot.send_message(message.from_user.id, "Не понимаю вас, воспользуйтесь кнопками или командами из /help")


def but_message(message):
        keyboard = types.InlineKeyboardMarkup()
        key_today = types.InlineKeyboardButton(text= 'Сегодня', callback_data = 'today')
        keyboard.add(key_today)
        key_date = types.InlineKeyboardButton(text= 'В другой день', callback_data = 'date')
        keyboard.add(key_date)
        bot.send_message(message.from_user.id, text="И так, когда вы пойдете покупать воду ?", reply_markup=keyboard)

def but_message_but(call):
        keyboard = types.InlineKeyboardMarkup()
        key_today = types.InlineKeyboardButton(text= 'Сегодня', callback_data = 'today')
        keyboard.add(key_today)
        key_date = types.InlineKeyboardButton(text= 'В другой день', callback_data = 'date')
        keyboard.add(key_date)
        bot.send_message(call.message.chat.id, text="И так, когда вы пойдете покупать воду ?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)


def callback_worker(call):
    if call.data == "today":
        day_calculator_but(datetime.datetime.now().date(), call)
        but_message_but(call)
    elif call.data == 'date':
        msg = bot.send_message(call.message.chat.id, "Введите дату нужного дня в формате:\n\n*01 01 1999*", parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, date_func)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


def date_func(message):
        date = message.text.split(" ")
        day_calculator(datetime.date(int(date[2]), int(date[1]), int(date[0])), message)
        but_message(message)


def day_calculator(input_point, message):
    base_point = datetime.date(2020, 10, 27)
    if base_point >= input_point:
        while input_point < base_point:
            input_point = input_point + datetime.timedelta(days=2)
        if input_point == base_point:
            bot.send_message(message.chat.id, "\U0001F478 _Добрая королева разливает воду из источника_", parse_mode='MarkdownV2')
        else: 
            bot.send_message(message.chat.id, "\U0001F479 _У источника дежурит злобный огр_", parse_mode='MarkdownV2')

    elif base_point <= input_point:
        while input_point > base_point:
            input_point = input_point - datetime.timedelta(days=2)
        if input_point == base_point:
            bot.send_message(message.chat.id, "\U0001F478 _Добрая королева разливает воду из источника_", parse_mode='MarkdownV2')
        else: 
            bot.send_message(message.chat.id, "\U0001F479 _У источника дежурит злобный огр_", parse_mode='MarkdownV2')


def day_calculator_but(input_point, call):
    base_point = datetime.date(2020, 10, 27)
    if base_point >= input_point:
        while input_point < base_point:
            input_point = input_point + datetime.timedelta(days=2)
        if input_point == base_point:
            bot.send_message(call.message.chat.id, "\U0001F478 _Добрая королева разливает воду из источника_", parse_mode='MarkdownV2')
        else: 
            bot.send_message(call.message.chat.id, "\U0001F479 _У источника дежурит злобный огр_", parse_mode='MarkdownV2')

    elif base_point <= input_point:
        while input_point > base_point:
            input_point = input_point - datetime.timedelta(days=2)
        if input_point == base_point:
            bot.send_message(call.message.chat.id, "\U0001F478 _Добрая королева разливает воду из источника_", parse_mode='MarkdownV2')
        else: 
            bot.send_message(call.message.chat.id, "\U0001F479 _У источника дежурит злобный огр_", parse_mode='MarkdownV2')

bot.polling(none_stop=True, interval=5)


