import telebot

# --- 1. Вставьте свой токен ---
# Замените 'ВАШ_ТОКЕН_БОТА' на токен, который вы получили от @BotFather
TOKEN = 'ВАШ_ТОКЕН_БОТА'
bot = telebot.TeleBot(TOKEN)

# --- 2. Обработчик команды /start ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Отвечает на команду /start
    """
    # message.chat.id - ID чата, куда отправлять сообщение
    bot.send_message(message.chat.id, 
                     "Привет! Я простой эхо-бот. Отправь мне любое сообщение, и я его повторю.")

# --- 3. Обработчик любых текстовых сообщений (ЭХО) ---
@bot.message_handler(content_types=['text'])
def echo_all(message):
    """
    Повторяет (эхо) любое текстовое сообщение
    """
    # message.text - текст сообщения
    bot.send_message(message.chat.id, message.text)

# --- 4. Запуск бота ---
# Бот начинает "слушать" новые сообщения
print("Бот запущен. Нажмите Ctrl+C для остановки.")
bot.polling(none_stop=True)


