import discord
from discord.ext import commands

from shared.SingletonValues import SingletonValues

singleton_values = SingletonValues()
class ThreadEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_thread_create(self, thread: discord.Thread):
        """
        Executed when the bot reads a new message.
        """
        print("Thread created", thread.name, thread.category.name)


    @commands.Cog.listener()
    async def on_raw_thread_update(self, event: discord.RawThreadDeleteEvent):
        """
        Executed when the bot reads a new message.
        """
        print("Thread created", event.thread.name, event.thread.category.name)

    @commands.Cog.listener()
    async def on_raw_thread_delete(self, event: discord.RawThreadDeleteEvent):
        """
        Executed when the bot has logged in and ready to work.
        """
        if event.thread:
            print("Thread removed", event.thread.name, event.thread.category.name)
        else:
            print("Thread removed parent:", event.parent_id)


