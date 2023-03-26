from typing import Callable
from math import sin, exp, cos, sqrt, log

functions: list[Callable[[float], float]] = [
    lambda x: -(x ** 3) - x ** 2 - 2 * x + 1,
    lambda x: sin(x) * exp(x) - 1.5 * x ^ 2,
    lambda x: 3 * x * cos(2 * x),
    lambda x: 1 / sqrt(x),
    lambda x: 1 / (1 - x)
]

functions_primordial: dict[Callable[[float], float], Callable[[float], float]] = {
    functions[0]: lambda x: 1,
    functions[1]: lambda x: 1,
    functions[2]: lambda x: 1,
    functions[3]: lambda x: 2 * sqrt(x),
    functions[4]: lambda x: -log(1 - x)
}

functions_views: list[str] = [
    "-x^3 - x^2 - 2x +1",
    "sin(x) * exp(x) - 1.5x^2",
    "3x * cos(2x)",
    "1 / sqrt(x)",
    "1 / (1 - x)"
]
