import discord
import os
import time


client = discord.Client()


@client.event
async def on_ready():
  print("I Am Online")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Ok Leave Now, Thanks"))
  await client.get_channel(855175532140167188).send("Hello! I has becomes onlines")


@client.event

async def on_message(message):
  await client.get_channel(855175532140167188).send(message.content)
  


client.run(ODU1MTgzNTc4NzU2MTUzMzU1.YMuxxQ.75jRc72uJdPopTnAhgX7hyy15o0)
