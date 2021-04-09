import discord
from core.classes import Cog_Extension
from discord.ext import commands
from core.setup import client, rsp
import core.functions as func
import asyncio


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':stopwatch: {round(self.bot.latency * 1000)} (ms)')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        token_role = await member.guild.get_role(791680285464199198)
        await member.add_roles(token_role)

    @commands.command()
    async def get_role(self, ctx, role: str):
        await ctx.message.delete()

        try:
            token_role = ctx.guild.get_role(791680285464199198)
            target_role = discord.utils.get(ctx.guild.roles, name=role)
            await ctx.author.add_roles(target_role)
            await ctx.author.remove_roles(token_role)
        except:
            msg = rsp["role_token"]["role_name_error"]["pt_1_1"] + '\n'
            msg += f'才沒有甚麼叫做 `{role}` 的職位啦！\n'
            msg += rsp["role_token"]["role_name_error"]["pt_1_2"]
            await ctx.message.author.send(msg)

            await ctx.message.author.send('https://imgur.com/LKEMcHb')

            msg = '\n'.join(rsp["role_token"]["role_name_error"]["pt_2"])
            await ctx.message.author.send(msg)

    @commands.command()
    async def manual_pack(self, ctx, channel: str):
        if channel not in ['working-report', 'sqcs-report', 'sqcs-lecture-attend']:
            await ctx.send(f':exclamation: The channel {channel} can\'t be reached!')
            return

        await asyncio.sleep(2)
        await func.buffer_pack(discord.utils.get(self.bot.guilds[0].text_channels, name=channel))
        await ctx.send(':white_check_mark: Log packing finished!')


def setup(bot):
    bot.add_cog(Main(bot))
