import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

users = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     'Добро пожаловать в бота сбора обратной связи! Введие своё имя')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)


def save_username(message):
    chat_id = message.chat.id
    name = message.text
    users[chat_id]['name'] = name
    bot.send_message(chat_id, f'Отлично, {name}. Теперь укажи свою фамилию')
    bot.register_next_step_handler(message, save_surname)


def save_surname(message):
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname
    bot.send_message(chat_id, f'Ваши данные успешно сохранены!')


@bot.message_handler(commands=['who_i'])
def who_i(message):
    chat_id = message.chat.id
    name = users[chat_id]['name']
    surname = users[chat_id]['surname']
    bot.send_message(chat_id, f'Вы: {name} {surname}')


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
