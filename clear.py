from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.command()
async def clear(ctx, amount):
    await ctx.message.delete()
    await ctx.channel.purge(limit=int(amount))


@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Podano niepoprawny argument")


def setup(cmd):
    cmd.add_command(clear)
