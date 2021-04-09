from datetime import datetime, timezone, timedelta
import math
import discord
import asyncio


def now_time_info(mode):
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt2 = dt1.astimezone(timezone(timedelta(hours=8)))  # 轉換時區 -> 東八區

    if mode == 'whole':
        return str(dt2.strftime("%Y-%m-%d %H:%M:%S"))
    if mode == 'hour':
        return int(dt2.strftime("%H"))
    if mode == 'date':
        return int(dt2.isoweekday())
    if mode == 'week':
        return str(dt2.strftime("%A"))


def getChannel(bot, target):
    if target == '_Report':
        return discord.utils.get(bot.guilds[0].text_channels, name='working-report')

    if target == 'sqcs_report':
        return discord.utils.get(bot.guilds[0].text_channels, name='sqcs-report')


async def buffer_pack(buffer):
    logs = str()
    found = bool(False)
    while not found:
        msg_logs = await buffer.history(limit=50).flatten()
        for item in msg_logs:
            if item.content != '#CHECKPOINT#':
                logs += item.content + '\n'
                await item.delete()
            else:
                found = True
                break

    if len(logs) == 0:
        return

    with open('./txts/report_buffer.txt', mode='w', encoding='utf8') as temp_file:
        temp_file.write(logs)

    # clear the string
    logs = ''

    await buffer.send(file=discord.File('./txts/report_buffer.txt'))
    await buffer.send('#CHECKPOINT#')

    # clear buffer content
    with open('./txts/report_buffer.txt', mode='w', encoding='utf8') as temp_file:
        temp_file.write('')
