import random
import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Securely get bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing! Set it in the environment variables.")

# Lists for random responses
love_messages = [
    "You are the reason I smile every day ❤️",
    "My heart beats only for you 💖",
    "Every moment with you is special 💕",
    "You make my life beautiful 🌹",
    "I love you more than words can say 😘"
]

hug_gifs = [
    "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
    "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
    "https://media.giphy.com/media/wnsgren9NtITS/giphy.gif"
]

kiss_gifs = [
    "https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif",
    "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif",
    "https://media.giphy.com/media/KH1CTZtw1iP3W/giphy.gif"
]

date_ideas = [
    "Candlelight dinner at home 🍽️✨",
    "Late-night drive with your favorite songs 🎶",
    "Picnic in the park 🌳🥪",
    "Stargazing together 🌌💫",
    "Movie night with cozy blankets 🎬🍿"
]

secrets = [
    "I told her about my bullying past...",
    "Diwali - she sent me a pic in red suit...",
    "My ex returned out of nowhere...",
    "I loved it when she asked me...",
    "When Nikku gave her a dare...",
    "When I asked if we should keep the PFP...",
    "When people shipped me with her...",
    "When she sent the reel with a date...",
    "I once told her that Anam asked me...",
    "This one's embarrassing but when we started talking...",
    "When we were in the double date GC...",
    "Whenever she's making something and says 'Aajao Khila Dungi'..."
]

special_message = "Will you be my Valentine? Not only this year but for the rest of my life? ❤️"

stored_images = {}

# Command Handlers
async def love(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(love_messages))

async def hug(update: Update, context: CallbackContext):
    await update.message.reply_animation(random.choice(hug_gifs))

async def kiss(update: Update, context: CallbackContext):
    await update.message.reply_animation(random.choice(kiss_gifs))

async def date(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(date_ideas))

async def sticker(update: Update, context: CallbackContext):
    await update.message.reply_sticker("CAACAgUAAxkBAAEKGlxlE8mQzJvXjwxXJd8RUqHugOwRYAACQAkAAvoLtFSVjeGxNkZMjLQE")  # Example sticker ID

async def secret(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(secrets))

async def mylove(update: Update, context: CallbackContext):
    if update.message.from_user.username == "your_mo0nlightt":
        await update.message.reply_text(special_message)
    else:
        await update.message.reply_text("This message is only for Ritika! ❤️")

async def store(update: Update, context: CallbackContext):
    if update.message.reply_to_message and update.message.reply_to_message.photo:
        file_id = update.message.reply_to_message.photo[-1].file_id
        stored_images[len(stored_images) + 1] = file_id
        await update.message.reply_text(f"Image saved as {len(stored_images)}")
    else:
        await update.message.reply_text("Please reply to an image to store it.")

async def list_images(update: Update, context: CallbackContext):
    if not stored_images:
        await update.message.reply_text("No images stored yet.")
    else:
        img_list = "\n".join([f"{num}: Image" for num in stored_images.keys()])
        await update.message.reply_text(f"Stored images:\n{img_list}")

async def sendimg(update: Update, context: CallbackContext):
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /sendimg <image number>")
        return

    img_number = int(context.args[0])
    if img_number in stored_images:
        await update.message.reply_photo(stored_images[img_number])
    else:
        await update.message.reply_text("Invalid image number.")

# Main Function
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("love", love))
    app.add_handler(CommandHandler("hug", hug))
    app.add_handler(CommandHandler("kiss", kiss))
    app.add_handler(CommandHandler("date", date))
    app.add_handler(CommandHandler("sticker", sticker))
    app.add_handler(CommandHandler("secret", secret))
    app.add_handler(CommandHandler("mylove", mylove))
    app.add_handler(CommandHandler("store", store))
    app.add_handler(CommandHandler("list", list_images))
    app.add_handler(CommandHandler("sendimg", sendimg))

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
