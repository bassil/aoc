def parse_input(file_name: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    with open(file_name) as text_io_wrapper:
        file = text_io_wrapper.read().split("\n")
    for line in file:
        device, children = line.split(": ")
        children = children.split(" ")
        result[device] = children
    return result


def count_paths(
    graph: dict[str, list[str]], current: str, target: str, memo: dict[str, int]
) -> int:
    if current in memo:
        return memo[current]

    if current == target:
        result = 1
    else:
        result = sum(
            count_paths(graph, child, target, memo) for child in graph.get(current, [])
        )
    memo[current] = result
    return result


def count_paths_visiting(
    graph: dict[str, list[str]],
    current: str,
    target: str,
    required: frozenset[str],
    visited: frozenset[str],
    memo: dict[tuple[str, frozenset[str]], int],
) -> int:
    if current in required:
        new_visited = visited | {current}  # set union
    else:
        new_visited = visited

    memo_key = (current, new_visited)

    if memo_key in memo:
        return memo[memo_key]

    if current == target:
        result = 1 if new_visited == required else 0
    else:
        result = sum(
            count_paths_visiting(graph, child, target, required, new_visited, memo)
            for child in graph.get(current, [])
        )

    memo[memo_key] = result
    return result


if __name__ == "__main__":
    file_name = "D:\\dev\\aoc\\2025\\11\\input.txt"
    graph = parse_input(file_name)
    print("part 1:", count_paths(graph, "you", "out", memo={}))
    required = frozenset(["dac", "fft"])
    print(
        "part 2:",
        count_paths_visiting(
            graph,
            "svr",
            "out",
            required,
            frozenset(),
            {},
        ),
    )
