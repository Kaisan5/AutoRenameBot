from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Config
from helper.database import db


async def not_subscribed(_, client, message):
    BANNED = False
    await db.add_user(client, message)
    if not Config.FORCE_SUB:
        return False
    try:
        for force_sub in Config.FORCE_SUB.split(' '):
            user = await client.get_chat_member(force_sub, message.from_user.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                BANNED = True
            else:
                BANNED = False
        return BANNED
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = []
    BANNED = False
    for idx, forces_sub in enumerate(Config.FORCE_SUB.split(' ')):
        buttons.append([InlineKeyboardButton(text=f"📢 {idx+1} Join Update Channel 📢", url=f"https://t.me/{forces_sub}")])
    text = "**Sᴏʀʀy Dᴜᴅᴇ Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Aʟʟ Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟs Tᴏ Cᴏɴᴛɪɴᴜᴇ**"
    try:
        for forcesub in Config.FORCE_SUB.split(' '):
            user = await client.get_chat_member(forcesub, message.from_user.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                BANNED = True
            
            else:
                BANNED = False
        
        if BANNED:
            return await client.send_message(message.from_user.id, text="Sᴏʀʀy Yᴏᴜ'ʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ")
    except UserNotParticipant:
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
