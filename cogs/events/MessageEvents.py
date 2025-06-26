import discord
from discord.ext import commands


class MessageEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """
        Executed when the bot reads a new message.
        :param message: The Message object that was sent
        """
        print("MESSAGE", message.content)


    @commands.Cog.listener()
    async def on_raw_message_edit(self, event:discord.RawMessageUpdateEvent):
        """
        Executed when the bot reads a new message.
        :param event: The Message Update Event
        """

        if not event.cached_message:
            print(f"Message Edited from channel <#{event.channel_id}>")
        else:
            print(f"Message Edited from channel <#{event.channel_id}> with content: {event.cached_message.content}")


    @commands.Cog.listener()
    async def on_raw_message_delete(self, event:discord.RawMessageDeleteEvent):
        """
        Executed when the bot reads a new message.
        :param event: The Message Delete Event
        """
        if not event.cached_message:
            print(f"Message Deleted from channel <#{event.channel_id}>")
        else:
            print(f"Message Deleted from channel <#{event.channel_id}> with content: {event.cached_message.content}")


    @commands.Cog.listener()
    async def on_raw_bulk_message_delete(self, event:discord.RawBulkMessageDeleteEvent):
        """
        Executed when the bot reads a new message.
        :param event: The Message Update Event
        """
        if not event.cached_messages:
            print(f"Message Bulk Deleted from channel <#{event.channel_id}>")
        else:
            print(f"Message Bulk Deleted from channel <#{event.channel_id}> with contents")
            for message in event.cached_messages:
                print(f"{message.content}")
