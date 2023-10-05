# import discord
# import requests
# from discord.ext import commands

# # Create a bot instance
# bot = commands.Bot(command_prefix='!')

# # Define your RapidAPI key
# RAPIDAPI_KEY = '1684fdba38msh8be1da2cb7af859p12944fjsnfca3c40a5bab'

# @bot.event
# async def on_ready():
#     print(f'Logged in as Muscle')

# @bot.command(name='lol', help='Get League of Legends standings')
# async def lol_standings(ctx):
#     url = "https://league-of-legends-esports.p.rapidapi.com/standings/103556720421148036"

#     headers = {
#         "X-RapidAPI-Key": '1684fdba38msh8be1da2cb7af859p12944fjsnfca3c40a5bab',
#         "X-RapidAPI-Host": "league-of-legends-esports.p.rapidapi.com"
#     }

#     try:
#         response = requests.get(url, headers=headers)
#         data = response.json()

#         if 'data' in data:
#             standings = data['data'][0]['standings']

#             # Send the standings as a Discord message
#             await ctx.send("League of Legends Standings:")
#             for team in standings:
#                 team_name = team['team']['name']
#                 wins = team['wins']
#                 losses = team['losses']
#                 await ctx.send(f"Team: {team_name}, Wins: {wins}, Losses: {losses}")

#         else:
#             await ctx.send("No standings data found.")

#     except Exception as e:
#         print(e)
#         await ctx.send('An error occurred while fetching League of Legends standings.')

# # Replace 'YOUR_TOKEN' with your bot token
# bot.run('MTE1OTM0ODg4ODgwMTY0MDUzOQ.GA5rSE.LjRzL7yIrUANd0Gow4CTRFfaGQLGWje2zmivZM')


import discord
import requests
from discord.ext import commands

# Define your RapidAPI key
RAPIDAPI_KEY = '1684fdba38msh8be1da2cb7af859p12944fjsnfca3c40a5bab'

# Define the list of intents required by your bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Add the 'messages' intent
intents.messages = True

# Create a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='hello', help='Respond with a friendly greeting')
async def hello(ctx):
    await ctx.send('Hello! How can I assist you today?')

@bot.command(name='lol', help='Get League of Legends standings')
async def lol_standings(ctx):
    url = "https://league-of-legends-esports.p.rapidapi.com/standings/103556720421148036"

    headers = {
        "X-RapidAPI-Key": '1684fdba38msh8be1da2cb7af859p12944fjsnfca3c40a5bab',
        "X-RapidAPI-Host": "league-of-legends-esports.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'data' in data:
            standings = data['data'][0]['standings']

            # Send the standings as a Discord message
            await ctx.send("League of Legends Standings:")
            for team in standings:
                team_name = team['team']['name']
                wins = team['wins']
                losses = team['losses']
                await ctx.send(f"Team: {team_name}, Wins: {wins}, Losses: {losses}")

        else:
            await ctx.send("No standings data found.")

    except Exception as e:
        print(e)
        await ctx.send('An error occurred while fetching League of Legends standings.')

# Replace 'YOUR_TOKEN' with your bot token
bot.run('MTE1OTM0ODg4ODgwMTY0MDUzOQ.GA5rSE.LjRzL7yIrUANd0Gow4CTRFfaGQLGWje2zmivZM')
