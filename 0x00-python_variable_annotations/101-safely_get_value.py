#!/usr/bin/env python3
from typing import Mapping, Any, TypeVar, Union

# Define a generic type variable T
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[T, Any]:
    """
    Get a value from a dictionary safely, with a default value if the key is not found.

    :param dct: A dictionary-like object.
    :param key: The key to look up in the dictionary.
    :param default: The default value to return if the key is not found (optional).
    :return: The value associated with the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
