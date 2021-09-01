import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

@run_async
def start(update: Update, context: CallbackContext):    
    user = update.effective_user
    update.message.reply("
What do you want to Request?
Choose from Give Options Below
━━━━━━━━━━━━━━━━━━━━━━━
» Walls - Anime Wallpapers
» Anime - Anime and Anime Movies
» Music - Anime Music (OP/ED/OST)
» Manga - Manga or Manhwas
» Themes - Custom Made Telegram Themes
» Stickers - Custom Made Sticker Packs
» Post - Post Your Art/AMVs/Memes on @Anime_Heaven_Official
━━━━━━━━━━━━━━━━━━━━━━━
 ")

buttons = [
    [        
        InlineKeyboardButton(
        text="Anime", callback_data="anime_"
        ),
    ],    
]


@run_async
def bot_about_callback(update, context):
    query = update.callback_query
    if query.data == "anime_":
        animee = client.ask(text= "Tell the Name of Anime You Want to Request".)
    

 
