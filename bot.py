from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CopyTextButton,
)
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8954506479:AAEIQXRwypJVZaIGhfOSVJpr5kJLVgIeuLE"

ADMIN_USERNAME = "@Syedmahinislam"
CUSTOM_EMOJI_ID = "6242460902872850889"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                text="GET ADMIN",
                copy_text=CopyTextButton(
                    text=ADMIN_USERNAME
                ),
                style="success",
                icon_custom_emoji_id=CUSTOM_EMOJI_ID
            )
        ]
    ]

    await update.message.reply_text(
        "👤 Admin Username Copy করতে নিচের Button-এ চাপ দিন 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
