import os
import telebot
from telebot import types
from google_trans_new import google_translator


# =========================
# Bot Configuration
# =========================

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

bot = telebot.TeleBot(BOT_TOKEN)
translator = google_translator()


# =========================
# Supported Languages
# =========================

LANGUAGES = {
    "🇺🇿 Uzbek": "uz",
    "🇷🇺 Russian": "ru",
    "🇬🇧 English": "en",
    "🇹🇷 Turkish": "tr",
    "🇫🇷 French": "fr",
    "🇩🇪 German": "de",
    "🇪🇸 Spanish": "es",
    "🇮🇹 Italian": "it",
    "🇸🇦 Arabic": "ar",
}


# This dictionary stores users' last messages
user_messages = {}


# =========================
# Keyboard Function
# =========================

def create_language_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    buttons = [
        types.InlineKeyboardButton(text=language, callback_data=code)
        for language, code in LANGUAGES.items()
    ]

    keyboard.add(*buttons)
    return keyboard


# =========================
# Start Command
# =========================

@bot.message_handler(commands=["start"])
def send_welcome(message):
    welcome_text = (
        "👋 Welcome to Translator Bot!\n\n"
        "Send me any text, and I will translate it into the language you choose."
    )

    bot.send_message(message.chat.id, welcome_text)


# =========================
# Message Handler
# =========================

@bot.message_handler(content_types=["text"])
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    user_messages[chat_id] = text

    bot.send_message(
        chat_id,
        f"Your text:\n\n{text}\n\nChoose a language:",
        reply_markup=create_language_keyboard()
    )


# =========================
# Callback Handler
# =========================

@bot.callback_query_handler(func=lambda call: True)
def handle_language_selection(call):
    chat_id = call.message.chat.id
    language_code = call.data

    original_text = user_messages.get(chat_id)

    if not original_text:
        bot.send_message(chat_id, "Please send a text first.")
        return

    try:
        translated_text = translator.translate(original_text, lang_tgt=language_code)

        language_name = get_language_name(language_code)

        response = (
            f"Original text:\n{original_text}\n\n"
            f"Translated to {language_name}:\n{translated_text}"
        )

        bot.send_message(chat_id, response)

    except Exception as error:
        bot.send_message(
            chat_id,
            "Sorry, something went wrong while translating your text."
        )
        print(f"Translation error: {error}")


# =========================
# Helper Function
# =========================

def get_language_name(language_code):
    for language_name, code in LANGUAGES.items():
        if code == language_code:
            return language_name

    return language_code


# =========================
# Run Bot
# =========================

if __name__ == "__main__":
    print("Translator bot is running...")
    bot.polling(none_stop=True)
