import discord
import random
from discord.ext import commands 

client = commands.Bot(command_prefix="~")

@client.event
async def on_ready():
	print("Bot is ready")

@client.command()
async def ping(ctx):
	await ctx.send(f"Pong! {round(client.latency * 1000)}")

@client.command()
async def yo(ctx):
	await ctx.send("Wagwarn")

@client.command()
async def Wagwarn(ctx):
	await ctx.send("Wys Pussio")

@client.command()
async def Sym(ctx):
	await ctx.send("Suck your dead dad")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes",
                 "Ask again later",
                 "Better not tell you now",
                 "Cannot predict now",
                 "Concentrate and ask again",
                 "Don’t count on it",
                 "It is certain",
                 "It is decidedly so",
                 "Most likely",
                 "My reply is no",
                 "My sources say no",
                 "Outlook not so good",
                 "Outlook good",
                 "Reply hazy, try again",
                 "Signs point to yes",
                 "Very doubtful",
                 "Without a doubt",
                 "Yes",
                 "Yes – definitely",
                 "You may rely on it"]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


client.run("ODMxODkyNjAwMTA5NzkzMzAx.YHb2Ww.LhOFk1xR02bdK9v_T8IHzEs9zbA")
