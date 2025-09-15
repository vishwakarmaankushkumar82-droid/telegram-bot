import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Environment Variables
TOKEN = os.environ.get("TELEGRAM_TOKEN")  # Render.com में TELEGRAM_TOKEN add होना चाहिए
ADMIN_ID = os.environ.get("ADMIN_ID")     # optional, अगर admin commands चाहिए

# Basic /start command
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(f"Hello {user.first_name}! Bot is running.")

# Error handler
def error(update: Update, context: CallbackContext):
    print(f"Update {update} caused error {context.error}")

def main():
    # Updater object
    updater = Updater(TOKEN, use_context=True)

    # Handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_error_handler(error)

    # Start bot using polling (simple for Render)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
