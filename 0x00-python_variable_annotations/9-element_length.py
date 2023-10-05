#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in a list of sequences.

    :param lst: An iterable of sequences.
    :return: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
