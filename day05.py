from functools import reduce


def parse_input(inp):
    inp = inp.split('\n\n')
    inp = [x.split('\n') for x in inp]
    seeds = [int(x) for x in inp[0][0].split()[1:]]
    ranges = [parse_range(x) for x in inp[1:]]
    return seeds, ranges


def parse_range(range_map):
    name = range_map[0][0:-1]
    ranges = [[int(y) for y in x.split()] for x in range_map[1:]]
    return ranges


def map_value(val, ranges, swap_dest_src = False):
    for r in ranges:
        source, dest, size = r if swap_dest_src else (r[1], r[0], r[2])
        if source <= val < source + size:
            return dest + (val - source)
    return val


def solve1(parsed):
    seeds, ranges = parsed
    mapped = [reduce(lambda acc, val: map_value(acc, val), ranges, s) for s in seeds]
    return min(mapped)


def solve2(parsed):
    seeds, ranges = parsed
    ranges = list(reversed(ranges))
    seed_range = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    for i in range(4_000_000_000):
        res = reduce(lambda acc, val: map_value(acc, val, True), ranges, i)
        if any(s[0] <= res < s[0] + s[1] for s in seed_range):
            return i


def main():
    inp = day_input()
    parsed = parse_input(inp)
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return """"""
