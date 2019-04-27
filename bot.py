#! usr/bin/env python3

import discord, dbl, asyncio, datetime
from get_news import get_news

def main():
	TOKEN = "NTcxNDI3OTI4MzMyODI4NzEy.XMNmKA.wXKFt4z4zoRKTP8nLIA87wSkYnY"
	client = discord.Client()
	
	async def print_news(channel):
		news = get_news()
		if news:
			tmp, link = news[0].replace("\n\n\n", "\n").replace("\n\n", "\n"), news[1]
			cntr = 0
			out = ""
			for a in tmp.split("\n"):
				if cntr + len(a) > 2000:
					await channel.send(out)
					out = a + "\n"
					cntr = len(a) + 1
				else:
					out +=  a + "\n"
					cntr += len(a) + 1
			if out:
				await channel.send(out)
			await channel.send(link)
		else:
			await(channel.send("no new news"))

	async def update_news():
		await client.wait_until_ready()
		if datetime.datetime.now().hour == 23:
			for channel in member.server.channels:
				if str(channel) == "bns-news-update":
					await print_news(message.channel)

		else:
			await asyncio.sleep(3600)

	@client.event
	async def on_ready():
		print("The bot is ready!")
	
	@client.event
	async def on_message(message):
		if message.author == client.user:
			return
		if message.content == "Hello" and str(message.author) == "TheFirstFlame#0017":
			await message.channel.send("*World*")
		if message.content == "!fp" and str(message.author) == "TheFirstFlame#0017":
			await print_news(message.channel)

	client.loop.create_task(update_news())
	client.run(TOKEN)

if __name__ == "__main__":
	main()
