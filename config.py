

import re, os, time

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21857983")
    API_HASH  = os.environ.get("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7508789523:AAE_0EYz7_E_FkI-hyXbtSnN5Axekmz-CqY") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://dhimanrajat:Y8IAGI0lVrMhjvkU@cluster0.mytkgu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/nxK.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '833465134').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    PORT = os.environ.get("PORT", "6060")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    FILES_CHANNEL = int(os.environ.get("FILES_CHANNEL", ""))
    USER_REPLY_TEXT = "Your Are Not Authorised To use me Contact @ItzMonkeyDLuffy to use me "

    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<blockquote expandable><b>Hɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : MonKey D.Luffy ⚡</b></blockquote>"""
    
    FILE_NAME_TXT = """
    <u><b>SETUP AUTO RENAME FORMAT</b></u>\n\nUse These Keywords To Setup Custom File Name\n\n➝ episode :- to replace episode number\n➝ quality :- to replace video resolution\n\n‣ <b>Example :</b> /autorename  One Piece - EPepisode [quality] [Sub] @AnimeStation2.mkv\n\n‣ <b>Your Current Rename Format :</b> {format_template}
    """
    
    ABOUT_TXT = f"""
<b>╔════════════⦿
├⋗ ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/ItzMonkeyDLuffy'>ᴍᴏɴᴋᴇʏ ᴅ.ʟᴜꜰꜰʏ</a>
├⋗ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>
├⋗ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
├⋗ Main Channel : <a href='https://t.me/AnimeStation2'>Anime Channel</a>
├⋗ Support Group : <a href='https://t.me/Animestation_Chat_Group'>Group Chat</a>
╚═════════════════⦿</b>
"""

    ABOUTS_TXT = """ Just A normal Auto Rename Bot Working For Anime Station"""

    
    THUMB_TXT = """ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ
➜ /start: ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ..
➜ /del_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
➜ /view_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
ɴᴏᴛᴇ: ɪꜰ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ɪɴ ʙᴏᴛ ᴛʜᴇɴ, ɪᴛ ᴡɪʟʟ ᴜꜱᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴛʜᴇ ᴏʀɪɢɪɴɪᴀʟ ꜰɪʟᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ"""
    

    PREMIUM_TXT = """✨ Pʀᴇᴍɪᴜᴍ Bᴇɴᴇғɪᴛs ✨

Uᴘɢʀᴀᴅᴇ ᴛᴏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴇɴJᴏʏ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs:
➲ Uɴʟɪᴍɪᴛᴇᴅ Rᴇɴᴀᴍɪɴɢ: ʀᴇɴᴀᴍᴇ ᴀs ᴍᴀɴʏ ғɪʟᴇs ᴀs ʏᴏᴜ ᴡᴀɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
➲ Eᴀʀʟʏ Aᴄᴄᴇss: ʙᴇ ᴛʜᴇ ғɪʀsᴛ ᴛᴏ ᴛᴇsᴛ ᴀɴᴅ ᴜsᴇ ᴏᴜʀ ʟᴀᴛᴇsᴛ ғᴇᴀᴛᴜʀᴇs ʙᴇғᴏʀᴇ ᴀɴʏᴏɴᴇ ᴇʟsᴇ.

Pʀɪᴄɪɴɢ:
➜ Contact:- @ItzMonkeyDLuffy

Uɴʟᴏᴄᴋ ᴛʜᴇ ғᴜʟʟ ᴘᴏᴛᴇɴᴛɪᴀʟ ᴏғ ᴏᴜʀ ʀᴇɴᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss. Sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴀɴᴅ sᴜᴘᴇʀᴄʜᴀʀɢᴇ ʏᴏᴜʀ ғɪʟᴇ ʀᴇɴᴀᴍɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ! ⚡️

Tᴏ sᴜʙsᴄʀɪʙᴇ, sɪᴍᴘʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴏᴜʀ ᴅᴇᴠᴇʟᴏᴘᴇʀ ʙᴇʟᴏᴡ."""


    COMMANDS_TXT = """<b>✨Auto Rename Bot🫧
 ʙᴏᴛ ɪꜱ ᴀ ʜᴀɴᴅʏ ᴛᴏᴏʟ ᴛʜᴀᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ᴀᴜᴛᴏʀᴇɴᴀᴍᴇ ʙʏ ɢɪᴠɪɴɢ ᴄᴏᴍᴍᴀɴᴅ /Aᴜᴛᴏʀᴇɴᴀᴍᴇ [Yᴏᴜʀ ғᴏʀᴍᴀᴛ] ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.
ɪᴍᴘᴏʀᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:
➲ /Autorename: ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ.
➲ /View_Thumb: ᴛᴏ sᴇᴇ ᴄᴏᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /Setmedia: sᴇᴛ ʏᴏᴜʀ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ."""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
