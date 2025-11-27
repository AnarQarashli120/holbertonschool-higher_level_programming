#!/usr/bin/python3
"""Module defining the MyList class."""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Print the list but sorted in ascending order."""
        print(sorted(self))
