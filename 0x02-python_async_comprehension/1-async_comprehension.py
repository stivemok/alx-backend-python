#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine tah takes no argument and return
    ten random numbers"""
    return [i async for i in async_generator()]
