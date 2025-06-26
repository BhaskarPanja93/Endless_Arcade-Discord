import discord
from discord.ext import commands
from discord.ext.commands.cog import app_commands

from shared.SingletonValues import SingletonValues

singleton_values = SingletonValues()

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @app_commands.command(name="trial1", description="trial")
    async def trial1(self, interaction:discord.Interaction):
        parsed_interaction = discord.interactions.InteractionResponse(interaction)
        await parsed_interaction.send_message("Found message 1")

    @app_commands.command(name="trial2", description="trial2")
    async def trial2(self, interaction:discord.Interaction):
        parsed_interaction = discord.interactions.InteractionResponse(interaction)
        await parsed_interaction.send_message("Found message 2")
