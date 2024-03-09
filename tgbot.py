import telebot
TOKEN = "7048836769:AAEv_2XDOETUksLXAQWzOCnmDjp9YsEexw8"
bot_token = TOKEN
bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()