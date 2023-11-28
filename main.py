import telebot
bot = telebot.TeleBot('6967649811:AAHLMaH62aafxkir60yPOoPHpfqT1K9qe08')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!', parse_mode='Markdown')
@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'для просмотра нажми на [ссылку](https://www.youtube.com/watch?v=WqGCbO4QW9k)', parse_mode='Markdown')
@bot.message_handler(commands=['stop'])
def main(message):
    bot.send_message(message.chat.id, 'До свидания!', parse_mode='Markdown')

bot.infinity_polling()