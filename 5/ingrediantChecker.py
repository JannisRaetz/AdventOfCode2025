class IngrediantRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_within_range(self, amount):
        return self.start <= amount <= self.end

    def to_list(self):
        return list(range(self.start, self.end))

class IngrediantRanges:
    def __init__(self, ranges_string: str):
        self.ranges = []
        for line in ranges_string.splitlines():
            start, end = line.split("-")
            self.ranges.append(IngrediantRange(int(start), int(end)))

    def is_fresh(self, id: int) -> bool:
        for ingrediant_range in self.ranges:
            if ingrediant_range.start >= id >= ingrediant_range.end:
                continue
            if ingrediant_range.is_within_range(id):
                return True
        return False

    def count_fresh_ingredients(self, ids: list[int]) -> int:
        count = 0
        for id in ids:
            if self.is_fresh(id):
                count += 1
        return count

    def count_all_fresh_ingredients(self) -> int:
        all_ingredients = set()
        for ingrediant_range in self.ranges:
            all_ingredients.update(ingrediant_range.to_list())
        return len(all_ingredients)

def main():
    # import sys

    input_ranges = []
    input_ids = []
    input_ranges_finished = False
    # print("Go!", flush=True)
    # puzzle_input = sys.stdin.read().strip()

    with open("mini-input.txt", "r") as f:
    # with open("super-mini-input.txt", "r") as f:
    # with open("input.txt", "r") as f:
        puzzle_input = f.read().strip()
        input_ranges, input_ids = puzzle_input.split("\n\n")
    inpout_ranges = IngrediantRanges(input_ranges)
    print (inpout_ranges.count_fresh_ingredients([int(id) for id in input_ids.splitlines()]))
    print (inpout_ranges.count_all_fresh_ingredients())

if __name__ == "__main__":
    main()
