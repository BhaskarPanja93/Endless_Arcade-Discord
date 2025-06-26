import discord
from discord.ext import commands

from shared.SingletonValues import SingletonValues

singleton_values = SingletonValues()
class MemberEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        Executed when the bot reads a new message.
        """
        print("Member Joined", member.name)


    @commands.Cog.listener()
    async def on_raw_member_remove(self, event: discord.RawMemberRemoveEvent):
        """
        Executed when the bot reads a new message.
        """
        print("Member left", event.user.name)


    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user:discord.abc.User|discord.Member):
        """
        Executed when the bot reads a new message.
        """
        print("Member banned", user.name)


    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild, user:discord.abc.User|discord.Member):
        """
        Executed when the bot reads a new message.
        """
        print("Member unbanned", user.name)
