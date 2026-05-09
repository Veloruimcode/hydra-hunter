import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

# Keys desde Railway Variables
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

print("🔥 HYDRA V4.0 RAILWAY ONLINE - BOT CONVERSACIONAL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 HYDRA ONLINE BUBU. Dime algo y te respondo con OpenAI.")

async def hablar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    print(f"User: {user_msg}")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres HYDRA. Responde directo, sin filtros, estilo callejero cubano. Breve y letal."},
                {"role": "user", "content": user_msg}
            ]
        )
        reply = response.choices[0].message.content
        await update.message.reply_text(reply)
        print(f"HYDRA: {reply}")
    except Exception as e:
        await update.message.reply_text(f"Error HYDRA: {e}")
        print(f"Error: {e}")

if __name__ == '__main__':
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hablar))
    print("Polling iniciado...")
    app.run_polling()