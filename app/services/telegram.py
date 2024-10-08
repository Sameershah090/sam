from telegram import Bot
import aiohttp
from app.config import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

async def get_file_stream(chat_id: int, message_id: int):
    message = await bot.get_message(chat_id=chat_id, message_id=message_id)
    if not message.document and not message.video and not message.audio and not message.voice:
        raise ValueError("No file found in this message")

    file = await bot.get_file(message.document.file_id if message.document else 
                              message.video.file_id if message.video else 
                              message.audio.file_id if message.audio else 
                              message.voice.file_id)
    file_url = file.file_path

    async def file_stream():
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.telegram.org/file/bot{settings.TELEGRAM_BOT_TOKEN}/{file_url}") as resp:
                while True:
                    chunk = await resp.content.read(8192)
                    if not chunk:
                        break
                    yield chunk

    file_name = message.document.file_name if message.document else "file"
    mime_type = message.document.mime_type if message.document else None

    return file_stream(), file_name, mime_type

async def get_file_info(chat_id: int, message_id: int):
    message = await bot.get_message(chat_id=chat_id, message_id=message_id)
    if not message.document and not message.video and not message.audio and not message.voice:
        raise ValueError("No file found in this message")

    file_type = "document" if message.document else "video" if message.video else "audio" if message.audio else "voice"
    file_name = message.document.file_name if message.document else "video" if message.video else "audio" if message.audio else "voice"

    return {"file_type": file_type, "file_name": file_name}
