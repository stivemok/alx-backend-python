#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn n coroutines of wait_random with the specified
    max_delay and return the list of delays
    n: number of coroutines to spawn
    max_delay: maximim delay in seconds ascending order"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
