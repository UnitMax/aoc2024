print("AOC Day 15")
print("==========")

f = open("day15real.txt", "r")
content = f.read()
f.close()

map_s = content.split("\n\n")[0]
movement_s = content.split("\n\n")[1]
movement_s = movement_s.replace("\n", "")

grid = [[c for c in s] for s in map_s.split("\n")]
maxy = len(grid)
maxx = len(grid[0])
initial_pos = (0, 0)

for y in range(maxy):
    for x in range(maxx):
        if grid[y][x] == '@':
            initial_pos = (x, y)
            break

def move(grid, mov, xpos, ypos):
    pos = (xpos, ypos)
    match mov:
        case '^':
            y = ypos - 1
            if grid[y][xpos] == '.':
                grid[ypos][xpos] = '.'
                grid[y][xpos] = '@' # new position
                pos = (xpos, y)
            elif grid[y][xpos] == '#':
                pass # dont do anything
            elif grid[y][xpos] == 'O':
                for yn in range(y - 1, -1, -1):
                    if grid[yn][xpos] == '.':
                        pos = (xpos, y)
                        last = grid[ypos][xpos]
                        for ymove in range(y, yn - 1, -1):
                            tmp = grid[ymove][xpos]
                            grid[ymove][xpos] = last
                            last = tmp
                        grid[ypos][xpos] = '.'
                        break
                    elif grid[yn][xpos] == '#':
                        break
            else:
                raise Exception("This should not happen")
        case '>':
            x = xpos + 1
            if grid[ypos][x] == '.':
                grid[ypos][xpos] = '.'
                grid[ypos][x] = '@' # new position
                pos = (x, ypos)
            elif grid[ypos][x] == '#':
                pass # dont do anything
            elif grid[ypos][x] == 'O':
                for xn in range(x + 1, maxx, 1):
                    if grid[ypos][xn] == '.':
                        pos = (x, ypos)
                        last = grid[ypos][xpos]
                        for xmove in range(x, xn + 1, 1):
                            tmp = grid[ypos][xmove]
                            grid[ypos][xmove] = last
                            last = tmp
                        grid[ypos][xpos] = '.'
                        break
                    elif grid[ypos][xn] == '#':
                        break
            else:
                raise Exception("This should not happen")
        case '<':
            x = xpos - 1
            if grid[ypos][x] == '.':
                grid[ypos][xpos] = '.'
                grid[ypos][x] = '@' # new position
                pos = (x, ypos)
            elif grid[ypos][x] == '#':
                pass # dont do anything
            elif grid[ypos][x] == 'O':
                for xn in range(x - 1, -1, -1):
                    if grid[ypos][xn] == '.':
                        pos = (x, ypos)
                        last = grid[ypos][xpos]
                        for xmove in range(x, xn - 1, -1):
                            tmp = grid[ypos][xmove]
                            grid[ypos][xmove] = last
                            last = tmp
                        grid[ypos][xpos] = '.'
                        break
                    elif grid[ypos][xn] == '#':
                        break
            else:
                raise Exception("This should not happen")
        case 'v':
            y = ypos + 1
            if grid[y][xpos] == '.':
                grid[ypos][xpos] = '.'
                grid[y][xpos] = '@' # new position
                pos = (xpos, y)
            elif grid[y][xpos] == '#':
                pass # dont do anything
            elif grid[y][xpos] == 'O':
                for yn in range(y + 1, maxy, 1):
                    if grid[yn][xpos] == '.':
                        pos = (xpos, y)
                        last = grid[ypos][xpos]
                        for ymove in range(y, yn + 1, 1):
                            tmp = grid[ymove][xpos]
                            grid[ymove][xpos] = last
                            last = tmp
                        grid[ypos][xpos] = '.'
                        break
                    elif grid[yn][xpos] == '#':
                        break
            else:
                raise Exception("This should not happen", grid[y][xpos])
    return pos

def calc_gps(grid):
    score = 0
    for y in range(maxy):
        for x in range(maxx):
            if grid[y][x] == 'O':
                score += (x + 100 * y)
    return score

def print_grid(grid):
    for line in grid:
        for c in line:
            print(c, end='')
        print("")

pos = initial_pos
for mov in movement_s:
    pos = move(grid, mov, pos[0], pos[1])

print("Part 1, GPS score =", calc_gps(grid))