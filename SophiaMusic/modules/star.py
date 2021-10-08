from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> Hi there,👋 {message.from_user.first_name}!
\nThis is Glitter Music Bot.
Saya memutar musik di Obrolan Suara Telegram.
\nFo More Help Use Buttons Below:
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥂 DONATUR 🥂", url="https://t.me/Biarenakliatnyaaa")
                  ],[
                    InlineKeyboardButton(
                        "💬 CHANNEL", url="https://t.me/storeglitter"
                    ),
                    InlineKeyboardButton(
                        "💻 GROUP", url="https://t.me/Virtuallnihboss"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ TAMBAHKAN SAYA KE GROUP ➕", url="https://t.me/DemusGlitterBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**BOT MUSIC GLITTER AKTIF.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 UPDATES CHANNEL", url="https://t.me/storeglitter")
                ]
            ]
        )
   )
