def read_file():
    try:
        grid = []
        with open("day4/input.txt") as f:
            lines = f.readlines()

            for line in lines:
                linelist = []
                line = line.strip()
                for i in line:
                    linelist.append(i)
                grid.append(linelist)
        return grid
    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print(f"Error {e}")


def search_from(grid, word, row, col, delta_row, delta_col):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)

    for i in range(word_length):
        r = row + i * delta_row
        c = col + i * delta_col

        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
            return False

    return True


def find_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Down-Right (Diagonal)
        (-1, -1),  # Up-Left (Diagonal)
        (1, -1),  # Down-Left (Diagonal)
        (-1, 1),  # Up-Right (Diagonal)
    ]
    occurrences = []

    for row in range(rows):
        for col in range(cols):
            for delta_row, delta_col in directions:
                if search_from(grid, word, row, col, delta_row, delta_col):
                    occurrences.append(row)

    return occurrences


if __name__ == "__main__":
    grid = read_file()
    ans = find_word(grid, "XMAS")
    print(len(ans))
