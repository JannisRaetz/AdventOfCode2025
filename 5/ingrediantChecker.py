class IngrediantRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_within_range(self, amount):
        return self.start <= amount <= self.end

    def to_list(self):
        return list(range(self.start, self.end))

    def get_size(self) -> int:
        return self.end - self.start + 1

    def overlaps(self, range_b: 'IngrediantRange') -> bool:
        return self.start >= range_b.end or self.end >= range_b.start

    def __str__(self):
        return f"{self.start}:{self.end}"

class IngrediantRanges:
    def __init__(self, ranges_string: str):
        self.ranges = []
        for line in ranges_string.splitlines():
            start, end = line.split("-")
            self.ranges.append(IngrediantRange(int(start), int(end)))
        self.ranges_length = len(self.ranges)
        self.ranges.sort(key=lambda x: x.start)

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

    def consolidate_ranges(self):
        i = 0
        while i < self.ranges_length:
            if (i+1 < self.ranges_length):
                range_a = self.ranges[i]
                range_b = self.ranges[i+1]
                if range_a.overlaps(range_b):
                    self.ranges[i] = IngrediantRange(min(range_a.start, range_b.start),max(range_a.end, range_b.end))
                    self.ranges.pop(i+1)
                    i -= 1
                    self.ranges_length -= 1
            i += 1
        # for i in range(self.ranges_length).__reversed__():
        #     if (i-1 < 0):
        #         range_a = self.ranges[i]
        #         range_b = self.ranges[i-1]
        #         if range_a.overlaps(range_b):
        #             self.ranges[i] = IngrediantRange(min(range_a.start, range_b.start),max(range_a.end, range_b.end))
        #             self.ranges.pop(i-1)
        #             i += 1
        #             self.ranges_length += 1

    def get_size(self):
        size = 0
        for r in self.ranges:
            size += r.get_size()
        return size

def main():
    import sys
    print("Go!", flush=True)
    puzzle_input = sys.stdin.read().strip()

    # with open("mini-input.txt", "r") as f:
    # with open("super-mini-input.txt", "r") as f:
    # with open("input.txt", "r") as f:
    #     puzzle_input = f.read().strip()
    #     input_ranges, input_ids = puzzle_input.split("\n\n")
    input_ranges, input_ids = puzzle_input.split("\n\n")
    inpout_ranges = IngrediantRanges(input_ranges)
    print (inpout_ranges.count_fresh_ingredients([int(id) for id in input_ids.splitlines()]))
    inpout_ranges.consolidate_ranges()
    print (inpout_ranges.get_size())


if __name__ == "__main__":
    main()
