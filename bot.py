import telebot

API_TOKEN = "7731566512:AAHyqNaYNyzOnvWUuxHoCy04PZNiXcxiI04"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Bạn vừa nhắn: {message.text}")

print("Bot is running...")
bot.infinity_polling()
