from core.classes import Cog_Extension
from discord.ext import commands
import discord
import core.functions as func


class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(content=f'`{error}`', delete_after=5.0)

    @commands.Cog.listener()
    async def on_command(self, ctx):
        cmd_name = ctx.command.name
        cmd_parents = ctx.command.full_parent_name
        channel_name = ctx.channel.name
        user_name = ctx.author.name
        user_id = ctx.author.id
        message = ctx.message.content

        if len(cmd_parents) == 0:
            cmd_parents = str('N/A')

        log_msg = f'[{cmd_parents}][{cmd_name}], [{channel_name}], [{user_name}][{user_id}]\n[{message}]\n'
        report_channel = discord.utils.get(self.bot.guilds[0].text_channels, name='working-report')
        await report_channel.send(f'[cmd exec]{log_msg}[{func.now_time_info("whole")}]')


def setup(bot):
    bot.add_cog(Event(bot))
