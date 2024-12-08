import copy
import multiprocessing

def initialize_visited_dirs(grid, sx, sy, sdx, sdy):
    vd = []
    for y in range(len(grid)):
        vdl = []
        for x in range(len(grid[0])):
            if x == sx and y == sy:
                vdl.append([(sdx, sdy)])
            else:
                vdl.append([])
        vd.append(vdl)
    return vd

def find_loop(grid, maxx, maxy, sx, sy, dx, dy):
    vd = initialize_visited_dirs(grid, sx, sy, dx, dy)

    nx = sx
    ny = sy
    i = 0
    while not (nx >= maxx or ny >= maxy or nx < 0 or ny < 0):
        c = grid[ny][nx]
        v = vd[ny][nx]

        if c == '.':
            if (dx, dy) not in v:
                v.append((dx, dy))
            elif i > 0:
                return True
        elif c == '#':
            nx -= dx
            ny -= dy
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
                raise Exception("this can never happen")
            
            dx = ndx
            dy = ndy
        else:
            raise Exception("this can never happen")
        
        nx += dx
        ny += dy
        i += 1
    return False

def search_obstacles(t, grid, start, end, sx, sy, sdx, sdy):
    nr_obst = 0
    for y in range(start, end):
        for x in range(len(grid[0])):
            if grid[y][x] != '#' and (x != sx or y != sy):
                new_grid = copy.deepcopy(grid)
                new_grid[y][x] = '#'
                if find_loop(new_grid, len(new_grid[0]), len(new_grid), sx, sy, sdx, sdy):
                    nr_obst += 1
                else:
                    pass
    print("Thread", t, "finished with", nr_obst, "obstacles")
    return nr_obst

if __name__ == '__main__':
    print("AOC Day 06")
    print("==========")

    f = open("day6real.txt", "r")
    content = f.read()
    f.close()

    grid = []
    lines = content.split()

    sx = 0
    sy = 0
    sdx = 0
    sdy = 0

    cy = 0
    for l in lines:
        line = []
        cx = 0
        for char in l:
            if char == '^':
                sx = cx
                sy = cy
                sdx = 0
                sdy = -1
                line.append('.')
            elif char == '>':
                sx = cx
                sy = cy
                sdx = 1
                sdy = 0
                line.append('.')
            elif char == '<':
                sx = cx
                sy = cy
                sdx = -1
                sdy = 0
                line.append('.')
            elif char == 'v':
                sx = cx
                sy = cy
                sdx = 0
                sdy = 1
                line.append('.')
            else:
                line.append(char)
            cx += 1
        grid.append(line)
        cy += 1

    print(sx, sy, sdx, sdy)
    print("===")

    lg = len(grid)
    ts = []
    arguments = []
    NUM_THREADS = 12

    for i in range(NUM_THREADS):
        start = i * (lg // NUM_THREADS)
        end = (i + 1) * (lg // NUM_THREADS)
        if i == NUM_THREADS - 1:
            end = lg
        print("Start thread", i + 1, "start", start, "end", end)
        arguments.append((i + 1, grid, start, end, sx, sy, sdx, sdy))

    with multiprocessing.Pool(NUM_THREADS) as pool:
        results = pool.starmap(search_obstacles, arguments)
    
    print("Part 2, number of obstacles = ", results, sum(results))