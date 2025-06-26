import asyncio

import discord
from discord.ext import commands
from discord.ext.commands import AutoShardedBot

from cogs.commands.Greetings import Greetings
from cogs.events.BotEvents import BotEvents
from cogs.events.GuildEvents import GuildEvents
from cogs.events.GuildRoleEvents import GuildRoleEvents
from cogs.events.InviteEvents import InviteEvents
from cogs.events.MemberEvents import MemberEvents
from cogs.events.MessageEvents import MessageEvents
from cogs.events.ThreadEvents import ThreadEvents
from processors import Predicates
from shared import Secrets
from shared.SingletonValues import SingletonValues

singleton_values = SingletonValues()

bot = AutoShardedBot(
    command_prefix=singleton_values.Values.BOT_PREFIX,
    case_insensitive=True,
    intents=discord.Intents().all(),
    strip_after_prefix=True,
    shard_connect_timeout=10,
    shard_count=1
)

@bot.event
async def on_ready():
    """
    Executed when the bot has logged in and ready to work.
    """
    print("Logged in as", bot.user)
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="your messages"))
    await bot.add_cog(BotEvents(bot))
    await bot.add_cog(GuildEvents(bot))
    await bot.add_cog(GuildRoleEvents(bot))
    await bot.add_cog(InviteEvents(bot))
    await bot.add_cog(MemberEvents(bot))
    await bot.add_cog(MessageEvents(bot))
    await bot.add_cog(ThreadEvents(bot))
    await bot.add_cog(Greetings(bot))

    for guild in bot.guilds:
        if guild.id == singleton_values.Values.GUILD_ID:
            bot.loop.create_task(bot.tree.sync(guild=guild))
            print("SYNCING COMMAND TREE")

#
# @bot.tree.command(name='sync', description='Owner only')
# async def sync(interaction: discord.interactions.Interaction):
#     response = discord.interactions.InteractionResponse(interaction)
#     if interaction.user.id in singleton_values.Values.OWNERS:
#         bot.loop.create_task(bot.tree.sync(guild=interaction.guild))
#         print('Command tree synced.')
#         await response.send_message("Sync started")
#     else:
#         await response.send_message("Only owner can use this command", ephemeral=True)
#


async def main():
    async with bot:
        await bot.start(Secrets.BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
