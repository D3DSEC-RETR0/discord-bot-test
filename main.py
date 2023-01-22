import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready.")
    while not client.is_closed():
        await asyncio.sleep(600) # sleep for 10 minutes
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        channel = client.get_channel(channel_id) # replace with the channel id you want the message to be sent to
        await channel.send("The current time is " + current_time)

client.run("your_bot_token")
