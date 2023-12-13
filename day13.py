def parse_input(inp):
    inp = inp.split('\n\n')
    inp = [[[x for x in c] for c in line.split('\n')] for line in inp]
    return inp


def find_reflection_cols(pattern, prev = 0):
    for i in range(1, len(pattern[0])):
        if all(list(reversed(line[:i]))[:len(line) - i] == line[i:2*i] for line in pattern) and i != prev:
            return i
    return 0


def find_reflection_rows(pattern, prev = 0):
    for i in range(1, len(pattern)):
        if list(reversed(pattern[:i]))[:len(pattern) - i] == pattern[i:2*i] and i != prev:
            return i
    return 0


def find_smudge(p):
    init_p = [[c for c in line] for line in p]
    replace = -1
    cr = (find_reflection_cols(p), find_reflection_rows(p))
    while True:
        p = [[c for c in line] for line in init_p]
        replace += 1
        i, j = replace // len(p[0]), replace % len(p[0])
        p[i][j] = '.' if p[i][j] == '#' else '#'
        new_cr = (find_reflection_cols(p, cr[0]), find_reflection_rows(p, cr[1]))
        if new_cr != (0, 0) and cr != new_cr:
            return new_cr


def solve1(inp):
    cr = [(find_reflection_cols(p), find_reflection_rows(p)) for p in inp]
    return sum(c + 100 * r for c, r in cr)


def solve2(inp):
    cr = [find_smudge(p) for p in inp]
    cr = [(c, r) if r == 0 else (0,  r) for c, r in cr]
    return sum(c + 100 * r for c, r in cr)


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return """"""
