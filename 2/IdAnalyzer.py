class IdRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def analyze_validity(self, present_id: str) -> bool:
        split_at = present_id.__len__() // 2
        id_1,id_2 = present_id[:split_at], present_id[split_at:]
        if present_id.startswith("0"):
            return False
        if id_1 == id_2:
            return False
        return True

    def get_invalid_ids(self):
        invalid_ids = []
        for i in range(self.start, self.end + 1):
            if not self.analyze_validity(str(i)):
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

    def get_invalid_ids(self):
        invalid_ids = []
        for id_range in self.id_ranges:
            invalid_ids.extend(id_range.get_invalid_ids())
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
    with open("input.txt", "r") as f:
        puzzle_input = f.read().strip()
        analyzer = IdAnalyzer.get_from_id_string(puzzle_input)
        invalid_ids = analyzer.get_invalid_ids()
        solution = 0
        for invalid_id in invalid_ids:
            solution += invalid_id
        print(solution)

if __name__ == "__main__":
    main()
