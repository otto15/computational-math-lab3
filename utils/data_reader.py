from typing import Callable
from data.functions import functions, functions_views


class InputData:
    integral: Callable[[float], float]
    method: int
    interval: tuple[float, float]
    accuracy: float


def input_choice(choices: set, msg: str) -> int:
    choice: int
    while True:
        try:
            choice = int(input(msg))
            if choice not in choices:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid choice, try again...")


def choose_integral() -> Callable[[float], float]:
    for i in range(len(functions_views)):
        print(f'{i + 1}. {functions_views[i]}')
    eq_choice: int = input_choice(set(range(1, len(functions_views) + 1)), "Type a number of the desired function: ")
    return functions[eq_choice - 1]


def input_data() -> InputData:
    data: InputData = InputData()
    data.integral = choose_integral()
    data.method = input_choice({1, 2, 3, 4, 5},
                               "1. simpson method\n2. trapezoid method\n3. rectangle method (left)\n4. rectangle method (right)\n5. rectangle method (middle)\nChoose method: ")

    data.interval = input_interval()
    data.accuracy = input_accuracy()

    return data


def input_interval() -> tuple[float, float]:
    while True:
        try:
            start: float = float(input("Type start of the interval: ").replace(",", "."))
            break
        except ValueError:
            print("Invalid input, try again... ")

    while True:
        try:
            end = float(input("Type end of the interval: ").replace(",", "."))
            if end <= start:
                print("End must be greater than start, try again...")
                continue
            break
        except ValueError:
            print("Invalid input, try again... ")

    return start, end


def input_accuracy() -> float:
    while True:
        try:
            accuracy: float = float(input("Type accuracy: ").replace(",", "."))
            if accuracy <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid accuracy, try again")

    return accuracy
