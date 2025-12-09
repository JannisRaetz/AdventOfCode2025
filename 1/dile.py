class Dile:
    position: int
    number_of_zeroes: int

    def __init__(self, position=50):
        self.position = position
        self.number_of_zeroes = 0

    def roll(self, command: str):
        direction = command[0]
        steps = int(command[1:])
        if direction == 'R':
            self.turn_right(steps)
        elif direction == 'L':
            self.turn_left(steps)

        if self.position == 0:
            self.number_of_zeroes += 1

    def turn_right(self, steps: int):
        self.position = (self.position + steps) % 100

    def turn_left(self, steps: int):
        position = (self.position - steps) % 100
        if position < 0:
            position += 100
        self.position = position


def main():
    dile = Dile()
    while True:
        puzzle_input = input()
        for line in puzzle_input.splitlines():
            dile.roll(line)
        print(dile.number_of_zeroes)


if __name__ == "__main__":
    main()
