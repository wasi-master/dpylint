# dpylint

dpylint is a pylint extension for linting python code using the discord.py library

## Installation

You'll need to have [python](https://www.python.org) and [pylint](https://www.pylint.org) installed in order to use the extension

Currently there are two ways to install dpylint

* Installing via pip
  1. Directly installing via pip (Recommended)

     ```sh
     pip install dpylint
     ```

  2. Installing using pip and git

     ```sh
     pip install git+https://github.com/wasi-master/dpylint.git
     ```

* Cloning then installing
  1. Clone the repo

     ```sh
     git clone https://github.com/wasi-master/dpylint.git
     ```

  2. Install using pip

     ```sh
     pip install .
     ```

## Configuration

### **.pylintrc file**

You can create a new file called `.pylintrc` and add this to that file in order to make sure the extension is loaded

```ini
[MASTER]

load-plugins=dpylint
```

### **command line argument**

Alternatively if you usually run pylint from the command line, you can pass `--load-plugins=dpylint` to pylint to load the plugin when using it from the command line

```sh
pylint file.py --load-plugins=dpylint
```

### **vscode**

In order to use the extension with vscode, make sure you have the python extension installed, then you can do either

* Press `Ctrl+Shift+P` and type `Open Settings (JSON)`. then in a new line write

  ```js
  "python.linting.pylintArgs": [
        "--load-plugins=dpylint",
  ],
  "python.linting.pylintEnabled": true,
  "python.linting.enabled": true
  ```

* Press `Ctrl+Shift+P` and type `Preferences: Open Settings (UI)`. then
  1. Search for `python.linting.enabled` then click the check mark
    ![image](https://i.imgur.com/mVaOZz4.png)
  2. Search for `python.linting.pylintEnabled` then click the check mark
    ![image](https://i.imgur.com/cUJqdoQ.png)
  3. Search for `python.linting.pylintArgs` then click Add item
    ![image](https://i.imgur.com/Wj3ab9v.png)
  4. Add `--load-plugins=dpylint` then click `OK`
    ![image](https://i.imgur.com/xHzwwft.png)

## Checkers

| Name                             | ID             | Details        |
| -------------------------------- | -------------- | -------------- |
| invalid-permission-name          | E9001          | An invalid permission was passed to has_permissions (for a list of valid permissions see [the docs](https://discordpy.readthedocs.io/en/latest/api.html#discord.Permissions)|
| invalid-permission-value         | W9002          | The value passed to has_permissions should be either True or False|
| no-permissions-specified         | W9003          | There should be at least one valid permission passed to has_permissions
| invalid-event-name               | E9004          | An invalid event was used (for a list of valid events see [the docs](https://discordpy.readthedocs.io/en/latest/api.html#event-reference))
| invalid-event-params             | E9005          | The event signature has invalid parameters

More checkers will be added in the future

## Demo

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

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

* For a list of things that need to be done, see the [todo list](https://github.com/wasi-master/dpylint/blob/main/TODO_LIST.md)
