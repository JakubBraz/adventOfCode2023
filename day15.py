from functools import reduce


def parse_input(inp):
    inp = inp.split(',')
    return inp


def hash_fun(acc, val):
    r = acc + ord(val)
    r *= 17
    r %= 256
    return r


def do_hash(s):
    return reduce(hash_fun, s, 0)


def solve1(inp):
    return sum(do_hash(s) for s in inp)


def find_index(arr, val):
    for i, (ind, _) in enumerate(arr):
        if ind == val:
            return i
    return -1


def solve2(inp):
    boxes = [[] for _ in range(256)]
    for lens in inp:
        if '-' in lens:
            ind = lens[:-1]
            h = do_hash(ind)
            i = find_index(boxes[h], ind)
            if i >= 0:
                boxes[h].pop(i)
        else:
            ind, val = lens.split('=')
            h = do_hash(ind)
            i = find_index(boxes[h], ind)
            if i >=0:
                boxes[h][i] = [ind, val]
            else:
                boxes[h].append([ind, val])
    result = 0
    for i, b in enumerate(boxes):
        for slot, (_, val) in enumerate(b):
            result += (i + 1) * (slot + 1) * int(val)
    return result


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return """"""
