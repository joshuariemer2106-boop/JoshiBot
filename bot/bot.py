import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Bot online als {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.send("Bot funktioniert!")

bot.run(DISCORD_TOKEN)
