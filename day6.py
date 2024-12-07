import math

print("AOC Day 06")
print("==========")

f = open("day6test.txt", "r")
content = f.read()
f.close()

grid = []
visited = []

lines = content.split()

sx = 0
sy = 0
sdx = 0
sdy = 0

cy = 0
for l in lines:
    line = []
    visited_line = []
    cx = 0
    for char in l:
        if char == '^':
            sx = cx
            sy = cy
            sdx = 0
            sdy = -1
            line.append('.')
            visited_line.append(1)
        elif char == '>':
            sx = cx
            sy = cy
            sdx = 1
            sdy = 0
            line.append('.')
            visited_line.append(1)
        elif char == '<':
            sx = cx
            sy = cy
            sdx = -1
            sdy = 0
            line.append('.')
            visited_line.append(1)
        elif char == 'v':
            sx = cx
            sy = cy
            sdx = 0
            sdy = 1
            line.append('.')
            visited_line.append(1)
        else:
            line.append(char)
            visited_line.append(0)
        cx += 1
    grid.append(line)
    visited.append(visited_line)
    cy += 1

def traverse(grid, maxx, maxy, sx, sy, dx, dy, subtotal):
    nx = sx + dx
    ny = sy + dy
    if nx >= maxx or ny >= maxy or nx < 0 or ny < 0:
        return subtotal
    c = grid[ny][nx]
    v = visited[ny][nx]
    addv = 1 if v == 0 else 0
    if c == '.':
        visited[ny][nx] = 1
        return traverse(grid, maxx, maxy, nx, ny, dx, dy, subtotal + addv)
    elif c == '#':
        visited[ny][nx] = 1 
        ndx = 0
        ndy = 1
        if dx == 1: # right
            # now down
            ndx = 0
            ndy = 1
        elif dy == 1: # down
            # now left
            ndx = -1
            ndy = 0
        elif dx == -1: # left
            # now up
            ndx = 0
            ndy = -1
        elif dy == -1: # up
            # now right
            ndx = 1
            ndy = 0
        else:
            raise Exception("Again, what is happening here?")
        
        return traverse(grid, maxx, maxy, sx + ndx, sy + ndy, ndx, ndy, subtotal + addv)
    else:
        raise Exception("this should not happen")

print(sx, sy, sdx, sdy)

dist_pos = traverse(grid, len(grid[0]), len(grid), sx, sy, sdx, sdy, 0)

for vp in visited:
    for vpi in vp:
        print(vpi, end='')
    print("")

print(grid)
print("===")
print("Part 1, distinct positions = ", dist_pos)