from telethon import TelegramClient, events
from userbot import bot
import asyncio


@bot.on(events.NewMessage(pattern='(?i).type'))
async def typewriter(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        textx = await e.get_reply_message()
        message = e.text

        if message[6:]:
            message = str(message[6:])
        elif textx:
            message = textx
            message = str(message.message)
        sleep_time = 0.1
        index = 1
        old_text = ''
        msg = await e.edit('|')
        await asyncio.sleep(sleep_time)
        while old_text != message:
            old_text = message[:index]
            index += 1
            await msg.edit('`%s`' % (old_text + '|'))
            await asyncio.sleep(sleep_time)
            await msg.edit('`%s`' % (old_text.strip()))
            await asyncio.sleep(sleep_time)
