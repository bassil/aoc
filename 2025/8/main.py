from __future__ import annotations
import math
from itertools import combinations


VERY_LARGE_NUMBER: int = 2147483647


class JunctionBox:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self) -> list[int]:
        return [self.x, self.y, self.z]

    def __repr__(self) -> str:
        return f"JunctionBox(x={self.x}, y={self.y}, z={self.z})"
    
    def distance(self, other: JunctionBox) -> float:
        return math.dist(self.__iter__(), other.__iter__())


class Circuit:
    def __init__(self, junction_boxes: list[JunctionBox]):
        self.junction_boxes = junction_boxes

    def __repr__(self):
        return f"Circuit: ({self.junction_boxes})"

    def __eq__(self, other: Circuit):
        return self.junction_boxes == other.junction_boxes

    def add(self, other: Circuit):
        for junction_box in other.junction_boxes:
            self.junction_boxes.append(junction_box)

    def distance(self, other: Circuit):
        min_distance: float = VERY_LARGE_NUMBER
        for junction_box in self.junction_boxes:
            for other_junction_box in other.junction_boxes:
                d = junction_box.distance(other_junction_box)
                if d < min_distance:
                    min_distance = d
        return min_distance



class Grid:
    def __init__(self, junction_boxes: list[JunctionBox]):
        self.size: int = len(junction_boxes)
        self.circuits: list[Circuit] = self._make_circuits(junction_boxes)

    def _make_circuits(self, junction_boxes: list[JunctionBox]) -> list[Circuit]:
        return [Circuit([junction_box]) for junction_box in junction_boxes]

    def make_shortest_connections(self, num_connections: int):
        pairs: combinations[tuple[Circuit, Circuit]] = combinations(self.circuits, 2)
        distances = {}
        for pair in pairs:
            # calculate the distance and add to something
            _first, _second = pair
            distance = _first.distance(_second)
            distances[distance] = pair
        
        for i, distance in enumerate(sorted(distances.keys())):
            if i == num_connections:
                break

            first: Circuit
            second: Circuit
            first_circuit: Circuit = Circuit([])
            second_circuit: Circuit = Circuit([])
            first, second = distances[distance]
            # find the circuit that each junction_box belongs to
            for circuit in self.circuits:
                if first.junction_boxes[0] in circuit.junction_boxes:
                    first_circuit = circuit
                if second.junction_boxes[0] in circuit.junction_boxes:
                    second_circuit = circuit
            if first_circuit == second_circuit:
                continue
            else:
                self.circuits.remove(first_circuit)
                self.circuits.remove(second_circuit)
                first_circuit.add(second_circuit)
                self.circuits.append(first_circuit)
                if num_connections == -1 and len(self.circuits) == 1:
                    return (
                        first.junction_boxes[0].x 
                        * second.junction_boxes[0].x
                    )               

    
    def solve(self, num_connections: int):
        result = self.make_shortest_connections(num_connections)
        if num_connections == -1:
            return result
        sizes: list[int] = [0, 0 , 0]
        for circuit in self.circuits:
            sizes.append(len(circuit.junction_boxes))
            sizes = sorted(sizes)[1:]
        result = 1
        for size in sizes:
            result *= size
        return result


def parse_input(file_name: str) -> list[JunctionBox]:
    with open(file_name) as text_io_wrapper:
        lines = text_io_wrapper.read().split("\n")
    results: list[JunctionBox] = []
    for line in lines:
        x, y, z = line.split(",")
        results.append(JunctionBox(int(x), int(y), int(z)))
    return results
        

if __name__ == "__main__":
    file_name = "D:\\dev\\aoc\\2025\\8\\input.txt"
    junction_boxes = parse_input(file_name)
    grid = Grid(junction_boxes)
    print("part_1:", grid.solve(num_connections=1000))
    grid = Grid(junction_boxes)
    print("part_2:", grid.solve(num_connections=-1))
