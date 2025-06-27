
import telebot
import schedule
import time
import threading
from youtube_reel import get_spanish_reel

TELEGRAM_BOT_TOKEN = "7225764693:AAHD0uXaR49pUCkoe2_bbHBfDAceNFrr66M"
CHAT_ID = "1162610813"  # Replace with your own chat/channel ID

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)



@bot.message_handler(commands=["start"])
def greet_user(message):
    print("🟢 Received /start command")
    bot.send_message(
        message.chat.id,
        "¡Hola! 👋 Welcome to *Dímelo* – your Spanish Reels Buddy 🇪🇸\n\nSend /reel anytime to get a new Spanish reel on food, culture, slang, and more.",
        parse_mode="Markdown"
    )


# Command to manually fetch reel
@bot.message_handler(commands=["reel"])
def send_reel_now(message):
    reel = get_spanish_reel()
    bot.send_message(message.chat.id, f"🎥 Spanish Reel:\n{reel}")

# Scheduled task
def scheduled_reel():
    reel = get_spanish_reel()
    bot.send_message(CHAT_ID, f"📌 Scheduled Reel:\n{reel}")

# Schedule jobs (24-hour format)
schedule.every().day.at("09:00").do(scheduled_reel)
schedule.every().day.at("15:00").do(scheduled_reel)
schedule.every().day.at("21:00").do(scheduled_reel)

# Background thread for scheduler
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start scheduler in background
threading.Thread(target=run_schedule).start()

# Start bot
print("🤖 Bot is running...")
bot.infinity_polling()
