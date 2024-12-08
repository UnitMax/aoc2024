import itertools

print("AOC Day 07")
print("==========")

f = open("day7real.txt", "r")
content = f.read()
f.close()

lines = content.split('\n')

def get_possible_ops(nr, part2):
    # single or double pipes should be stylistic only and it's easier to handle a single char here
    possible_ops = itertools.product(['*', '+', '|'] if part2 else ['*', '+'], repeat=nr)
    return list(possible_ops)

def apply_ops(ops, input):
    outs = ""
    i = 0
    for nr in input:
        outs += str(nr)
        if i == len(input) - 1:
            break
        outs += ops[i]
        i += 1
    return outs

# cannot use built-in python eval because weird rules
def eval_ops(ops, input):
    if len(ops) == 0 and len(input) == 1:
        return input[0]
    subtotal = input[0]
    i = 0
    for nr in input[1:]:
        op = ops[i]
        if op == '*':
            subtotal *= nr
        elif op == '+':
            subtotal += nr
        elif op == '|':
            subtotal = int(str(subtotal) + str(nr))
        i += 1
    return subtotal

def get_calibration_result(part2):
    calibration_result = 0
    for l in lines:
        part = list(map(lambda x: int(x.replace(":", "")), l.split()))
        result = part[0]
        input = part[1:]
        ops = get_possible_ops(len(input) - 1, part2)
        for op in ops:
            eq = apply_ops(op, input)
            res = eval_ops(op, input)
            if res == result:
                calibration_result += res
                break 
    return calibration_result

print("Part 1, calibration result = ", get_calibration_result(False))
print("Part 2, calibration result = ", get_calibration_result(True))