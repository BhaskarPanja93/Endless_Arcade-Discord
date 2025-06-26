import discord
from discord.ext import commands


class GuildEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.Cog.listener()
    async def on_guild_update(self, before: discord.Guild, after: discord.Guild):
        """
        Executed when the bot reads a new message.
        :param before: The Channel object that was deleted
        :param after: The Channel object that was deleted
        """
        print("Guild changed", before.name, after.name)


    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
        """
        Executed when the bot reads a new message.
        :param channel: The Channel object that was deleted
        """
        print("Channel deleted", channel.name, channel.category.name)


    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
        """
        Executed when the bot reads a new message.
        :param channel: The Channel object that was created
        """
        print("Channel created", channel.name, channel.category.name)


    @commands.Cog.listener()
    async def on_guild_channel_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        """
        Executed when the bot reads a new message.
        :param before: The Channel object that was changed from
        :param after: The Channel object that was changed to
        """
        print("Channel updated", before.name, after.name, before.category.name, after.category.name)

