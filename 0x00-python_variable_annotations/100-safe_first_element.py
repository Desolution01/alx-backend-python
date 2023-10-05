#!/usr/bin/env python3
from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence if it exists, or None if the sequence is empty.

    :param lst: A sequence of elements of unknown types.
    :return: The first element of the sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
