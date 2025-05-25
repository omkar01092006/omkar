import time
import os
import copy
print("Name:Omkar")
print("USN:1AY24AI079")
print("Section:O")

WIDTH = 20
HEIGHT = 10


DELAY = 0.5  # seconds


def create_grid():
    return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]


def print_grid(grid):
    os.system("cls" if os.name == "nt" else "clear")
    for row in grid:
        print("".join(['█' if cell else ' ' for cell in row]))


def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),         ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
            count += grid[nx][ny]
    return count


def next_generation(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid


def main():
    grid = create_grid()


    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

    while True:
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
