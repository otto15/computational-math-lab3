from typing import Callable


def runge(prev, cur, accuracy_order):
    return abs(cur - prev) / (2 ** accuracy_order - 1)


def calc(f, part_val, intervals) -> float:
    val = 0
    for a, b in intervals:
        val += f(a, b, part_val)
    return val


def solve(func: Callable[[float, float, int], float], intervals: list[tuple[float, float]], part_value: int, accuracy: float,
          accuracy_order: int):
    prev: float = calc(func, part_value, intervals)
    part_value *= 2
    cur: float = calc(func, part_value, intervals)
    while runge(prev, cur, accuracy_order) >= accuracy:
        part_value *= 2
        prev = cur
        cur = calc(func, part_value, intervals)
    return cur, part_value
