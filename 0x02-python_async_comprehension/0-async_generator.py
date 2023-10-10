#!/usr/bin/env python3
"""Async generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that takes no argument"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
