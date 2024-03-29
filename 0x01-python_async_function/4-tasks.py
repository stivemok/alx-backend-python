#!/usr/bin/env python3
"""new function task_wait_n alter from wait_n"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times"""
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*coroutines)
    return sorted(wait_times)
