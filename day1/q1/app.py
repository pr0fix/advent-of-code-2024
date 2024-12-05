def read_file():
    try:
        with open("day1/input.txt") as f:
            lines = [line.strip() for line in f]

        tuple_lines = [tuple(map(int, s.split())) for s in lines]

        left = sorted(t[0] for t in tuple_lines)
        right = sorted(t[1] for t in tuple_lines)

        distances = [abs(l - r) for l, r in zip(left, right)]

        dist_sum = sum(distances)

        print(dist_sum)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    read_file()
