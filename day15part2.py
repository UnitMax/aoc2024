import sys

print("AOC Day 15 Part2")
print("==========")

f = open("day15real.txt", "r")
content = f.read()
f.close()

map_s = content.split("\n\n")[0]
movement_s = content.split("\n\n")[1]
movement_s = movement_s.replace("\n", "")

grid = []
for s in map_s.split("\n"):
    l = []
    for c in s:
        match c:
            case '#':
                l.append('#')
                l.append('#')
            case '.':
                l.append('.')
                l.append('.')
            case 'O':
                l.append('[')
                l.append(']')
            case '@':
                l.append('@')
                l.append('.')
    grid.append(l)

maxy = len(grid)
maxx = len(grid[0])
initial_pos = (0, 0)

for y in range(maxy):
    for x in range(maxx):
        if grid[y][x] == '@':
            initial_pos = (x, y)
            break

def calc_gps(grid):
    score = 0
    for y in range(maxy):
        for x in range(maxx):
            if grid[y][x] == '[':
                score += (x + 100 * y)
    return score

def print_grid(grid, flush=True):
    l = 1
    for line in grid:
        l += 1
        for c in line:
            print(c, end='')
        print("")
    if flush:
        sys.stdout.write("\033[F" * l)
        sys.stdout.flush()

def check_box_move(boxes, c, compare, x, y):
    if c == compare and (x, y) not in boxes:
        boxes.append((x, y))

def move_boxes(grid, boxes: list, mov):
    canmove = True
    boxes_to_move = []
    while canmove and len(boxes) > 0:
        x, y = boxes.pop(0)
        match mov:
            case '^':
                x1, y1 = x, y - 1
                x2, y2 = x + 1, y - 1
                c1 = grid[y1][x1]
                c2 = grid[y2][x2]
                if c1 == '#' or c2 == '#':
                    canmove = False
                    break
                check_box_move(boxes, c1, '[', x1, y1)
                check_box_move(boxes, c1, ']', x1 - 1, y1)
                check_box_move(boxes, c2, '[', x2, y2)
                check_box_move(boxes, c2, ']', x2 - 1, y2)
                if (x, y) not in boxes_to_move:
                    boxes_to_move.append((x, y))
            case 'v':
                x1, y1 = x, y + 1
                x2, y2 = x + 1, y + 1
                c1 = grid[y1][x1]
                c2 = grid[y2][x2]
                if c1 == '#' or c2 == '#':
                    canmove = False
                    break
                check_box_move(boxes, c1, '[', x1, y1)
                check_box_move(boxes, c1, ']', x1 - 1, y1)
                check_box_move(boxes, c2, '[', x2, y2)
                check_box_move(boxes, c2, ']', x2 - 1, y2)
                if (x, y) not in boxes_to_move:
                    boxes_to_move.append((x, y))
            case '>':
                # box is 2 wide, hence we're moving 2
                x1, y1 = x + 2, y
                c1 = grid[y1][x1]
                if c1 == '#':
                    canmove = False
                    break
                # we shouldn't need to verify the other side of the box because 
                # the initial input is correctly formatted and so should be all
                # subsequent transformations
                check_box_move(boxes, c1, '[', x1, y1)
                if (x, y) not in boxes_to_move:
                    boxes_to_move.append((x, y))
            case '<':
                if grid[y][x - 1] == '#':
                    canmove = False
                    break
                x1, y1 = x - 2, y
                c1 = grid[y1][x1]
                # if c1 == '#':
                #     canmove = False
                #     break
                check_box_move(boxes, c1, '[', x1, y1)
                if (x, y) not in boxes_to_move:
                    boxes_to_move.append((x, y))

    if canmove:
        # just fill everything up with .'s
        # the robot's @ will be placed at the end
        while len(boxes_to_move) > 0:
            x, y = boxes_to_move.pop()
            match mov:
                case '^':
                    grid[y - 1][x] = '['
                    grid[y - 1][x + 1] = ']'
                    grid[y][x] = '.'
                    grid[y][x + 1] = '.'
                case 'v':
                    grid[y + 1][x] = '['
                    grid[y + 1][x + 1] = ']'
                    grid[y][x] = '.'
                    grid[y][x + 1] = '.'
                case '>':
                    grid[y][x] = '.'
                    grid[y][x + 1] = '['
                    grid[y][x + 2] = ']'
                case '<':
                    grid[y][x] = ']'
                    grid[y][x - 1] = '['
                    grid[y][x + 1] = '.'

    return canmove

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
            elif grid[y][xpos] == '[':
                if move_boxes(grid, [(xpos, y)], mov):
                    grid[y][xpos] = '@' # new position
                    grid[ypos][xpos] = '.'
                    pos = (xpos, y)
            elif grid[y][xpos] == ']':
                if move_boxes(grid, [(xpos - 1, y)], mov):
                    grid[y][xpos] = '@' # new position
                    grid[ypos][xpos] = '.'
                    pos = (xpos, y)
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
            elif grid[y][xpos] == '[':
                if move_boxes(grid, [(xpos, y)], mov):
                    grid[y][xpos] = '@' # new position
                    grid[ypos][xpos] = '.'
                    pos = (xpos, y)
            elif grid[y][xpos] == ']':
                if move_boxes(grid, [(xpos - 1, y)], mov):
                    grid[y][xpos] = '@' # new position
                    grid[ypos][xpos] = '.'
                    pos = (xpos, y)
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
            elif grid[ypos][x] == '[':
                if move_boxes(grid, [(x, ypos)], mov):
                    grid[ypos][x] = '@' # new position
                    grid[ypos][xpos] = '.'
                    pos = (x, ypos)
            elif grid[ypos][x] == ']':
                raise Exception("This should not happen either")
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
            elif grid[ypos][x] == ']':
                if move_boxes(grid, [(x - 1, ypos)], mov):
                    grid[ypos][xpos] = '.'
                    grid[ypos][x] = '@' # new position
                    pos = (x, ypos)
            elif grid[ypos][x] == '[':
                raise Exception("This should not happen either")
            else:
                raise Exception("This should not happen", grid[ypos][x])
    return pos

pos = initial_pos
for mov in movement_s:
    pos = move(grid, mov, pos[0], pos[1])

print_grid(grid, False)
print("Part 2, GPS score =", calc_gps(grid))