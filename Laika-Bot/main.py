import os
import sys
import discord
import re
from datetime import time

# discord access info -----------------------------------------------------------------
client = discord.Client()
bot_id = 'removed'
channel_id = 000000
channel_name = "channel name"
# -------------------------------------------------------------------------------------


@client.event # run the code when the bot goes online
async def on_ready():
    bot_testing = client.get_channel(channel_id) # accessing the channel
    await bot_testing.send("Laika Bot is now online!")

@client.event
async def on_message(message):
    new_message = True
    gate = False

    if str(message.channel) == channel_name: gate = True

    slime_bot = client.get_channel(channel_id)
    original_input = message.content
    serverID = message.guild.id
    userID = message.author.id
    userName = message.author.name

    if original_input == "//bye-laika":
        await message.channel.send("Bye!")
        sys.exit(0)

    while gate == True:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fileName = 'log.txt'

        messageCount = 1
        with open(os.path.join(dir_path, fileName), "a+", encoding="utf-8") as file_ptr:
            file_ptr.seek(0)
            filedata = file_ptr.readlines()
            # print(filedata)
            for line in filedata:
                num = re.search(r'Message Count: \d+', line)
                if num != None:
                    num = num.group(0)
                    num = num.strip().replace("Message Count: ", "")
                    if len(num) > 0:
                        messageCount = int(num) + 1
            
            file_ptr.write(f"User ID: {userID}\n")
            file_ptr.write(f"Username: {userName}\n")
            file_ptr.write(f"Message Count: {messageCount}\n\n")

        gate = False

@client.event
async def on_message_delete(message):
    new_message = True
    gate = False
    
    if str(message.channel) == channel_name: gate = True

    slime_bot = client.get_channel(channel_id)
    original_input = message.content
    serverID = message.guild.id
    userID = message.author.id
    userName = message.author.name

    while gate == True:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fileName = 'delete-log.txt'

        messageCount = 1
        with open(os.path.join(dir_path, fileName), "a+", encoding="utf-8") as file_ptr:
            file_ptr.seek(0)
            filedata = file_ptr.readlines()
            for line in filedata:
                num = re.search(r'Deleted Message Count: \d+', line)
                if num != None:
                    num = num.group(0)
                    num = num.strip().replace("Deleted Message Count: ", "")
                    if len(num) > 0:
                        messageCount = int(num) + 1
            
            file_ptr.write(f"User ID: {userID}\n")
            file_ptr.write(f"Username: {userName}\n")
            file_ptr.write(f"Deleted Message Count: {messageCount}\n\n")

        gate = False

while True:
    client.run(bot_id)