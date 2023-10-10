#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
from asyncio import gather
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that run four times in parallel"""
    start_time = time()
    task = [async_comprehension() for i in range(4)]
    await gather(*task)
    end_time = time()
    return end_time - start_time
