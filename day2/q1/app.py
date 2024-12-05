def read_file():
    try:
        with open("day2/input.txt") as f:
            lines = [line.split() for line in f]
            results = []
            total = 0

            for line in lines:
                line = [int(num) for num in line]

                if line == sorted(line) or line == sorted(line, reverse=True):
                    valid = True
                    for i in range(len(line) - 1):
                        diff = abs(line[i] - line[i + 1])
                        if diff < 1 or diff > 3:
                            valid = False
                            break
                    results.append(valid)
                else:
                    results.append(False)

            for result in results:
                if result:
                    total += 1

            print(total)

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    read_file()
