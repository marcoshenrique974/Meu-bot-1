import telebot
import time

TOKEN = "8695556395:AAENrSmp8ABW9SFhEaNEGWxB-HD-zfLREIY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Bot funcionando!")

print("Bot rodando...")
while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(15)
