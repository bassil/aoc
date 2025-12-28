import math


def parse_input(file_name: str) -> tuple[list[list[str]], list[str]]:
    results: list[list[str]] = []
    with open(file_name) as text_io_wrapper:
        file_content: list[str] = text_io_wrapper.read().split("\n")
    raw_operations: str = file_content[-1]
    operations: list[str] = []
    indexes: list[int] = []
    for i, operation in enumerate(raw_operations):
        if operation != " ":
            operations.append(operation)
            indexes.append(i)
    for row in file_content[:-1]:
        result: list[str] = []
        for start in range(len(indexes) - 1):
            result.append(row[indexes[start]:indexes[start+1] - 1])
        # add the final number in the row
        result.append(row[indexes[-1]:])
        results.append(result)
    return results, operations


def perform_computation(values: list[int], operation: str) -> int:
    result: int = 0
    operation = operation.strip()
    if operation == "+":
        result += sum(values)
    if operation == "*":
        result += math.prod(values)
    return result


def get_values_part_1(puzzle_input: list[list[str]], num_rows, column) -> list[int]:
    values: list[int] = []
    for row in range(num_rows):
        values.append(int(puzzle_input[row][column].strip()))
    return values


def get_values_part_2(puzzle_input: list[list[str]], num_rows, column) -> list[int]:
    # ['64 ', '23 ', '314'] -> [4, 431, 623]
    pad: int = 0
    values: list[list[str]] = []
    num_digits: int = 0
    for row in range(num_rows):
        value: list[str] = [_ for _ in puzzle_input[row][column]]
        if len(value) > num_digits:
            num_digits = len(value)
        values.append(value)

    results: list[int] = []
    for col in range(len(values[0])):
        new_number: str = ""
        for row in range(num_rows):
            new_number += values[row][col]
        new_number = new_number.strip()
        if new_number:
            results.append(int(new_number))
    return results


def solve(puzzle_input: list[list[str]], operations: list[str], values_getter) -> int:
    result: int = 0
    num_columns: int = len(puzzle_input[0])
    num_rows: int = len(puzzle_input)
    for column in range(num_columns):
        operation: str = operations[column]
        values = values_getter(puzzle_input, num_rows, column)
        computation: int = perform_computation(values, operation)
        result += computation
    return result


if __name__ == "__main__":
    file_name: str = "D:\\dev\\aoc\\2025\\6\\input.txt"
    puzzle_input, operations = parse_input(file_name)
    print("part_1:", solve(puzzle_input, operations, get_values_part_1))
    print("part_2:", solve(puzzle_input, operations, get_values_part_2))
    
