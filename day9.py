import itertools

print("AOC Day 09")
print("==========")

f = open("day9real.txt", "r")
content = f.read()
f.close()

def rearrange_files(input):
    outl = []
    isfree = False
    fileid = 0
    for c in input:
        num = int(c)
        for i in range(num):
            if isfree:
                outl.append(None)
            else:
                outl.append(fileid)
        if not isfree:
            fileid += 1
        isfree = not isfree
    return outl

def frag(input):
    freectr = 0
    inputctr = len(input) - 1
    while inputctr >= 0 and freectr < len(input):
        if freectr >= inputctr:
            break

        # find free space
        while input[freectr] != None and freectr < inputctr:
            freectr += 1
        if input[freectr] != None:
            break

        # find input
        while input[inputctr] == None and freectr < inputctr:
            inputctr -= 1
        if input[inputctr] == None:
            break

        input[freectr] = input[inputctr]
        input[inputctr] = None
    return input

def rearrange_files_chunks(input):
    outl = []
    isfree = False
    fileid = 0
    for c in input:
        if isfree:
            outl.append({"file": None, "times": int(c)})
        else:
            outl.append({"file": fileid, "times": int(c)})
        if not isfree:
            fileid += 1
        isfree = not isfree
    return outl

def consolidate_spaces(input):
    for i in range(len(input) - 1):
        if input[i]["times"] == 0:
            continue
        if input[i]["file"] == None and input[i+1]["file"] == None:
            input[i]["times"] += input[i+1]["times"]
            input[i+1]["times"] = 0

    return list(filter(lambda x: x["times"] > 0 or x["file"] != None, input))

def printblocks(input):
    outs = ""
    for val in input:
        for i in range(val["times"]):
            if val["file"] == None:
                outs += '.'
            else:
                outs += str(val["file"])
    return outs

def defrag(input):
    freectr = 0

    i = len(input) - 1
    while i >= 0:
        if input[i]["file"] == None:
            i -= 1
            continue

        inputsize = input[i]["times"]

        freectr = 0
        while freectr < len(input) and freectr < i and (input[freectr]["file"] != None or input[freectr]["times"] < inputsize):
            freectr += 1
        if freectr >= len(input) or freectr >= i or input[freectr]["file"] != None or input[freectr]["times"] < inputsize:
            i -= 1
            continue

        freesize = input[freectr]["times"]
        inputsize = input[i]["times"]
        if freesize >= inputsize:
            input[freectr] = {"file": input[i]["file"], "times": inputsize}
            input[i]["file"] = None
            if freesize > inputsize:
                input.insert(freectr + 1, {"file": None, "times": freesize - inputsize})
                if i >= freectr:
                    i += 1
        
        i -= 1
        
        input = consolidate_spaces(input)
        if i >= len(input):
            i = len(input) - 1

    return input

def checksum(inputs):
    input = list(inputs)
    chksm = 0
    for i in range(len(input)):
        if input[i] == None:
            break
        chksm += (i * int(input[i]))
    return chksm

def checksum_chunks(input):
    chksm = 0
    i = 0
    for val in input:
        for t in range(val["times"]):
            f = val["file"]
            if f != None:
                chksm += (i * int(f)) # None is 0 anyway
            i += 1
    return chksm

checksum_1 = checksum(frag(rearrange_files(content)))
checksum_2 = checksum_chunks(defrag(rearrange_files_chunks(content)))

print("Part 1, checksum =", checksum_1)
print("Part 2, checksum =", checksum_2)