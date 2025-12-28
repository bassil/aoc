def parse_input(file_path: str) -> list[list[int, int]]:
    results: list[list[int, int]] = []
    with open(file_path) as f:
        lines: str = f.read().split(',')
    for line in lines:
        start, stop = line.split("-")
        results.append([int(start), int(stop)])
    return results


def is_invalid_part_1(number: int) -> bool:
    number_str: str = str(number)
    num_digits: int = len(number_str)
    # can't be repeated twice if length is odd
    if num_digits % 2 != 0:
        return False
    middle: int = int(num_digits / 2)
    first_half: str = number_str[:middle]
    second_half: str = number_str[middle:]
    if first_half == second_half:
        return True
    return False


def is_matching_prefix(number_str: str, prefix: str) -> bool:
    # test the prefix against each prefix-sized substring of the number
    for i in range(0, len(number_str), len(prefix)):
        if number_str[i: i+len(prefix)] != prefix:
            # print(f"prefix {prefix} doesn't match {number_str}")
            return False
    return True


def is_invalid_part_2(number: int) -> bool:
    """The key insight for part 2 in day 2's puzzle is that we must must find a substring that repeats N times.
    At first I considered adding digits to a stack, but that wouldn't work because a number like 112233 would
    have an exhausted stack, but a number like 121212 would not. I started thinking about substring problems,
    and found this stack overflow post: https://stackoverflow.com/questions/41077268/find-repeated-substring-in-string,
    where one of the answers suggested building a prefix array. 
    This seemed lime a promising direction, so after considering a prefix array for our use case, 
    it seemed like we could simply check each prefix for each number in a brutish approach!
    """
    number_str: str = str(number)
    num_digits: int = len(number_str)
    prefix_list: list[str] = []
    for i in range(1, num_digits):
        prefix_list.append(number_str[:i])
    
    for prefix in prefix_list:
        # if prefix can't repeat, go to the next prefix
        if num_digits % len(prefix) != 0:
            continue
        matching: bool = is_matching_prefix(number_str, prefix)
        if not matching:
            continue
        # print(f"--- MATCH! prefix {prefix} matches {number_str} ---")
        return True
    return False


def solve(puzzle_input: list[list[int, int]], is_invalid: callable) -> int:
    result: int = 0
    for start, stop in puzzle_input:
        for number in range(start, stop + 1):
            if is_invalid(number):
                result += number
    return result


if __name__ == "__main__":
    file_path: str = "/Users/bassil/dev/aoc/2025/2/input.txt"
    puzzle_input: list[list[int, int]] = parse_input(file_path)
    print("part_1:", solve(puzzle_input, is_invalid_part_1))
    print("part_2:", solve(puzzle_input, is_invalid_part_2))

