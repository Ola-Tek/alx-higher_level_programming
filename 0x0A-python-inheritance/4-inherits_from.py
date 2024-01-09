#!/usr/bin/python3
"""Defines a function that checks for an object"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class or inherited directly from a specified class.
    Args:
        obj(any):represents the object of an instance or specified class.
        a_class(any): represents the class tomatch the objects.
    Return:
        True if the the object is an instance of a class and false if othereise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
