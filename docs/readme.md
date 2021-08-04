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

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

* For a list of things that need to be done, see the [todo list](https://github.com/wasi-master/dpylint/blob/main/TODO_LIST.md)
