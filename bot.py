from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐺 Lupus Noctis Activated.\n\nMission initialized.\nDiscipline Mode: STRICT."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Lupus Noctis is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
