def parse_input(file_path: str) -> list[list[int]]:
    with open(file_path) as text_io_stream:
        text = text_io_stream.read()
    banks = text.split("\n")
    results: list[list[int]] = []
    for bank in banks:
        results.append([int(digit) for digit in bank])
    return results


def get_max_joltage(batteries: list[int], num_batteries: int) -> int:
    """Initially, this was the solution to part 2, hard coded with num_batteries set to 12.
    We noticed that this was generalizable to the selection of any number of batteries."""
    joltages: list[int] = batteries[:num_batteries]
    for current_joltage in batteries[num_batteries:]:
        i = 0
        internal_replacement: bool = False
        while i < num_batteries - 1:
            if joltages[i+1] > joltages[i]:
                internal_replacement = True
                break
            i += 1
        if internal_replacement:
            for j in range(i, num_batteries - 1):
                joltages[j] = joltages[j+1]
            joltages[j+1] = current_joltage
        else:
            # check last battery joltage
            if joltages[num_batteries - 1] < current_joltage:
                joltages[num_batteries - 1] = current_joltage
    return int("".join([str(joltage) for joltage in joltages]))


def solve(puzzle_input: list[list[int]], num_batteries: int):
    result: int = 0
    for batteries in puzzle_input:
        result += get_max_joltage(batteries, num_batteries)
    return result


if __name__ == "__main__":
    file_path: str = "/Users/bassil/dev/aoc/2025/3/input.txt"
    puzzle_input: list[list[int]] = parse_input(file_path)
    print("part_1:", solve(puzzle_input, 2))
    print("part_2:", solve(puzzle_input, 12))
