import discord
from discord.ext import commands
import os, random, requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def memepemograman(ctx):
    img_name = random.choice(os.listdir('Meme pemograman'))
    with open(f'Meme pemograman/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def memerelate(ctx):
    img_name = random.choice(os.listdir('Meme relate'))
    with open(f'Meme relate/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("Token")
