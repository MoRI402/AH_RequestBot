from pyrogram import Client, filters
from pyrogram import Client

app = from pyrogram import Client

app = Client(
    "my_bot",
    bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
)

@app.on_message(filters.command('start'))
async def main(client, message):
    await message.reply_text()


app.run()
