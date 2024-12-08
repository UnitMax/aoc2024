import itertools

print("AOC Day 08")
print("==========")

f = open("day8real.txt", "r")
content = f.read()
f.close()

grid = content.split()
positions = {}

def is_valid_pos(grid, x, y):
    return x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0])

def get_antinode_locations(grid, pos1, pos2, part2=False):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    xdiff = x1 - x2
    ydiff = y1 - y2
    antinode_locs = []
    orig_pos = [(x1, y1), (x2, y2)]
    if part2:
        for (x, y) in orig_pos:
            newx = x + xdiff
            newy = y + ydiff
            while is_valid_pos(grid, newx, newy):
                antinode_locs.append((newx, newy))
                newx += xdiff
                newy += ydiff
            newx = x - xdiff
            newy = y - ydiff
            while is_valid_pos(grid, newx, newy):
                antinode_locs.append((newx, newy))
                newx -= xdiff
                newy -= ydiff
    else:
        for (x, y) in orig_pos:
            if (x+xdiff, y+ydiff) not in orig_pos and is_valid_pos(grid, x+xdiff, y+ydiff):
                antinode_locs.append((x+xdiff,y+ydiff))
            if (x-xdiff, y-ydiff) not in orig_pos and is_valid_pos(grid, x-xdiff, y-ydiff):
                antinode_locs.append((x-xdiff,y-ydiff))
    return antinode_locs

for y in range(len(grid)):
    for x in range(len(grid[0])):
        c = grid[y][x]
        if c != '.':
            if c not in positions:
                positions[c] = [(x, y)]
            else:
                positions[c].append((x, y))

def get_all_antinode_positions(grid, positions, part2):
    all_antinode_positions = []
    for node, locs in positions.items():
        combs = list(itertools.combinations(locs, r=2))
        for comb in combs:
            antinode_pos = get_antinode_locations(grid, comb[0], comb[1], part2)
            all_antinode_positions.extend(antinode_pos)
    return all_antinode_positions

# remove dupes
all_antinode_positions_1 = list(set(get_all_antinode_positions(grid, positions, False)))
all_antinode_positions_2 = list(set(get_all_antinode_positions(grid, positions, True)))

print("===")
print("Part 1, unique antinode positions = ", len(all_antinode_positions_1))
print("Part 2, unique antinode positions = ", len(all_antinode_positions_2))