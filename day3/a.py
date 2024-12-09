import sys
import re
from operator import mul

f = sys.stdin
text = f.read().strip()
lines = text.splitlines()

def mul(x, y): return x * y

def part1():
    return sum(eval(x) for x in re.findall(r"mul\(\d+,\d+\)", text))

def part2():
    total = 0
    state = True
    
    for x in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", text):
        if x == "don't()":
            state = False
        elif x == "do()":
            state = True
        else:
            if state == False:
                continue
            total += eval(x)
    return total

def part2b():
    state = True
    def do():
        nonlocal state 
        state = True
        return 0
    
    def dont():
        nonlocal state 
        state = False
        return 0
    
    def mul(x, y):
        nonlocal state
        if state == True:
            return x * y
        return 0

    t = text.replace("don\'t", "dont")
    return sum([eval(x) for x in re.findall(r"do\(\)|dont\(\)|mul\(\d+,\d+\)", t)])

print("part 1:", part1())
print("part 2:", part2())
print("part 2b:", part2b())
