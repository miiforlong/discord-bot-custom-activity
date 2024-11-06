import discord
from discord.ext import commands

activity_input = input("Entrez l'activité du bot : ")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")

    if activity_input:

        activity = discord.Game(name=activity_input)
        await bot.change_presence(status=discord.Status.online, activity=activity)

    print(f"L'activité du bot est maintenant : {activity_input}")

bot.run('YOUR_TOKEN_HERE')  
