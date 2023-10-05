# import discord
# import asyncio
# from datetime import datetime

# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)

# scheduled_events = {}

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('schedule'):
#         try:
#             _, event_time_str, *event_description = message.content.split()
#             event_description = ' '.join(event_description)
#             event_time = datetime.strptime(event_time_str, '%Y-%m-%d %H:%M')
#         except ValueError:
#             await message.channel.send('Invalid format. Please use "schedule YYYY-MM-DD HH:MM Event description".')
#             return

#         scheduled_events[event_time] = event_description
#         await message.channel.send(f'Scheduled event: "{event_description}" at {event_time}.')
#         print(f'Scheduled event: "{event_description}" at {event_time}.')  # Add this line to check if the code reaches here.

# async def check_scheduled_events():
#     while True:
#         current_time = datetime.now()
#         for event_time, event_description in list(scheduled_events.items()):
#             if current_time >= event_time:
#                 channel = client.get_channel(1159348888801640539)
#                 await channel.send(f'Reminder: "{event_description}" was scheduled at {event_time}.')
#                 del scheduled_events[event_time]
#                 print(f'Reminder sent for: "{event_description}" at {event_time}.')  # Add this line for debugging.
#         await asyncio.sleep(60)

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')
#     client.loop.create_task(check_scheduled_events())

# client.run('MTE1OTM0ODg4ODgwMTY0MDUzOQ.GZ2Ydq.ok0AbQKiFu0ZL-9Po3fuBQJfnN-vOvAeNx-vTw')

# import discord
# import asyncio
# from datetime import datetime

# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)

# scheduled_events = {}

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')
#     client.loop.create_task(check_scheduled_events())

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('schedule'):
#         try:
#             _, event_time_str, *event_description = message.content.split()
#             event_description = ' '.join(event_description)
#             event_time = datetime.strptime(event_time_str, '%Y-%m-%d %H:%M')
#         except ValueError:
#             await message.channel.send('Invalid format. Please use "schedule YYYY-MM-DD HH:MM Event description".')
#             return

#         scheduled_events[event_time] = event_description
#         await message.channel.send(f'Scheduled event: "{event_description}" at {event_time}.')
#         print(f'Scheduled event: "{event_description}" at {event_time}.')

# async def check_scheduled_events():
#     while True:
#         current_time = datetime.now()
#         print(f'Checking scheduled events at {current_time}.')  # Add this line for debugging.
#         for event_time, event_description in list(scheduled_events.items()):
#             if current_time >= event_time:
#                 channel = client.get_channel(1159348888801640539)
#                 await channel.send(f'Reminder: "{event_description}" was scheduled at {event_time}.')
#                 del scheduled_events[event_time]
#                 print(f'Reminder sent for: "{event_description}" at {event_time}.')  # Add this line for debugging.
#         await asyncio.sleep(60)

# client.run('MTE1OTM0ODg4ODgwMTY0MDUzOQ.GA5rSE.LjRzL7yIrUANd0Gow4CTRFfaGQLGWje2zmivZM')


import discord
import asyncio
import datetime
import aiohttp

intents = discord.Intents.all()  # Initialize intents correctly

class EventSchedulingBot(discord.Client):
    def __init__(self, intents=intents):  # Use the initialized intents
        super().__init__(intents=intents)

        self.events = {}

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.content.startswith('!createevent'):
            await self.create_event(message)
        elif message.content.startswith('!listevents'):
            await self.list_events(message)
        elif message.content.startswith('!delevent'):
            await self.delete_event(message)

    async def create_event(self, message):
        args = message.content.split(' ')

        if len(args) < 5:  # Check for 5 arguments instead of 4
            await message.channel.send('Usage: !createevent <name> <date> <time>')
            return
        name = args[1]
        date_str = args[2]
        time_str = args[3]

        print(f"Received date string: {date_str}")
        print(f"Received time string: {time_str}")

        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            time = datetime.datetime.strptime(time_str, '%H:%M')
        except ValueError:
            await message.channel.send('Invalid date or time format. Use YYYY-MM-DD and HH:MM.')
            return

        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://discord.com/api/v10/guilds/1159348888801640539/events',
                headers={'Authorization': 'Bot MTE1OTM0ODg4ODgwMTY0MDUzOQ.GA5rSE.LjRzL7yIrUANd0Gow4CTRFfaGQLGWje2zmivZM'},
                json={
                    'name': name,
                    'start_timestamp': date.strftime('%Y-%m-%dT%H:%M:%SZ'),
                    'end_timestamp': (date + datetime.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
                }
            ) as response:
                if response.status == 201:
                    self.events[name] = {
                        'date': date,
                        'time': time,
                        'creator': message.author.id 
                    }
                    await message.channel.send('Event created successfully!')
                    print(f'Event "{name}" added.')
                else:
                    await message.channel.send('Failed to create event.')

    async def list_events(self, message):
        if not self.events:
            await message.channel.send('There are no events scheduled.')
            return

        events = ''
        for event_name, event_info in self.events.items():
            events += f'{event_name}: {event_info["date"]} {event_info["time"]}\n'

        await message.channel.send(events)

    async def delete_event(self, message):
        args = message.content.split(' ')

        if len(args) < 2:
            await message.channel.send('Usage: !delevent <name>')
            return

        name = args[1]

        if name not in self.events:
            await message.channel.send('There is no event scheduled with that name.')
            return

        async with aiohttp.ClientSession() as session:
            async with session.delete(
                f'https://discord.com/api/v10/guilds/YOUR_GUILD_ID/events/{name}',
                headers={'Authorization': ' Bot MTE1OTM0ODg4ODgwMTY0MDUzOQ.GA5rSE.LjRzL7yIrUANd0Gow4CTRFfaGQLGWje2zmivZM'}
            ) as response:
                if response.status == 204:
                    del self.events[name]
                    await message.channel.send('Event deleted successfully!')
                    print(f'Event "{name}" deleted.')
                else:
                    await message.channel.send('Failed to delete event.')

if __name__ == '__main__':
    bot = EventSchedulingBot()
    bot.run('MTE1OTM0ODg4ODgwMTY0MDUzOQ.GA5rSE.LjRzL7yIrUANd0Gow4CTRFfaGQLGWje2zmivZM')

