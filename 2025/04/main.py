def parse_input(file_path: str) -> list[list[str]]:
    with open(file_path) as text_io_wrapper:
        text: str = text_io_wrapper.read()
    result: list[list[str]] = [list(_) for _ in text.split("\n")]
    return result


def num_adjacent(grid: list[list[str]], row: int, column: int) -> int:
    result: int = 0

    column_start = column - 1 if column > 0 else column
    column_end = column + 1 if column < len(grid) - 1 else len(grid) - 1
    row_start = row - 1 if row > 0 else row
    row_end = row + 1 if row < len(grid[column]) - 1 else len(grid[column]) - 1

    for j in range(column_start, column_end + 1):
        for i in range(row_start, row_end + 1):
            if i == row and j == column:
                continue
            if grid[j][i] == "@":
                result += 1
    return result


def part_1(grid: list[list[str]]) -> int:
    result: int = 0
    # 0,0 is top left
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            # print(f"row: {row}, column: {column}, value: {grid[column][row]}")
            # print("getting adjacent cells")
            if grid[column][row] == ".":
                continue
            if num_adjacent(grid, row, column) < 4:
                result += 1
    return result


def part_2(grid: list[list[str]], previous_num_removed: int = 0) -> int:
    """Dynamic programming solution"""
    num_removed: int = 0
    # 0,0 is top left
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            # print(f"row: {row}, column: {column}, value: {grid[column][row]}")
            # print("getting adjacent cells")
            if grid[column][row] == ".":
                continue
            if num_adjacent(grid, row, column) < 4:
                num_removed += 1
                grid[column][row] = "."
    if num_removed ==  0:
        return previous_num_removed
    return previous_num_removed + part_2(grid, num_removed)
    

if __name__ == "__main__":
    file_path: str = "/Users/bassil/dev/aoc/2025/4/input.txt"
    grid: list[list[str]] = parse_input(file_path)
    print("part 1:", part_1(grid))
    print("part 2:", part_2(grid))
