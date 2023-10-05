#!/usr/bin/env python3
"""Function that converts a variable to a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a variable to a tuple"""
    return k, v ** 2
