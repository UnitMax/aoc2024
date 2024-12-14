import re
from termcolor import colored

GRID_WIDTH = 101
GRID_HEIGHT = 103

grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

print("AOC Day 14")
print("==========")

f = open("day14real.txt", "r")
content = f.read()
f.close()

# f = from, t = to
def move(grid, fx, fy, tx, ty, seconds):
    newx = (fx + (tx * seconds)) % GRID_WIDTH
    newy = (fy + (ty * seconds)) % GRID_HEIGHT
    grid[newy][newx] += 1

def print_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            c = grid[y][x]
            if int(c) > 0:
                print(colored(c, "green"), end='')
            else:
                print(c, end='')

        print("")

def get_score(grid):
    wcenter = ((GRID_WIDTH - 1) // 2)
    hcenter = ((GRID_HEIGHT - 1) // 2)
    score = 1
    for (xfrom, xto, yfrom, yto) in [(0, wcenter - 1, 0, hcenter - 1),
                                     (wcenter + 1, GRID_WIDTH - 1, 0, hcenter - 1),
                                     (0, wcenter - 1, hcenter + 1, GRID_HEIGHT - 1),
                                     (wcenter + 1, GRID_WIDTH - 1, hcenter + 1, GRID_HEIGHT - 1)]:
        qscore = 0
        for y in range(yfrom, yto + 1):
            for x in range(xfrom, xto + 1):
                qscore += grid[y][x]
        score *= qscore
    return score

for line in content.split("\n"):
    match = re.search(r"p=(-?[0-9]+,-?[0-9]+) v=(-?[0-9]+,-?[0-9]+)$", line)
    if not match:
        continue
    p_coords = match.group(1).split(",")
    v_coords = match.group(2).split(",")
    px = int(p_coords[0])
    py = int(p_coords[1])
    vx = int(v_coords[0])
    vy = int(v_coords[1])

    move(grid, px, py, vx, vy, 100)


print("Part 1, score =", get_score(grid))