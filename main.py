import os
from telebot import TeleBot
from dotenv import load_dotenv
from telebot.types import Message

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN: str = os.getenv('8088305768:AAEOB7f893L-57dADMyAh32gTApX8iPgFY8')

# Initialize bot
bot = TeleBot(token=TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    """ Handles the /start command by sending a "Hello world!" message in response. """
    chat_id = message.chat.id
    bot.send_message(chat_id, "ghb")


@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    """Echo the user message."""
    chat_id = message.chat.id
    bot.send_message(chat_id, message.text)


bot.infinity_polling()

