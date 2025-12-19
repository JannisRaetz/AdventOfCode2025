class Grid:
    def __init__(self, new_grid:list[list[str]]):
        self.height = len(new_grid)
        self.width = len(new_grid[0])
        self.grid = new_grid
        self.number_of_accessable_cells = 0
        self.number_of_removed_rolls = 0


    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def mark_accessable_cell(self, corner_limit):
        number_of_neighbors = 0
        self.number_of_accessable_cells = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == "@":
                    # check neighbors
                    neighbors = [
                        (i-1, j), # up
                        (i+1, j), # down
                        (i, j-1), # left
                        (i, j+1),  # right
                        (i-1, j-1), # up-left
                        (i-1, j+1), # up-right
                        (i+1, j-1), # down-left
                        (i+1, j+1)  # down-right
                    ]
                    for ni, nj in neighbors:
                        if 0 <= ni < self.height and 0 <= nj < self.width:
                            if self.grid[ni][nj] == "@" or self.grid[ni][nj] == "X":
                                number_of_neighbors += 1
                    if number_of_neighbors < corner_limit:
                        self.grid[i][j] = "X"
                        self.number_of_accessable_cells += 1
                    number_of_neighbors = 0

    def remove_accessable_marks(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == "X":
                    self.grid[i][j] = "."
                    self.number_of_removed_rolls += 1

    def iterate_removing_accessable_marks(self, corner_limit):
        while self.number_of_accessable_cells > 0:
            self.mark_accessable_cell(corner_limit)
            self.remove_accessable_marks()

    def print_number_of_accessable_cells(self):
        print(self.number_of_accessable_cells)

    def print_number_of_removed_rolls(self):
        print(self.number_of_removed_rolls)


def main():
    import sys
    print("Go!", flush=True)
    puzzle_input = sys.stdin.read().strip()
    puzzle_input = [list(line) for line in puzzle_input.splitlines()]
    # with open("mini-input.txt", "r") as f:
    # with open("super-mini-input.txt", "r") as f:
    # with open("input.txt", "r") as f:
    #     puzzle_input = f.read().strip()
    #     puzzle_input = [list(line) for line in puzzle_input.splitlines()]
    grid = Grid(puzzle_input)
    grid.mark_accessable_cell(corner_limit=4)
    grid.print_number_of_accessable_cells()
    grid.remove_accessable_marks()
    grid.iterate_removing_accessable_marks(corner_limit=4)
    grid.print_number_of_removed_rolls()

if __name__ == "__main__":
    main()