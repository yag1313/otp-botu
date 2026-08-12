import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8631181439:AAGLUotPA5aymRTMEStSKaatZVT18HSjNgg"
CHAT_ID = "8008360585"

# Şimdilik örnek OTP
def get_latest_sms():
    return "Örnek OTP: 123456"

async def start(update, update, context):
    await update.message.reply_text("✅ OTP Bot aktif! /check ile OTP sorgula.")

async def check(update, context):
    otp = get_latest_sms()
    await update.message.reply_text(f"📩 Gelen OTP: {otp}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check", check))
    print("🚀 Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()
