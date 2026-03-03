# image_functions.py

import os

def read_image():
    while True:
        filename = input("Enter image filename: ")
        if os.path.exists(filename):
            break
        print("File does not exist. Try again.")

    grid = []
    with open(filename, "r") as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            grid.append(row)

    return grid


def print_grid(grid):
    for row in grid:
        for value in row:
            print(f"{value:3}", end="")
        print()
    print()


def first_pass(grid):
    rows = len(grid)
    cols = len(grid[0])
    label = 1

    new_grid = [[0]*cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 1:

                top = new_grid[r-1][c] if r > 0 else 0
                left = new_grid[r][c-1] if c > 0 else 0

                if top == 0 and left == 0:
                    label += 1
                    new_grid[r][c] = label

                elif top != 0 and left == 0:
                    new_grid[r][c] = top

                elif top == 0 and left != 0:
                    new_grid[r][c] = left

                else:
                    new_grid[r][c] = min(top, left)

    return new_grid


def write_grid_to_file(grid):
    with open("ss", "w") as file:
        for row in grid:
            line = " ".join(map(str, row))
            file.write(line + "\n")
