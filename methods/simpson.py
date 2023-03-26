from typing import Callable


def get_accuracy_order():
    return 4


def get_method_function(f: Callable[[float], float]):
    return lambda a, b, part_number: calculate(f, a, b, part_number)


def calculate(f: Callable[[float], float], a: float, b: float, part_number: int) -> float:
    h: float = (b - a) / part_number
    sm: float = (f(a) + f(b))
    for step in range(1, part_number):
        val = f(a + h * step) * 2
        if step % 2 != 0:
            val *= 2
        sm += val
    return (h / 3) * sm
