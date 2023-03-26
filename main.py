from utils.data_reader import input_data, InputData
from utils.result_output import output_results
from utils.death_dot import find_death_dot_intervals
from methods import integral_solver, rectangle_left, rectangle_right, rectangle_middle, simpson, trapeze
import config
from utils.output_data import OutputData
from typing import Callable


def determine_method(data: InputData) -> tuple[Callable, int]:
    match data.method:
        case 1:
            return simpson.get_method_function(data.integral), simpson.get_accuracy_order()
        case 2:
            return trapeze.get_method_function(data.integral), trapeze.get_accuracy_order()
        case 3:
            return rectangle_left.get_method_function(data.integral), rectangle_left.get_accuracy_order()
        case 4:
            return rectangle_right.get_method_function(data.integral), rectangle_right.get_accuracy_order()
        case 5:
            return rectangle_middle.get_method_function(data.integral), rectangle_middle.get_accuracy_order()
        case _:
            raise ValueError


if __name__ == '__main__':
    try:
        data = input_data()
        intervals = find_death_dot_intervals(data.integral, data.interval[0], data.interval[1])
        method_func, accuracy_order = determine_method(data)
        val, partition_number = integral_solver.solve(
            method_func,
            intervals,
            config.starting_partition_number,
            data.accuracy,
            accuracy_order
        )
        output_results(OutputData(val, partition_number))
    except ValueError as e:
        print(str(e))
    except (EOFError, KeyboardInterrupt):
        print("Something bad happened...")
