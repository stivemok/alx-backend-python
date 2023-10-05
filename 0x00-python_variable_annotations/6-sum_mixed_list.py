#!/usr/bin/env python3
"""Function that takes list of integers and
floats then returns the sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of mixed numbers in the list as float"""
    return sum(mxd_lst)
