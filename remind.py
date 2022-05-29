from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!")


@bot.command()
async def remind(ctx, time, *, task,):
    await ctx.message.delete()
    def convert(time):
        pos = ['s', 'm', 'h', 'd']

        time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    converted_time = convert(time)

    if converted_time == -1:
        await ctx.send("Nie ustawiłeś odpowiednio czasu")
        return

    if converted_time == -2:
        await ctx.send("Czas musi być liczbą")
        return

    await ctx.send(f"Ustawiono przypomnienie: **{task}** i potrwa: **{time}**")

    await asyncio.sleep(converted_time)
    await ctx.send(f"Przypomnienie: **{task}** zostało wykonane po określonym czasie: **{time}**")


def setup(cmd):
    cmd.add_command(remind)
