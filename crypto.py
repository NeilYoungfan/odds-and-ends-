import datetime
from secrets import API_TOKEN # Extra .py file saved locally to hide my Telegram API
from pycoingecko import CoinGeckoAPI
import telebot


# Get cryptocurrency prices from CoinGecko 
cg = CoinGeckoAPI()

btcusd = cg.get_price(ids=['bitcoin'], vs_currencies='usd')    
ethusd = cg.get_price(ids=['ethereum'], vs_currencies='usd')

btcgbp = cg.get_price(ids=['bitcoin'], vs_currencies='gbp')    
ethgbp = cg.get_price(ids=['ethereum'], vs_currencies='gbp')


# Get time and date from datetime
dt = datetime.datetime.now()
current_time = dt.strftime("%H:%M %d/%m/%Y")

# Send them to Telegram
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['usd'])
def send_welcome(message):
	bot.reply_to(message, f"Latest prices are:\n BTC: {btcusd}\n ETH: {ethusd} \n{current_time}")

@bot.message_handler(commands=['pound'])
def send_welcome(message):
	bot.reply_to(message, f"Latest prices are:\n BTC: {btcgbp}\n ETH: {ethgbp} \n{current_time}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

