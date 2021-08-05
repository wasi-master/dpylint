"""Discord.py Linter"""
__all__ = ("register",)
__title__ = "dpylint"
__version__ = "0.0.1"

from .checkers import HasPermissionsChecker, EventsChecker


def register(linter):
    """Registers the linters to pylint"""
    linter.register_checker(HasPermissionsChecker(linter))
    linter.register_checker(EventsChecker(linter))
