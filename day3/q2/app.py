import re

pattern = r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"

def read_file():
    total = 0
    inside_do_block = True
    try:
        with open("day3/input.txt") as f:
            content = f.read()
            for match in re.finditer(pattern, content):
                if match.group(1):
                    inside_do_block = True
                elif match.group(2):
                    inside_do_block = False
                elif match.group(3) and inside_do_block:
                    num1, num2 = int(match.group(3)), int(match.group(4))
                    total += num1 * num2

        print(total)

    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    read_file()
