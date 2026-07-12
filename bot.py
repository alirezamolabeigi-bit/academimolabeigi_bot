from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "TOKEN_HERE"
CHANNEL = "@Tapsi_konkor"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"سلام {user.first_name} 👋\n"
        "برای دریافت فایل‌ها ابتدا عضو کانال شوید:\n"
        f"{CHANNEL}\n\n"
        "بعد از عضویت دوباره /start را بزنید."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if name == "main":
    main()
