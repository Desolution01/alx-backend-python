#!/usr/bin/env python3
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string k as the first element and the square of v as the second element.

    :param k: The input string.
    :param v: The input integer or float.
    :return: A tuple with the string k and the square of v as a float.
    """
    return (k, float(v ** 2))
