class Machine:
    def __init__(self, line: str):
        self.indicator_light_diagram = self._get_indicator_light_diagram(line)
        self.button_wiring_schematic = self._get_button_wiring_schematic(line)
        self.joltage_requirements = self._get_joltage_requirements(line)

    def _get_indicator_light_diagram(self, line: str):
        pass

    def _get_button_wiring_schematic(self, line: str):
        pass

    def _get_joltage_requirements(self, line: str):
        pass


def parse_input(file_name: str) -> str:
    with open(file_name) as text_io_wrapper:
        result = text_io_wrapper.read()
    return result

if __name__ == "__main__":
    file_name = "D:\\dev\\aoc\\2025\\10\\sample.txt"
    puzzle_input = parse_input(file_name)
    