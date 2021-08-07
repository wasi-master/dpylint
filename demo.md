# Demo

Let's say we have the following file with the name [demo.py](https://github.com/wasi-master/dpylint/blob/main/demo.py)

```py
"""A file to show a demo of dpylint"""
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

```

Then running `pylint demo.py` will show these problems with our code:

```prolog
demo.py:5:1: W9002: Permission Value should not be "a", it should be either True or False (invalid-permission-value)
demo.py:11:1: E9001: Invalid Permission Name: "manage_server", did you mean manage_guild (invalid-permission-name)
demo.py:17:1: W9003: No Permissions Specified (no-permissions-specified)
demo.py:23:0: E9005: Invalid Parameters Passed to on_ready: (ctx) valid parameters are () (invalid-event-params)
demo.py:28:0: E9005: Invalid Parameters Passed to on_message: (message, user) valid parameters are (message) (invalid-event-params)
demo.py:32:1: E9004: Invalid Event Name "on_tpying", did you mean on_typing (invalid-event-name)
demo.py:38:0: E9004: Invalid Event Name "on_guld_jon", did you mean on_guild_join (invalid-event-name)
```
