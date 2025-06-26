import discord
from discord.ext import commands

from shared.SingletonValues import SingletonValues

singleton_values = SingletonValues()
class BotEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_shard_connect(self, shard_id):
        """
        Executed when the bot reads a new message.
        """
        print("Bot Connected to Shard", shard_id)


    @commands.Cog.listener()
    async def on_shard_disconnect(self, shard_id):
        """
        Executed when the bot reads a new message.
        """
        print("Bot Disconnected from Shard", shard_id)

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Executed when the bot has logged in and ready to work.
        """
        print("Ready in as", self.bot.user)


    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """
        Executed when the bot joins a new guild.
        :param guild: The Guild object of the guild that the bot joined
        """
        if guild.id == singleton_values.Values.GUILD_ID:
            print("JOINED KNOWN GUILD", guild.name)
        else:
            print("LEFT NEW UNKNOWN GUILD", guild.name)
            await guild.leave()


    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """
        Executed when the bot joins a new guild.
        :param guild: The Guild object of the guild that the bot joined
        """
        if guild.id == singleton_values.Values.GUILD_ID:
            print("REMOVED FROM KNOWN GUILD", guild.name)

