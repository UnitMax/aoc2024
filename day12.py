print("AOC Day 12")
print("==========")

f = open("day12real.txt", "r")
content = f.read()
f.close()

grid = content.split()
ymax = len(grid)
xmax = len(grid[0])
visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

def traverse_positions(grid, c, x, y, subregion):
    if x < 0 or y < 0 or y >= ymax or x >= xmax:
        return []
    
    field = grid[y][x]
    if field != c:
        return []
    
    if visited[y][x] == 1:
        return []
    
    visited[y][x] = 1

    if not (x, y) in subregion:
        subregion.append((x, y))
    
    new_regions = []
    for (xp, yp) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + xp
        ny = y + yp
        new_regions.extend(traverse_positions(grid, c, nx, ny, []))

    subregion.extend(list(filter(lambda x: len(x) > 0, new_regions)))
    return subregion

def find_regions(grid):
    regions = []
    
    for y in range(ymax):
        for x in range(xmax):
            if visited[y][x] == 0:
                c = grid[y][x]
                region = traverse_positions(grid, c, x, y, [])
                regions.append(region)
    
    return regions

def is_same_point(grid, x, y, c):
    if x < 0 or y < 0 or y >= ymax or x >= xmax:
        return False
    return grid[y][x] == c

def count_sides(grid, region):
    # counting sides is basically counting corners
    # what can be a corner (o)
    #  xxx   xxxxx   xxxxx
    #  oxo   xAoxx   xxoAx
    #  xAx   xAAAx   xAAAx
    #  xAx   xxoAx   xAoxx
    #  oxo   xxxxx   xxxxx
    corners = 0
    for (x, y) in region:
        c = grid[y][x]
        if not is_same_point(grid, x - 1, y, c) and not is_same_point(grid, x, y - 1, c):
            corners += 1
        if not is_same_point(grid, x + 1, y, c) and not is_same_point(grid, x, y - 1, c):
            corners += 1
        if not is_same_point(grid, x - 1, y, c) and not is_same_point(grid, x, y + 1, c):
            corners += 1
        if not is_same_point(grid, x + 1, y, c) and not is_same_point(grid, x, y + 1, c):
            corners += 1

        if is_same_point(grid, x - 1, y, c) and is_same_point(grid, x, y + 1, c) and not is_same_point(grid, x - 1, y + 1, c):
            corners += 1
        if is_same_point(grid, x + 1, y, c) and is_same_point(grid, x, y + 1, c) and not is_same_point(grid, x + 1, y + 1, c):
            corners += 1
        if is_same_point(grid, x + 1, y, c) and is_same_point(grid, x, y - 1, c) and not is_same_point(grid, x + 1, y - 1, c):
            corners += 1
        if is_same_point(grid, x - 1, y, c) and is_same_point(grid, x, y - 1, c) and not is_same_point(grid, x - 1, y - 1, c):
            corners += 1

    return corners

def analyze_region(grid, region):
    area = len(region)
    circumference = 0

    for (x, y) in region:
        c = grid[y][x]
        sameneighbors = sum([1 if is_same_point(grid, nx, ny, c) else 0 for (nx, ny) in [(x + xp, y + yp) for (xp, yp) in [(0, 1), (0, -1), (1, 0), (-1, 0)]]])
        circumference += (4 - sameneighbors)

    return area, circumference, count_sides(grid, region)

regions = find_regions(grid)
cost_part1 = 0
cost_part2 = 0
for region in regions:
    ar, ci, sides = analyze_region(grid, region)
    c = grid[region[0][1]][region[0][0]]
    cost_part1 += ar * ci
    cost_part2 += ar * sides
    print("region", c, "plot size", len(region), "area", ar, "circumference", ci, "sides", sides)

print("Fence cost part 1", cost_part1)
print("Fence cost part 2", cost_part2)