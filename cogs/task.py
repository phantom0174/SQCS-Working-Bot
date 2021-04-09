import discord
from discord.ext import commands, tasks
from core.classes import Cog_Extension, JsonApi
import core.functions as func


class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.quiz_auto.start()

    @tasks.loop(minutes=30)
    async def quiz_auto(self):
        await self.bot.wait_until_ready()

        status = JsonApi().get_json('dyn')

        if func.now_time_info('hour') != 23 or status['buffer_flush'] == 1:
            if func.now_time_info('hour') == 1:

                status = JsonApi().get_json('dyn')
                status['buffer_flush'] = 0
                JsonApi().put_json('dyn', status)

            return

        await func.buffer_pack(func.getChannel(self.bot, 'sqcs_report'))
        await func.buffer_pack(func.getChannel(self.bot, 'working_report'))

        status['buffer_flush'] = 1

        JsonApi().put_json('dyn', status)


def setup(bot):
    bot.add_cog(Task(bot))
