from typing import Callable


def get_accuracy_order():
    return 2


def get_method_function(f: Callable[[float], float]):
    return lambda a, b, part_number: calculate(f, a, b, part_number)


def calculate(f: Callable[[float], float], a: float, b: float, part_number: int) -> float:
    h: float = (b - a) / part_number
    sigma: float = (f(a) + f(b)) / 2
    for step in range(1, part_number):
        sigma += f(a + h * step)
    return h * sigma
