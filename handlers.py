from telegram.ext import (
    Application,
    CommandHandler,
)

from config import BOT_TOKEN
from handlers import mission_handler


async def start(update, context):
    await update.message.reply_text(
        """
🐺 LUPUS NOCTIS

STRICT MODE ACTIVE

Type /mission to begin today's mission.
"""
    )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(mission_handler)

    print("🐺 Lupus Noctis Online")

    app.run_polling()


if __name__ == "__main__":
    main()