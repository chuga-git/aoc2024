import sys
import itertools
import re
import operator
from functools import reduce

def lmap(func, *iterables) -> list:
    return list(map(func, *iterables))

def ints(s: str) -> list[int]:
    return lmap(int, re.findall(r"-?\d+", s))

def concat(a, b):
    return int(str(a) + str(b))

lines = f.read().strip().splitlines()
nums = lmap(ints, lines)
    
# i'm really disappointed this didn't work. damn you, left-to-right evaluation!
# q = list(roundrobin(ns, p))
# print(eval(reduce(operator.add, q, "")))

def part1():
    total = 0
    for n, *rest in nums:
        perms = itertools.product([operator.add, operator.mul], repeat=len(rest)-1)
        ns = lmap(str, rest)
        for p in perms:
            P = iter(p)
            s = rest[0]
            for t in rest[1:]:
                s = next(P)(s, t)
            if s == n:
                total += s
                break
    return total

def part2():
    total = 0
    for n, *rest in nums:
        perms = itertools.product([operator.add, operator.mul, concat], repeat=len(rest)-1)
        ns = lmap(str, rest)
        for p in perms:
            P = iter(p)
            s = rest[0]
            for t in rest[1:]:
                s = next(P)(s, t)
            if s == n:
                total += s
                break
    return total

print("part 1:", part1())
print("part 2:", part2())
