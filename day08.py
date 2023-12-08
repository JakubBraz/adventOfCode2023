import re
from functools import reduce


def parse_input(inp):
    inp = inp.split('\n')
    instr = inp[0]
    inp = inp[2:]
    inp = [re.findall(r"\w+", line) for line in inp]
    inp = {x[0]: {"L": x[1], "R": x[2]} for x in inp}
    return instr, inp


def solve(inp, start, terminate_f):
    instr, step_map = inp
    i = 0
    curr_instr = instr
    current = start
    while terminate_f(current):
        if not curr_instr:
            curr_instr = instr
        step = curr_instr[0]
        curr_instr = curr_instr[1:]
        current = step_map[current][step]
        i += 1
    return i


def gcd(a, b):
    while True:
        if a == 0:
            return b
        a, b = b % a, a


def solve2(inp):
    instr, step_map = inp
    currents = [x for x in step_map if x[-1] == "A"]
    to_finish = [solve(inp, x, lambda x: x[-1] != 'Z') for x in currents]
    return reduce(lambda acc, val: (acc * val) // gcd(acc, val), to_finish[1:], to_finish[0])


def main():
    inp = parse_input(day_input())
    print(solve(inp, "AAA", lambda x: x != "ZZZ"))
    print(solve2(inp))


def day_input():
    return """"""
