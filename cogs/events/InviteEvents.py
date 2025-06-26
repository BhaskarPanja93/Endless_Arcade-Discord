import discord
from discord.ext import commands

from shared.SingletonValues import SingletonValues

singleton_values = SingletonValues()
class InviteEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_invite_create(self, invite: discord.abc.Invite):
        """
        Executed when the bot reads a new message.
        """
        print("Invite created by", invite.inviter.name)


    @commands.Cog.listener()
    async def on_invite_delete(self, invite: discord.abc.Invite):
        """
        Executed when the bot reads a new message.
        """
        print("Invite deleted by", invite.inviter.name)
