#!/usr/bin/python3
"""This module provides the lookup function to list attributes and methods of an object."""

def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
