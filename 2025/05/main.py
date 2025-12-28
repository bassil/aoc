
class Inventory:
    def __init__(self, available: set[int], fresh_ranges: set[tuple[int, int]]):
        self.available: set[int] = available
        self.fresh_ranges: set[int] = fresh_ranges

    def part_1(self) -> int:
        """fresh_ranges intervals too large to store individual fresh_id's in memory"""
        result: int = 0
        for available_id in self.available:
            for start, end in self.fresh_ranges:
                if start <= available_id <= end:
                    result += 1
                    break
        return result
    
    def part_2(self) -> int:
        """determine count of all fresh_ids. fresh_ranges overlap"""
        # construct new ranges by removing overlaps.
        non_overlapping_fresh_ranges: list[tuple[int, int]] = []
        for current_interval in self.fresh_ranges:
            if not non_overlapping_fresh_ranges:
                non_overlapping_fresh_ranges.append(current_interval)
                continue
            
            # Start with the current interval and progressively remove overlaps
            intervals_to_add = [current_interval]
            
            for interval in non_overlapping_fresh_ranges:
                new_intervals_to_add = []
                for interval_to_check in intervals_to_add:
                    if is_overlap(interval, interval_to_check):
                        # Remove the overlapping part
                        non_overlaps = remove_overlap_from_current_interval(interval, interval_to_check)
                        if non_overlaps:
                            new_intervals_to_add.extend(non_overlaps)
                    else:
                        # No overlap, keep this interval
                        new_intervals_to_add.append(interval_to_check)
                intervals_to_add = new_intervals_to_add
            
            # Add whatever's left after removing all overlaps
            non_overlapping_fresh_ranges.extend(intervals_to_add)
        
        result: int = 0
        for interval in non_overlapping_fresh_ranges:
            result += interval[1] - interval[0] + 1
        return result


def is_overlap(range_1: tuple[int, int], range_2: tuple[int, int]) -> bool:
    return min(range_1[1], range_2[1]) - max(range_1[0], range_2[0]) >= 0


def remove_overlap_from_current_interval(
        interval: tuple[int, int],
        current_interval: tuple[int, int],
    ) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    # we want the parts of current_interval that are not in interval
    # examples: 
    # [11, 14], [12, 13] -> None. [[12, 13]] is fully in [11, 14].
    # [11, 14], [9, 13] -> [[9, 10]]. 
    # [11, 14], [12, 16] -> [[15, 16]].
    # [11, 14], [9, 16] -> [[9, 10], [15, 16]].
    
    start, end = interval
    curr_start, curr_end = current_interval
    
    # Left portion: part of current_interval before interval starts
    if curr_start < start:
        result.append((curr_start, min(curr_end, start - 1)))
    
    # Right portion: part of current_interval after interval ends
    if curr_end > end:
        result.append((max(curr_start, end + 1), curr_end))
    
    return result


def parse_input(file_name: str) -> Inventory:
    with open(file_name) as text_io_wrapper:
        fresh, available = text_io_wrapper.read().split("\n\n")
    fresh = [interval.split("-") for interval in fresh.split("\n")]
    fresh = [(int(start), int(stop)) for start, stop in fresh]
    available = {int(_) for _ in available.split("\n")}
    return Inventory(available, fresh)


if __name__ == "__main__":
    file_name = '/Users/bassil/dev/aoc/2025/5/input.txt'
    inventory = parse_input(file_name)
    print("part 1:", inventory.part_1())
    print("part 2:", inventory.part_2())
