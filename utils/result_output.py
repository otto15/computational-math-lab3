from utils.output_data import OutputData


def output_results(output_data: OutputData) -> None:
    print(f'value = {output_data.value}, number of cuts = {output_data.number_of_cuts}')

