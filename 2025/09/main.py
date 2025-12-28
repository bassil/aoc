from __future__ import annotations
from itertools import combinations

class Cell:
    def __init__(self, coordinates: list[str]):
        self.x: int = int(coordinates[0])
        self.y: int = int(coordinates[1])
    
    def __repr__(self) -> str:
        return f"Cell: (x: {self.x},\ty: {self.y})"

    def area(self, other: Cell) -> int:
        return abs(self.x - other.x + 1) * abs(self.y - other.y + 1)


def parse_input(file_name: str) -> list[Cell]:
    with open(file_name) as text_io_wrapper:
        result: list[str] = text_io_wrapper.read().split("\n")
    return [Cell(line.split(",")) for line in result]


def part_1(puzzle_input: list[Cell]) -> int:
    pairs = combinations(puzzle_input, 2)
    max_area = -1
    max_pair: tuple[Cell, Cell] | None = None 
    pair: tuple[Cell, Cell]
    for pair in pairs:
        area = pair[0].area(pair[1])
        if area > max_area:
            max_area = area
            max_pair = pair
    print("max pair:", max_pair)
    return max_area


def is_valid(pair: tuple[Cell, Cell]) -> bool:
    result = False
    return result


def part_2(puzzle_input: list[Cell]) -> int:
    pairs = combinations(puzzle_input, 2)
    max_area = -1
    max_pair: tuple[Cell, Cell] | None = None 
    pair: tuple[Cell, Cell]
    for pair in pairs:
        if not is_valid(pair):
            continue
        area = pair[0].area(pair[1])
        if area > max_area:
            max_area = area
            max_pair = pair
    print("max pair:", max_pair)
    return max_area


if __name__ == "__main__":
    file_name = "D:\\dev\\aoc\\2025\\9\\input.txt"
    puzzle_input = parse_input(file_name)
    print("part 1:", part_1(puzzle_input))
