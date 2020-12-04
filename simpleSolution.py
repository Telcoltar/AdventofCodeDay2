from operator import xor

from commenUtils import get_input_data


def simple_solution_part_1() -> int:
    passes, lower_limits, higher_limits, letters = get_input_data()
    valid_passwords: int = 0
    for i, passwd in enumerate(passes):
        if lower_limits[i] <= passwd.count(letters[i]) <= higher_limits[i]:
            valid_passwords += 1
    return valid_passwords


def simple_solution_part_2() -> int:
    passes, lower_limits, higher_limits, letters = get_input_data()
    valid_passwords: int = 0
    for i, passwd in enumerate(passes):
        if (passwd[lower_limits[i] - 1] == letters[i]) ^ (passwd[higher_limits[i] - 1] == letters[i]):
            valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    print(simple_solution_part_1())
    print(simple_solution_part_2())
