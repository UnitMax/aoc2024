import itertools

print("AOC Day 09")
print("==========")

f = open("day9test.txt", "r")
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
            outl.append({"file": None, "times": int(c), "moved": False})
        else:
            outl.append({"file": fileid, "times": int(c), "moved": False})
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
    # inputctr = len(input) - 1

    i = len(input) - 1
    # for i in reversed(range(len(input))):
    while i >= 0:
        if input[i]["file"] == None:
            i -= 1
            continue

        inputsize = input[i]["times"]

        freectr = 0
        while freectr < len(input) and freectr < i and (input[freectr]["file"] != None or input[freectr]["times"] < inputsize): # and freectr < inputctr:
            freectr += 1
        if freectr >= len(input) or freectr >= i or input[freectr]["file"] != None or input[freectr]["times"] < inputsize:
            i -= 1
            continue

        # print("Free idx", freectr, input[freectr], "Input idx", i, input[i])

        # 1, 2, 3, 4
        #       ^2
        # 1, 2, 2, 3, 4
        #       ^2

        freesize = input[freectr]["times"]
        inputsize = input[i]["times"]
        if freesize >= inputsize:
            # TODO: fill possible remaining space
            input[freectr] = {"file": input[i]["file"], "times": inputsize, "moved": True}
            input[i]["file"] = None
            if freesize > inputsize:
                input.insert(freectr + 1, {"file": None, "times": freesize - inputsize, "moved": False})
                if i >= freectr:
                    i += 1
                # freectr += 1
        else:
            input[i]["moved"] = True # this counts
            # inputctr -= 1
        
        i -= 1
        
        input = consolidate_spaces(input)
        # print(input)
        # print(printblocks(input))
        # print("---")

    # while inputctr >= 0 and freectr < len(input):
    #     # if freectr >= inputctr:
    #     #     break

    #     # find free space
    #     while input[freectr]["file"] != None: # and freectr < inputctr:
    #         freectr += 1
    #     if input[freectr]["file"] != None or freectr >= len(input):
    #         break

    #     inputctr = len(input) - 1
    #     # find input
    #     while inputctr >= 0 and (input[inputctr]["file"] == None or input[inputctr]["moved"] == True): # and freectr < inputctr:
    #         inputctr -= 1
    #     if inputctr < 0 or input[inputctr]["file"] == None or input[inputctr]["moved"] == True:
    #         break

    #     print("Free idx", freectr, input[freectr], "Input idx", inputctr, input[inputctr])

    #     freesize = input[freectr]["times"]
    #     inputsize = input[inputctr]["times"]
    #     if freesize >= inputsize:
    #         # TODO: fill possible remaining space
    #         input[freectr] = {"file": input[inputctr]["file"], "times": inputsize, "moved": True}
    #         input[inputctr]["file"] = None
    #         if freesize > inputsize:
    #             input.insert(freectr + 1, {"file": None, "times": freesize - inputsize, "moved": False})
    #             # freectr += 1

    #         freectr += 1
    #     else:
    #         input[inputctr]["moved"] = True # this counts
    #         inputctr -= 1
        
    #     input = consolidate_spaces(input)
    #     print(input)
    #     print("---")

        

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



print("====")

checksum_1 = checksum(frag(rearrange_files(content)))

print("Part 1, checksum =", checksum_1)

# print(content)
c2 = defrag(rearrange_files_chunks(content))

print("++++++")
print(printblocks(c2))
print("++++++")
print(checksum_chunks(c2))