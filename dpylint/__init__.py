"""Discord.py Linter"""
from .checkers import HasPermissionsChecker, EventsChecker, NamingConventionChecker


def register(linter):
    """Registers the linters to pylint"""
    linter.register_checker(HasPermissionsChecker(linter))
    linter.register_checker(EventsChecker(linter))
    linter.register_checker(NamingConventionChecker(linter))

__name__    = "dpylint"
__title__   =  __name__
__license__ = "MIT"
__version__ = "0.2.2"
__author__  = "Arian Mollik Wasi"
__github__  = "https://github.com/wasi-master/dpylint"

__all__ = ("register",)
