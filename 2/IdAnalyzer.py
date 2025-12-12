import sys


class IdRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def analyze_simple_validity(self, present_id: str) -> bool:
        split_at = present_id.__len__() // 2
        id_1, id_2 = present_id[:split_at], present_id[split_at:]
        # if present_id.startswith("0"):
        #     return False
        if id_1 == id_2:
            return False
        return True

    def analyze_complex_validity(self, present_id: str) -> bool:
        # if present_id.startswith("0"):
        #     return False
        return not self.has_repetition(present_id)

    def has_repetition(self, present_id: str) -> bool:
        length = len(present_id)
        if length <= 1:
            return False
        has_repetition = True

        for i in range(1, length // 2 + 1):
            if length % i != 0:
                continue
            repetitions = length // i
            parts = [present_id[(i * len(present_id)) // repetitions: ((i + 1) * len(present_id)) // repetitions] for i in range(repetitions)]
            if all(part == parts[0] for part in parts):
                has_repetition = True
                break
            else:
                has_repetition = False
        return has_repetition

    def get_simple_invalid_ids(self):
        invalid_ids = []
        for i in range(self.start, self.end + 1):
            if not self.analyze_simple_validity(str(i)):
                # print(i)
                invalid_ids.append(i)
        return invalid_ids

    def get_complex_invalid_ids(self):
        invalid_ids = []
        for i in range(self.start, self.end + 1):
            if not self.analyze_complex_validity(str(i)):
                # print(i)
                invalid_ids.append(i)
        return invalid_ids

    def get_from_string(id_string: str) -> 'IdRange':
        parts = id_string.split("-")
        start, end = int(parts[0]), int(parts[1])
        return IdRange(start, end)


class IdAnalyzer:
    def __init__(self, id_ranges: list[IdRange]):
        self.id_ranges = id_ranges

    def get_simple_invalid_ids(self):
        invalid_ids = []
        for id_range in self.id_ranges:
            invalid_ids.extend(id_range.get_simple_invalid_ids())
        return invalid_ids

    def get_complex_invalid_ids(self):
        invalid_ids = []
        for id_range in self.id_ranges:
            invalid_ids.extend(id_range.get_complex_invalid_ids())
        return invalid_ids

    def get_from_id_string(id_string: str) -> 'IdAnalyzer':
        id_ranges = []
        id_range_strings = id_string.split(",")
        for id_range_string in id_range_strings:
            id_range = IdRange.get_from_string(id_range_string)
            id_ranges.append(id_range)
        return IdAnalyzer(id_ranges)


def main():
    # with open("mini-input.txt", "r") as f:
    # with open("input.txt", "r") as f:
        # puzzle_input = f.read().strip()
        print("Go!", flush=True)
        puzzle_input = sys.stdin.read().strip()
        analyzer = IdAnalyzer.get_from_id_string(puzzle_input)
        simple_invalid_ids = analyzer.get_simple_invalid_ids()
        solution_1 = 0
        for invalid_id in simple_invalid_ids:
            solution_1 += invalid_id
        print(solution_1)

        complex_invalid_ids = analyzer.get_complex_invalid_ids()
        solution_2 = 0
        for invalid_id in complex_invalid_ids:
            # print(invalid_id)
            solution_2 += invalid_id
        print(solution_2)


if __name__ == "__main__":
    main()
