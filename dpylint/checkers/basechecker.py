import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class DiscordBaseChecker(BaseChecker):
    __implements__ = IAstroidChecker
