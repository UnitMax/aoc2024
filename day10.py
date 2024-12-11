print("AOC Day 10")
print("==========")

f = open("day10real.txt", "r")
content = f.read()
f.close()

grid = content.split()
reached = {}

def find_trailheads(grid, x, y, sx, sy, last, check_reached):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return 0
    if grid[y][x] == '.':
        return 0
    c = int(grid[y][x])
    if c != last:
        return 0
    if c == 9:
        if not check_reached:
            return 1
        if not (sx, sy) in reached:
            reached[(sx, sy)] = []
        if (x, y) in reached[(sx, sy)]:
            return 0
        else:
            reached[(sx, sy)].append((x, y))
            return 1
    score = 0
    for (xp, yp) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        nx = x + xp
        ny = y + yp
        score += find_trailheads(grid, nx, ny, sx, sy, last + 1, check_reached)
    return score

overall_score = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '0':
            overall_score += find_trailheads(grid, x, y, x, y, 0, True)

print("Part 1 score =", overall_score)

overall_score = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '0':
            overall_score += find_trailheads(grid, x, y, x, y, 0, False)

print("Part 2 score =", overall_score)