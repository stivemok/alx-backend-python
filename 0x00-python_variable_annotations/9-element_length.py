#!/usr/bin/env python3
"""Annotate fnction parameter and return values with appropriate types."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Return list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]
