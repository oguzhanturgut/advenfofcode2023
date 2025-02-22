# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:
#
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
#
# What is the sum of all of the calibration values?

with open("day1_2.txt", "r") as file:
    result = 0
    for line in file:
        digits = []
        for index, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            for i, val in enumerate(
                    ["one", "two", "three", "four", "five", "six", "seven", "eight",
                     "nine"]):
                if line[index:].startswith(val):
                    digits.append(i + 1)

        # print(digits)
        result += int(f"{digits[0]}{digits[-1]}")

    print(result)
