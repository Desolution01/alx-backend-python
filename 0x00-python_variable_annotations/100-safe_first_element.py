#!/usr/bin/env python3

""" Duck typing - first element of a sequence """

from typing import Any, Mapping, Union

def safely_get_value(dct: Mapping, key: Any, default: Any = None) -> Any:
    '''
    Retrieves a value from a dictionary using a given key.

    :param dct: The dictionary to retrieve the value from.
    :param key: The key to search for in the dictionary.
    :param default: The value to return if the key is not found (default is None).
    :return: The value associated with the key in the dictionary, or the default value if not found.
    '''
    return dct.get(key, default)
