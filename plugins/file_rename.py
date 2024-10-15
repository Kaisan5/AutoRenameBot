from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InputMediaDocument, Message
from PIL import Image
from datetime import datetime

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from helper.utils import progress_for_pyrogram, humanbytes, convert
from helper.database import db
from helper.database import madflixbotz
from config import Config

import os
import time
import re

FILES_CHANNEL = Config.FILES_CHANNEL

renaming_operations = {}

# Patterns for episode and quality extraction
patterns = {
    'pattern1': re.compile(r'S(\d+)(?:E|EP)(\d+)'),
    'pattern2': re.compile(r'S(\d+)\s*(?:E|EP|-\s*EP)(\d+)'),
    'pattern3': re.compile(r'(?:[([<{]?\s*(?:E|EP)\s*(\d+)\s*[)\]>}]?)'),
    'pattern3_2': re.compile(r'(?:\s*-\s*(\d+)\s*)'),
    'pattern4': re.compile(r'S(\d+)[^\d]*(\d+)', re.IGNORECASE),
    'patternX': re.compile(r'(\d+)'),
    'pattern5': re.compile(r'\b(?:.*?(\d{3,4}[^\dp]*p).*?|.*?(\d{3,4}p))\b', re.IGNORECASE),
    'pattern6': re.compile(r'[([<{]?\s*4k\s*[)\]>}]?', re.IGNORECASE),
    'pattern7': re.compile(r'[([<{]?\s*2k\s*[)\]>}]?', re.IGNORECASE),
    'pattern8': re.compile(r'[([<{]?\s*HdRip\s*[)\]>}]?|\bHdRip\b', re.IGNORECASE),
    'pattern9': re.compile(r'[([<{]?\s*4kX264\s*[)\]>}]?', re.IGNORECASE),
    'pattern10': re.compile(r'[([<{]?\s*4kx265\s*[)\]>}]?', re.IGNORECASE)
}

def extract_quality(filename):
    for i in range(5, 11):
        match = re.search(patterns[f'pattern{i}'], filename)
        if match:
            quality = match.group(1) or match.group(2)
            print(f"Matched Pattern {i} with quality: {quality}")
            return quality
    print("Quality: Unknown")
    return "Unknown"

def extract_episode_number(filename):
    for i in range(1, 5):
        match = re.search(patterns[f'pattern{i}'], filename)
        if match:
            episode_number = match.group(2) if i == 1 else match.group(1)
            print(f"Matched Pattern {i} with episode: {episode_number}")
            return episode_number
    match = re.search(patterns['patternX'], filename)
    if match:
        print("Matched Pattern X with episode: " + match.group(1))
        return match.group(1)
    print("Episode: Unknown")
    return None

# Example usage
filename = "One Piece S1-07 [720p][Dual] @Anime_Edge.mkv"
episode_number = extract_episode_number(filename)
print(f"Extracted Episode Number: {episode_number}")

@Client.on_message(filters.private & filters.command("autorename"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id
    format_template = message.text.split("/autorename", 1)[1].strip()
    await madflixbotz.set_format_template(user_id, format_template)
    await message.reply_text("Auto rename format updated successfully!")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    user_id = message.from_user.id
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()
    await db.set_media_preference(user_id, media_type)
    await message.reply_text(f"Media preference set to: {media_type}")

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def auto_rename_files(client, message):
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    format_template = await db.get_format_template(user_id)
    media_preference = await db.get_media_preference(user_id)

    if not format_template:
        return await message.reply_text("Please set an auto rename format first using /autorename")

    if message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
        media_type = media_preference or "document"
    elif message.video:
        file_id = message.video.file_id
        file_name = f"{message.video.file_name}.mp4"
        media_type = media_preference or "video"
    elif message.audio:
        file_id = message.audio.file_id
        file_name = f"{message.audio.file_name}.mp3"
        media_type = media_preference or "audio"
    else:
        return await message.reply_text("Unsupported file type")

    print(f"Original File Name: {file_name}")
    logs_caption = f"{firstname}\n{user_id}\n\n**{file_name}**"
    await client.send_document(FILES_CHANNEL, document=file_id, caption=logs_caption)

    if file_id in renaming_operations:
        elapsed_time = (datetime.now() - renaming_operations[file_id]).seconds
        if elapsed_time < 10:
            print("File is being ignored as it is currently being renamed or was renamed recently.")
            return

    renaming_operations[file_id] = datetime.now()

    episode_number = extract_episode_number(file_name)
    print(f"Extracted Episode Number: {episode_number}")

    if episode_number:
        placeholders = ["episode", "Episode", "EPISODE", "{episode}"]
        for placeholder in placeholders:
            format_template = format_template.replace(placeholder, str(episode_number), 1)

        quality_placeholders = ["quality", "Quality", "QUALITY", "{quality}"]
        for quality_placeholder in quality_placeholders:
            if quality_placeholder in format_template:
                extracted_qualities = extract_quality(file_name)
                if extracted_qualities == "Unknown":
                    await message.reply_text("I wasn't able to extract the quality properly. Renaming as 'Unknown'...")
                    del renaming_operations[file_id]
                    return
                format_template = format_template.replace(quality_placeholder, "".join(extracted_qualities))

        _, file_extension = os.path.splitext(file_name)
        new_file_name = f"{format_template}{file_extension}"
        file_path = f"downloads/{new_file_name}"
        file = message

        download_msg = await message.reply_text(text="Trying to download...")
        try:
            path = await client.download_media(message=file, file_name=file_path, progress=progress_for_pyrogram, progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", download_msg, time.time()))
        except Exception as e:
            del renaming_operations[file_id]
            return await download_msg.edit(e)

        duration = 0
        try:
            metadata = extractMetadata(createParser(file_path))
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
        except Exception as e:
            print(f"Error getting duration: {e}")

        # Extract additional metadata
        metadata_info = {}
        try:
            metadata = extractMetadata(createParser(file_path))
            if metadata:
                for data in metadata.exportPlaintext():
                    key, value = data.split(': ', 1)
                    metadata_info[key] = value.strip()
        except Exception as e:
            print(f"Error extracting metadata: {e}")

        upload_msg = await download_msg.edit("Trying to uploading....")
        ph_path = None
        c_caption = await db.get_caption(message.chat.id)
        c_thumb = await db.get_thumbnail(message.chat.id)

        caption = c_caption.format(
            filename=new_file_name,
            filesize=humanbytes(message.document.file_size),
            duration=convert(duration),
            metadata="\n".join([f"{key}: {value}" for key, value in metadata_info.items()])
        ) if c_caption else f"**{new_file_name}**"

        if c_thumb:
            ph_path = await client.download_media(c_thumb)
            print(f"Thumbnail downloaded successfully. Path: {ph_path}")
        elif media_type == "video" and message.video.thumbs:
            ph_path = await client.download_media(message.video.thumbs[0].file_id)

        if ph_path:
            Image.open(ph_path).convert("RGB").save(ph_path)
            img = Image.open(ph_path)
            img.resize((320, 320))
            img.save(ph_path, "JPEG")
            logs_caption2 = f"{firstname}\n{user_id}\n{new_file_name}"
            await client.send_document(FILES_CHANNEL, document=file_path, thumb=ph_path, caption=logs_caption2)

        try:
            if media_type == "document":
                await client.send_document(
                    message.chat.id,
                    document=file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=("Upload Started....", upload_msg, time.time())
                )
            elif media_type == "video":
                await client.send_video(
                    message.chat.id,
                    document=file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=("Upload Started....", upload_msg, time.time())
                )
            type = media_type  # Use 'media_type' variable instead
            if type == "document":
                await client.send_document(
                    message.chat.id,
                    document=file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=("Upload Started....", upload_msg, time.time())
                )
            elif type == "video":
                await client.send_video(
                    message.chat.id,
                    video=file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=("Upload Started....", upload_msg, time.time())
                )
            elif type == "audio":
                await client.send_audio(
                    message.chat.id,
                    audio=file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=("Upload Started....", upload_msg, time.time())
                )
        except Exception as e:
            os.remove(file_path)
            if ph_path:
                os.remove(ph_path)
            # Mark the file as ignored
            return await upload_msg.edit(f"Error: {e}")

        await download_msg.delete() 
        os.remove(file_path)
        if ph_path:
            os.remove(ph_path)

# Remove the entry from renaming_operations after successful renaming
        del renaming_operations[file_id]
        
