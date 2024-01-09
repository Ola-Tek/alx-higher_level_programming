#!/usr/bin/python3
"""The shebang Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class and the mylist class inheriting attributes from the list."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
