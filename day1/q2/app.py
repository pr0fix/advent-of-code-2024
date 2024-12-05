def read_file():
    try:
        with open("day1/input.txt") as f:
            lines = [line.strip() for line in f]

        tuple_lines = [tuple(map(int, s.split())) for s in lines]

        left = sorted(t[0] for t in tuple_lines)
        right = sorted(t[1] for t in tuple_lines)
        
        result = []
        for num in left:
            count_in_right = right.count(num)
            result.append(num*count_in_right)

        print(sum(result))
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    read_file()
