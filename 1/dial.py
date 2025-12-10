import sys


class Dial:
    position: int
    number_of_zeroes_hit: int
    number_of_zeroes_passed: int

    def __init__(self, position=50):
        self.position = position
        self.number_of_zeroes_hit = 0
        self.number_of_zeroes_passed = 0

    def roll(self, command: str):
        direction = command[0]
        steps = int(command[1:])
        if direction == 'R':
            self.turn_right(steps)
        elif direction == 'L':
            self.turn_left(steps)
        # print(f"The dial is rotated {command} to point at {self.position}.")
        if self.position == 0:
            self.number_of_zeroes_hit += 1

    def turn_right(self, steps: int):
        rotations = (self.position + steps) // 100
        # if rotations:
        #     print(f"Dial crossed 0 {rotations} time(s)!")
        self.number_of_zeroes_passed += rotations
        self.position = (self.position + steps) % 100

    def turn_left(self, steps: int):
        new_position = self.position - steps
        if new_position < 0:
            rotations = abs(new_position // 100)
            if self.position == 0:
                self.number_of_zeroes_passed += rotations - 1
                # if rotations - 1:
                #     print(f"Dial crossed 0 {rotations} time(s)!")
            else:
                self.number_of_zeroes_passed += rotations
                # if rotations:
                #     print(f"Dial crossed 0 {rotations} time(s)!")
            new_position += 100 * rotations
        if new_position == 0:
            self.number_of_zeroes_passed += 1
            # print(f"Dial crossed 0 1 time(s)!")
        self.position = new_position


def main():
    dial = Dial()
    print("Go!", flush=True)
    puzzle_input = sys.stdin.read().strip().splitlines()
    for line in puzzle_input:
        dial.roll(line)
    print(dial.number_of_zeroes_hit)
    print(dial.number_of_zeroes_passed)

    # while True:
    #     puzzle_input = input()
    #     # if puzzle_input == "exit":
    #     #     break
    #     # elif puzzle_input == "reset":
    #     #     dial = Dial()
    #     #     continue
    #     dial.roll(puzzle_input)
    #
    #     print(dial.number_of_zeroes_hit)
    #     print(dial.number_of_zeroes_passed)
    # with open("input2.txt") as f:
    #     print(f"The dial starts at {dial.position}.")
    #     lines = f.readlines()
    #     for line in lines:
    #         dial.roll(line.strip())
    #         print(f"after {line}: pos={dial.position}, count={dial.number_of_zeroes}")
    # print(dial.number_of_zeroes)
    # assert dial.number_of_zeroes == 5847


if __name__ == "__main__":
    main()
