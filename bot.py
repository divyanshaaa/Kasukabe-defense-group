import discord
import pandas as pd
#cpu info
import psutil 

#instance of bot
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('system information'):
            if message.content == 'system information':
                # Get CPU usage and memory usage
                cpu_usage = psutil.cpu_percent()
                memory_usage = psutil.virtual_memory()

                # Get temperature information
                try:
                    sensors_data = pd.Series.from_cmd("sensors")
                    temperature_info = sensors_data.to_string(index=False)
                except Exception as e:
                    temperature_info = "Unable to retrieve temperature data."

                # Get disk space information
                disk_usage = psutil.disk_usage('/')
                
                response = f"Hello! Here is your system information:\n"
                response += f"CPU Usage: {cpu_usage}%\n"
                response += f"Memory Usage: {memory_usage.percent}%\n"
                response += f"Temperature Information:\n{temperature_info}\n"
                response += f"Disk Space Usage:\n"
                response += f"Total: {disk_usage.total} bytes\n"
                response += f"Used: {disk_usage.used} bytes\n"
                response += f"Free: {disk_usage.free} bytes\n"


                await message.channel.send(response)
            else:
                await message.channel.send('Hello!')


client.run('MTE1OTM0ODg4ODgwMTY0MDUzOQ.GA5rSE.LjRzL7yIrUANd0Gow4CTRFfaGQLGWje2zmivZM')



