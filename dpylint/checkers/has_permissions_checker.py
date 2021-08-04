"""A checker for checking the commands.has_permissions decorator"""
import astroid
import discord
from .basechecker import DiscordBaseChecker
import difflib


class HasPermissionsChecker(DiscordBaseChecker):
    permissions_docs = "https://discordpy.readthedocs.io/en/latest/api.html#discord.Permissions"

    name = "invalid-permission"
    priority = -1
    msgs = {
        "E9001": (
            "Invalid Permission Name: \"%s\", Did you mean %s",
            "invalid-permission-name",
            "All permissions passed to has_permissions must be valid (for a list of valid permissions see {})".format(
                permissions_docs
            ),
        ),
        "W9002": (
            "Permission value should not be \"%s\", it should be either True or False",
            "invalid-permission-value",
            "The value passed to has_permissions should be either True or False",
        ),
        "W9003": (
            "No Permissions Specified",
            "no-permissions-specified",
            "There should be at least one valid permission passed to has_permissions",
        ),
    }

    def visit_asyncfunctiondef(self, node):
        # We find the decorator that is named has_permissions.
        deco = discord.utils.get(node.decorators.nodes, func__attrname="has_permissions")

        # If the decorator was not found then we return
        if not deco:
            return

        # If no keywords were passed to has_permissions then we add a message
        if not deco.keywords:
            self.add_message("W9003", node=deco)

        # We loop through all the keywords to check if each keyword is a valid permission name
        for kwarg in deco.keywords:
            # We don't use a list of permissions and just see if the attribute exists in the
            # discord.Permissions class because maintaining a list of permissions list is hard
            if not hasattr(discord.Permissions, kwarg.arg):

                # If the user mistakenly uses manage_server instead of manage_guild, we add a message
                if kwarg.arg == 'manage_server':
                    self.add_message("E9001", node=deco, args=(kwarg.arg, 'manage_guild'))
                    # We continue to check for other permissions since we already know this one is
                    # invalid and we don't want to add another message for this being invalid
                    continue

                # We get the possible permission names
                possible_perm_names = difflib.get_close_matches(kwarg.arg, dir(discord.Permissions), n=1, cutoff=0.1)
                # We add a message with the possible permission names
                self.add_message(
                    "E9001",
                    node=deco,
                    args=(kwarg.arg, possible_perm_names[0] if possible_perm_names else None),
                )

            # We check if the value of the keyword is True or False
            if not (isinstance(kwarg.value, astroid.node_classes.Const) and kwarg.value.value in (True, False)):
                # If the value is something other than True or False, we send a message
                self.add_message("W9002", node=deco, args=(kwarg.value.value))
