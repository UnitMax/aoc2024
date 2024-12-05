import math

print("AOC Day 05")
print("==========")

f = open("day5real.txt", "r")
content = f.read()
f.close()

parts = content.split("\n\n")

rules_string = parts[0]
prints_string = parts[1]

rule_dict = {}
for rule_string in rules_string.split("\n"):
    rule = rule_string.split("|")
    num1 = int(rule[0])
    num2 = int(rule[1])
    if not num1 in rule_dict:
        rule_dict[num1] = [num2]
    else:
        rule_dict[num1].append(num2)

def is_before(x, y):
    return x in rule_dict and y in rule_dict[x]

def get_center(num_list):
    return num_list[math.floor(len(num_list) / 2)]

def fix_line(nums):
    indices = [sum([rule_dict[num].count(x) if num in rule_dict else 0 for x in nums]) for num in nums]
    sorted_indices = sorted(range(len(indices)), key=lambda i: indices[i])
    fixed_line = [nums[i] for i in sorted_indices]
    fixed_line.reverse()
    return fixed_line

middle_sum = 0
correct_middle_sum = 0

for print_s in prints_string.split():
    line_valid = True
    nums = list(map(int, print_s.split(",")))
    for i in range(0, len(nums)):
        num = nums[i]
        for j in range(i + 1, len(nums)):
            num_compare = nums[j]
            res = is_before(num, num_compare)
            if not res:
                line_valid = False
                break
    if line_valid:
        middle_sum += get_center(nums)
    else:
        correct_middle_sum += get_center(fix_line(nums))

print("Part 1, middle sum = ", middle_sum)
print("Part 2, correct middle sum = ", correct_middle_sum)