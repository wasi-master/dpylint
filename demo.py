"""A file to show a demo of dpylint. for actual testing see the test directory"""
from discord.ext import commands

@commands.command()
@commands.has_permissions(manage_messages="a")
async def test(ctx):
    """Tests the permission value passed to has_permissions"""
    await ctx.send("hi")

@commands.command()
@commands.has_permissions(manage_server=True)
async def test(ctx):
    """Tests the permission name passed to has_permissions"""
    await ctx.send("hi")

@commands.command()
@commands.has_permissions()
async def test(ctx):
    """Tests if any permissions were passed to has_permissions"""
    await ctx.send("hi")

@commands.Cog.listener("on_ready")
async def test(ctx):
    """Tests if the parameters taken in the function match the parameters that the event has"""
    return ctx

@commands.Cog.listener()
async def on_message(message, user):
    """Tests if the parameters taken in the function match the parameters that the event has"""
    return message, user

@commands.Cog.listener("on_tpying")
async def test(ctx):
    """Tests if the event name is right"""
    return ctx

@commands.Cog.listener()
async def on_guld_jon(ctx):
    """Tests if the event name is right"""
    return ctx
