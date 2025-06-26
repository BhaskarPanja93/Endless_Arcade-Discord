import discord
from discord.ext import commands


class GuildRoleEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.Cog.listener()
    async def on_guild_role_create(self, role: discord.abc.Role):
        """
        Executed when the bot reads a new message.
        :param role: The Channel object that was deleted
        """
        print("Role created", role.name)


    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: discord.abc.Role):
        """
        Executed when the bot reads a new message.
        :param role: The Channel object that was deleted
        """
        print("Role deleted", role.name)


    @commands.Cog.listener()
    async def on_guild_role_update(self, before: discord.abc.Role, after: discord.abc.Role):
        """
        Executed when the bot reads a new message.
        :param before: The Channel object that was created
        :param after: The Channel object that was created
        """
        print("Role updated", before.name, after.name)
