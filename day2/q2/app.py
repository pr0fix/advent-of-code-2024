def is_valid(line):
    line = [int(num) for num in line]

    if line == sorted(line) or line == sorted(line, reverse=True):
        for i in range(len(line) - 1):
            diff = abs(line[i] - line[i + 1])
            if diff < 1 or diff > 3:
                return False
        return True


def read_file():
    try:
        with open("day2/input.txt") as f:
            lines = [line.split() for line in f]
            results = []
            total = 0

            for line in lines:
                if is_valid(line):
                    results.append(line)
                    total += 1
                else:
                    for i in range(len(line)):
                        dampened = line[:i] + line[i + 1:]
                        if is_valid(dampened):
                            results.append(dampened)
                            total += 1
                            break
            print(total)

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    read_file()
