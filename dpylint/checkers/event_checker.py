"""Checker for anything related to events"""
import discord
from .basechecker import DiscordBaseChecker
import difflib
from dpylint.assets import EVENT_LIST


class EventsChecker(DiscordBaseChecker):
    events_docs = "https://discordpy.readthedocs.io/en/latest/api.html#event-reference"

    name = "events"
    msgs = {
        "E9004": (
            "Invalid Event Name \"%s\", Did you mean %s",
            "invalid-event-name",
            "The event used must be valid (for a list of valid events see {})".format(events_docs),
        ),
        "E9005": (
            "Invalid Parameters passed to %s: %s valid parameters are %s",
            "invalid-event-params",
            "The event parameters must be valid",
        ),
    }

    def visit_asyncfunctiondef(self, event_func):
        # We find any decorators named listener, listen or event
        # These are the decorators used for listening to events
        deco = discord.utils.find(
            lambda x: x.func and (any(x.func.attrname in word for word in ("listener", "listen", "event"))),
            event_func.decorators.nodes,
        )

        # If the function does not have any of those decorators, we just return
        if not deco:
            return
        # We set the name of the event to None, we will change it once we get the name
        event_name = None

        # Check if the event has a listener
        if deco.func.attrname in ("listener", "listen"):
            # Check if the event name was passed to the listener
            if deco.args:
                # Check if the event name is valid
                if deco.args[0].value in EVENT_LIST:
                    # If it is valid then set the event name to the value passed to the decorator
                    event_name = deco.args[0].value
                else:
                    # If the event name is invalid then we add a message and also specify a possible event
                    # We specify the possible event because the user may have a typo
                    possible_event_names = difflib.get_close_matches(deco.args[0].value, EVENT_LIST, n=1, cutoff=0.1)
                    self.add_message(
                        "E9004",
                        node=deco,
                        args=(deco.args[0].value, possible_event_names[0] if possible_event_names else None),
                    )
            else:
                # If the event name was not passed to the listener, the function name is the event name.
                # We validate the event name.
                event_name = self._check_event_name(event_func)
        else:
            # If the decorator was not a listener, then it was a @bot.event decorator,
            # So the function name is the event name.
            event_name = self._check_event_name(event_func)

        if not event_name:
            # If we could not determine the event name, then we return.
            return

        # We get a list of the arguments passed to the event function.
        passed_args = [i.name for i in event_func.args.args if not i.name == "self"]

        # If the amount of arguments passed are not the same as the amount of arguments the event takes
        if len(passed_args) != EVENT_LIST[event_name]:
            # We add a message, the "(" and ")" is used to make it feel like a parameter
            # of a function rather than a parameter name
            self.add_message(
                "E9005",
                node=event_func,
                args=(
                    event_name,
                    "(" + ", ".join(passed_args) + ")",
                    "(" + ", ".join(EVENT_LIST[event_name]) + ")"
                    if event_name in EVENT_LIST
                    else None,
                ),
            )


    def _check_event_name(self, event_func):
        event_name = event_func.name

        # If the event name is not in the list of valid events, then we add a message
        if event_name not in EVENT_LIST:
            # We get the most possible event name and show it in the message
            possible_event_names = difflib.get_close_matches(event_name, EVENT_LIST, n=1, cutoff=0.1)
            self.add_message(
                "E9004",
                node=event_func,
                args=(event_name, possible_event_names[0] if possible_event_names else None),
            )
            # If the event name is invalid, then we return None
            return None
        return event_name
