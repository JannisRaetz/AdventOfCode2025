class Battery:
    joltage: str

    def __init__(self, joltage: str):
        self.joltage = joltage

    def get_max_joltage(self, number_of_battery_slots) -> int:
        digits = []
        search_list = self.joltage
        for i in range(number_of_battery_slots):
            last_possible_index = len(search_list) - (number_of_battery_slots - i - 1)
            current_search_list = search_list[:last_possible_index]
            if len(current_search_list) == 1:
                digits.extend(list(search_list))
                break
            max_possible_digit = max(list(current_search_list))
            digits.append(int(max_possible_digit))

            search_list = search_list[search_list.find(max_possible_digit) + 1:]
        max_joiltage = int("".join(str(x) for x in digits))
        return int(max_joiltage)

    # def get_max_joltage(self) -> int:
    #     digit1: int = 0
    #     digit1_finished = False
    #     digit2: int = 0
    #     for i in range(len(self.joltage)):
    #         current_digit = int(self.joltage[i])
    #         if current_digit > digit1 and not digit1_finished and i < len(self.joltage) - 1:
    #             digit1 = current_digit
    #             digit2 = 0
    #             if digit1 == 9:
    #                 digit1_finished = True
    #         elif current_digit > digit2:
    #             digit2 = current_digit
    #             if digit2 == 9:
    #                 break
    #     print(int(str(digit1) + str(digit2)))
    #     return int(str(digit1) + str(digit2))


class BatteryBank:
    batteries: list[Battery]

    def __init__(self, batteries_string: str):
        self.batteries = []
        for line in batteries_string.splitlines():
            self.batteries.append(Battery(line.strip()))

    def get_total_max_joltage(self, number_of_battery_slots) -> int:
        total = 0
        for battery in self.batteries:
            total += battery.get_max_joltage(number_of_battery_slots)
        return total


def main():
    import sys
    print("Go!", flush=True)
    puzzle_input = sys.stdin.read().strip()
    # with open("mini-input.txt", "r") as f:
    # with open("super-mini-input.txt", "r") as f:
    # with open("input.txt", "r") as f:
    #     puzzle_input = f.read().strip()
    battery_bank = BatteryBank(puzzle_input)
    print(battery_bank.get_total_max_joltage(2))
    print(battery_bank.get_total_max_joltage(12))


if __name__ == "__main__":
    main()
