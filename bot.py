import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "🎉 **Hello, Photography Lover!** 🎉\n\n"
        "Welcome to *Photo Studio Bot*! 📸\n"
        "We’re here to make your memories shine ✨\n\n"
        "👇 Choose an option below to get started!"
    )
    
    website_markup = InlineKeyboardMarkup(row_width=2)
    website_markup.add(
        InlineKeyboardButton("🌐 Visit Our Website", url="https://example.com"),
        InlineKeyboardButton("📅 Book a Session", url="https://example.com/book"),
        InlineKeyboardButton("📸 Follow Us on Instagram", url="https://instagram.com/yourpage")
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=website_markup, parse_mode="Markdown")
    
    command_markup = InlineKeyboardMarkup(row_width=2)
    command_markup.add(
        InlineKeyboardButton("📋 Services", callback_data='services'),
        InlineKeyboardButton("📞 Contact Us", callback_data='contact'),
        InlineKeyboardButton("📝 Feedback", callback_data='feedback'),
        InlineKeyboardButton("ℹ️ Help", callback_data='help')
    )
    
    bot.send_message(message.chat.id, "👇 Choose another option:", reply_markup=command_markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'services':
        services(call.message)
    elif call.data == 'contact':
        contact(call.message)
    elif call.data == 'feedback':
        feedback(call.message)
    elif call.data == 'help':
        help(call.message)

@bot.message_handler(commands=['help'])
def help(message):
    help_text = (
        "💡 *Need some help?* No worries! Here's what you can do:\n\n"
        "🔹 `/start` - Meet the bot and explore options\n"
        "🔹 `/services` - See our amazing photo services 📸\n"
        "🔹 `/contact` - Get in touch with us ☎️\n"
        "🔹 `/feedback` - Tell us how we're doing! 🌟\n\n"
        "Let me know how I can assist you further! 😊"
    )
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

@bot.message_handler(commands=['services'])
def services(message):
    services_text = (
        "🎨 *Here’s what we do best:*\n\n"
        "1️⃣ *Wedding Photography* - Capturing your love story 💍\n"
        "2️⃣ *Birthday Parties* - Making every year memorable 🎂\n"
        "3️⃣ *Event Coverage* - Never miss a moment 🎉\n"
        "4️⃣ *Corporate Shoots* - Professional yet creative shots 💼\n\n"
        "✨ *Need more details?* Type `/contact` to connect with us!"
    )
    bot.send_message(message.chat.id, services_text, parse_mode="Markdown")

@bot.message_handler(commands=['contact'])
def contact(message):
    contact_info = (
        "📞 *Get in touch with us!*\n\n"
        "🔹 **Phone**: +123 45 678 901\n"
        "🔹 **Email**: photostudio@example.com\n\n"
        "We’re excited to hear from you! ✨"
    )
    bot.send_message(message.chat.id, contact_info, parse_mode="Markdown")

@bot.message_handler(commands=['feedback'])
def feedback(message):
    feedback_text = (
        "🌟 *We’d love to hear your thoughts!*\n\n"
        "Let us know how we can improve or just share your experience with us. ✍️\n\n"
        "Type your feedback below, and we’ll make sure it gets to the right people!"
    )
    bot.send_message(message.chat.id, feedback_text, parse_mode="Markdown")

@bot.message_handler(content_types=['photo'])
def handle_photos(message):
    bot.send_message(
        message.chat.id, 
        "📷 *Wow!* Thanks for sharing a photo. Let us know if you’d like to book a session!"
    )

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(
        message.chat.id,
        "🤔 *Oops! I didn’t quite get that.*\n\n"
        "Type `/help` to see all the amazing things I can do! 😊",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    while True:
        try:
            print("Bot is running.")
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"⚠️ Error occurred: {e}")
