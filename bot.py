import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is working ✅")

def main():
    token = os.getenv("TELEGRAM_TOKEN")  # Token environment variable se milega
    if not token:
        print("❌ Error: TELEGRAM_TOKEN not found!")
        return

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
