print("AOC Day 02")
print("==========")

f = open("day2real.txt", "r")
content = f.read()
f.close()

# print(content)

lines = content.split("\n")

def line_safe(input):
    if len(input) < 2:
        return True
    num = input[0]
    first_diff = input[1] - num
    should_increase = first_diff > 0
    for n in input[1:]:
        diff = num - n
        if diff == 0 or abs(diff) > 3:
            return False
        if should_increase:
            if diff > 0:
                return False
            else:
                num = n
                continue
        else:
            if diff < 0:
                return False
            else:
                num = n
                continue
    return True

def permutate_line(line):
    new_lines = []
    for i in range(0, len(line)):
        line_copy = line[:]
        line_copy.pop(i)
        new_lines.append(line_copy)
    return new_lines

num_safe_p1 = 0
num_safe_p2 = 0
for l in lines:
    number_line = list(map(int, l.split()))
    safe_p1 = line_safe(number_line)
    if safe_p1:
        num_safe_p1 += 1
    permutated_lines = permutate_line(number_line)
    safe_p2 = False
    for pl in permutated_lines:
        if line_safe(pl):
            safe_p2 = True
            break
    if safe_p2:
        num_safe_p2 += 1

print("Part 1, number of safe reports: ", num_safe_p1)
print("Part 2, number of safe reports: ", num_safe_p2)