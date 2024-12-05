import re

pattern = r"\bmul\(\d+,\d+\)\b"


def read_file():
    total = 0
    try:
        with open("day3/input.txt") as f:
            for line in f:
                matches = re.findall(r"mul\((\d+),(\d+)\)", line)

                for match in matches:
                    num1, num2 = int(match[0]), int(match[1])
                    total += num1 * num2

        print(total)

    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    read_file()
