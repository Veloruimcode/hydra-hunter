import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from openai import OpenAI

TOKEN = os.environ["TELEGRAM_TOKEN"]
OPENAI_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_KEY)

print("🔥 HYDRA V4.3 RAILWAY STABLE ONLINE")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("HYDRA online. Envíame un mensaje y te responderé.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    print(f"USER: {user_msg}")
    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente útil. Responde de forma clara, concisa y directa."},
                {"role": "user", "content": user_msg}
            ]
        )
        reply = r.choices[0].message.content
        await update.message.reply_text(reply)
        print(f"HYDRA: {reply}")
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        await update.message.reply_text(error_msg)
        print(error_msg)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("Polling iniciado...")
    await app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.run(main())