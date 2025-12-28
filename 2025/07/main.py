def parse_input(file_name: str) -> list[list[str]]:
    with open(file_name) as text_io_wrapper:
        contents = text_io_wrapper.read().split("\n")
    return [list(_) for _ in contents]


def part_1(tachyon_manifold: list[list[str]]) -> int:
    result = 0
    start = tachyon_manifold[0].index("S")
    current_beams: set[int] = {start}
    next_beams: set[int] = set()
    for row in tachyon_manifold[1:]:
        splitters: set[int] = set()
        for index, column in enumerate(row):
            if column == "^":
                splitters.add(index)
        for beam in current_beams:
            if beam in splitters:
                result += 1
                next_beams.add(beam - 1)
                next_beams.add(beam + 1)
            else:
                next_beams.add(beam)
        current_beams = next_beams
        next_beams = set()       

    return result

def part_2(tachyon_manifold: list[list[str]]) -> int:
    start = tachyon_manifold[0].index("S")
    current_paths: dict[int, int] = {start: 1}
    for row in tachyon_manifold[1:]:
        splitters = {i for i, col in enumerate(row) if col == "^"}
        next_paths: dict[int, int] = {}
        for beam, count in current_paths.items():
            if beam in splitters:
                next_paths[beam - 1] = next_paths.get(beam - 1, 0) + count
                next_paths[beam + 1] = next_paths.get(beam + 1, 0) + count
            else:
                next_paths[beam] = next_paths.get(beam, 0) + count
        current_paths = next_paths
    
    return sum(current_paths.values())


if __name__ == "__main__":
    file_name: str = "D:\\dev\\aoc\\2025\\7\\input.txt"
    tachyon_manifold: list[list[str]] = parse_input(file_name)
    print("part 1:", part_1(tachyon_manifold))
    print("part 2:", part_2(tachyon_manifold))