from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("8856649724:AAHJmY-oEpz2mYrA7DSHsmETi6-KtHY_IiI")

OWNER_ID = 8362679329

CHANNELS = {
    -1003899735484: "https://t.me/+73AkcDQWwqNlMzJl"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    not_joined = []

    # Owner notification
    try:
        await context.bot.send_message(
            chat_id=OWNER_ID,
            text=f"New user 🚀\nName: {user.first_name}\nID: {user.id}"
        )
    except Exception as e:
        print(e)

    # Join check
    for chat_id, link in CHANNELS.items():
        try:
            member = await context.bot.get_chat_member(chat_id, user.id)
            if member.status not in ["member", "administrator", "creator"]:
                raise Exception("Not joined")
        except:
            not_joined.append(link)

    if not_joined:
        keyboard = [[InlineKeyboardButton("Join 🔥", url=link)] for link in not_joined]
        await update.message.reply_text(
            "Join all channels 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    await update.message.reply_text("Welcome 😎")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
