import math
import re


def parse_input(inp):
    inp = inp.split('\n')
    inp = [re.findall('\d+', row) for row in inp]
    inp = [[int(x) for x in row] for row in inp]
    return list(zip(inp[0], inp[1]))


def parse_input_part2(inp):
    inp = inp.split('\n')
    inp = [re.findall('\d+', row) for row in inp]
    return (int(''.join(inp[0])), int(''.join(inp[1])))


def reach_distance(charging, limit):
    return charging * (limit - charging)


def solve1(inp):
    result = 1
    for time, to_reach in inp:
        counter = [x for x in range(1, time) if reach_distance(x, time) > to_reach]
        result *= len(counter)
    return result


def solve2(inp):
    time, to_reach = inp
    # f(x) = a*x^2 + bx + c
    # delta = b^2 - 4*a*c
    delta = time * time - 4 * to_reach
    x1 = math.ceil((time - math.sqrt(delta)) / 2)
    x2 = math.floor((time + math.sqrt(delta)) / 2)
    return x2 - x1 + 1


def main():
    parsed = parse_input(day_input()), parse_input_part2(day_input())
    print(solve1(parsed[0]))
    print(solve2(parsed[1]))


def day_input():
    return """"""
