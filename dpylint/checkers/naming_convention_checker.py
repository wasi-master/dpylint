"""Checker for naming conventions"""
import discord
from .basechecker import DiscordBaseChecker
from pylint.interfaces import INFERENCE

class NamingConventionChecker(DiscordBaseChecker):
    """Checker for naming conventions"""

    name = "naming_convention"
    msgs = {
        "C9006": (
            "A bot instance should not be named client",
            "misleading-client",
            "You should not name your bot instance, client since it's misleading",
        ),
    }

    def visit_assign(self, node):
        if node.targets and node.targets[0] and node.targets[0].name == "client":
            if node.value and node.value.func:
                if hasattr(node.value.func, 'name') and "bot" in node.value.func.name.lower():
                    self.add_message(
                        "C9006",
                        node=node,
                        args=(),
                        confidence=INFERENCE
                    )
                if hasattr(node.value.func, 'expr') and node.value.func.expr.name == "commands":
                    self.add_message(
                        "C9006",
                        node=node,
                        args=(),
                    )



