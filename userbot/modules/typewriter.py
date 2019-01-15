from telethon import TelegramClient, events
from userbot import bot
import asyncio


@bot.on(events.NewMessage(pattern='(?i)!type (.+)'))
async def typewriter(event):
    sleep_time = 0.3
    text = event.pattern_match.group(1)
    index = 1
    old_text = ''

    msg = await event.reply('|')
    await asyncio.sleep(sleep_time)

    while old_text != text:
        old_text = text[:index]
        index += 1

        await msg.edit('`%s`' % (old_text + '|'))
        await asyncio.sleep(sleep_time);
        await msg.edit('`%s`' % (old_text.strip()))
        await asyncio.sleep(sleep_time)

client.run_until_disconnected() 
