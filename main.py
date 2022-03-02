import discord
import os
import random
import string
from keep_alive import keep_alive

client = discord.Client()

def id_generator(size=4, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="IO Games | $help"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        await message.channel.send(
          '*$hello* - say hello\n' +
          '*$catan* - sends a catan link\n' + 
          '*$codenames* - sends a codenames link\n' +
          '*$monopolydeal* - sends a monopoly deal link\n' +
          '*$cardsagainsthumanity* - sends a cards against humanity link\n' +
          '*$secrethitler* - sends a secret hitler link\n'

        )

    if message.content.startswith('$hello'):
        await message.channel.send('chello!')

    if message.content.startswith('$catan'):
        await message.channel.send('https://colonist.io/#' + id_generator())

    if message.content.startswith('$codenames'):
        await message.channel.send('https://www.horsepaste.com/' + id_generator())

    if message.content.startswith('$monopolydeal'):
        await message.channel.send('https://www.covidopoly.io')

    if message.content.startswith('$cardsagainsthumanity'):
        await message.channel.send('https://cardsagainstformality.io/')

    if message.content.startswith('$secrethitler'):
    	await message.channel.send('https://secrethitler.io/')




keep_alive()
client.run(os.getenv('bot_token'))