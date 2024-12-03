import re

pattern = r"\bmul\(\d+,\d+\)\b"


def read_file():
    numbers = []
    multiplication = []
    try:
        with open("day3/q1/input.txt") as f:
            for line in f:
                matches = re.findall(r"mul\((\d+),(\d+)\)", line)

                for match in matches:
                    numbers.append((int(match[0]), int(match[1])))

        for num1, num2 in numbers:
            result = num1 * num2
            multiplication.append(result)
        print(sum(multiplication))

    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    read_file()
