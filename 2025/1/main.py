def parse_input(file_path: str) -> list[str]:
    result: list[str]
    with open(file_path) as f:
        result = f.read().split("\n")
    return result


def calculate_next_part_1(current_position: int, direction: str, distance: int) -> tuple[int, int]:
    result: int
    if direction == "R":
        result = (current_position + distance) % 100
    else:
        result = (current_position - distance) % 100
    num_passes: int = 1 if result == 0 else 0
    return result, num_passes


def calculate_next_right_rotation(current_position: int, distance: int) -> tuple[int, int]:
    next_position: int = current_position + distance
    result: int = next_position % 100
    num_passes: int = abs(next_position // 100)
    return result, num_passes


def calculate_next_part_2(current_position: int, direction: str, distance: int) -> tuple[int, int]:
    next_position: int
    result: int
    num_passes: int
    if direction == "R":
        result, num_passes = calculate_next_right_rotation(current_position, distance)
    else:
        # reduce to R rotation
        flipped_current_position: int = (100 - current_position) % 100
        flipped_result, num_passes = calculate_next_right_rotation(flipped_current_position, distance)
        # undo reduction
        result = (100 - flipped_result) % 100
    return result, num_passes


def solve(input: list[str], next_method: callable) -> int:
    result: int = 0
    current_position: int = 50
    for instruction in input:
        num_passes: int = 0
        direction: str = instruction[0]
        distance: int = int(instruction[1:])
        current_position, num_passes = next_method(current_position, direction, distance)
        result += num_passes
    return result


if __name__ == "__main__":
    file_path: str = "/Users/bassil/dev/aoc/2025/1/input.txt"
    puzzle_input: list[str] = parse_input(file_path)
    print("part_1:", solve(puzzle_input, calculate_next_part_1))
    print("part_2:", solve(puzzle_input, calculate_next_part_2))
