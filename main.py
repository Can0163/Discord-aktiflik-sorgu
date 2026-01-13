import discord
from discord import app_commands
import requests
import os

TOKEN = os.getenv("TOKEN")
UNIVERSE_ID = int(os.getenv("UNIVERSE_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Bot giriş yaptı: {client.user}")

@tree.command(name="aktiflik", description="Roblox oyununun anlık aktifliğini gösterir")
async def aktiflik(interaction: discord.Interaction):
    url = f"https://games.roblox.com/v1/games?universeIds={UNIVERSE_ID}"
    data = requests.get(url).json()
    game = data["data"][0]

    await interaction.response.send_message(
        f"🎮 **{game['name']}**\n"
        f"👥 Anlık Oyuncu: **{game['playing']:,}**"
    )

client.run(TOKEN)
