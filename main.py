# main.py

from BreadImageProcessing import read_image, print_grid, first_pass, write_grid_to_file


def main():
    grid = read_image()

    print("Original Image:")
    print_grid(grid)

    labeled_grid = first_pass(grid)

    print("After First Pass:")
    print_grid(labeled_grid)
    write_grid_to_file(labeled_grid)


if __name__ == "__main__":
    main()