from collections import defaultdict


def get_neighbours(x, y, max_x, max_y):
    return [(x + i, y + j)
            for i in range(-1, 2)
            for j in range(-1, 2)
            if 0 <= x + i < max_x and 0 <= y + j < max_y and (i, j) != (0, 0)]


def get_adjacent_nums(inp, indices):
    res = defaultdict(lambda: set())
    for i, j in indices:
        neigh = get_neighbours(i, j, len(inp), len(inp[i]))
        digits = (xy for xy in neigh if inp[xy[0]][xy[1]].isdigit())
        res[(i,j)].update(digits)
    return res


def iterate_row(x, y, row):
    i = y
    ys = set()
    while i >= 0 and row[i].isdigit():
        ys.add((x, i))
        i -= 1
    i = y
    while i < len(row) and row[i].isdigit():
        ys.add((x, i))
        i += 1
    return sorted(ys)


def nums_per_symbol(nums, inp):
    result = []
    xy = set(nums)
    while xy:
        x, y = xy.pop()
        coords = iterate_row(x, y, inp[x])
        xy = xy - set(coords)
        left = coords[0][-1]
        right = coords[-1][-1]
        i = coords[0][0]
        result.append((int(inp[i][left:right + 1])))
    return result


def build_nums(nums: dict, inp):
    return {k: nums_per_symbol(v, inp) for k, v in nums.items()}


def solve2(inp):
    stars = [(i, j) for i in range(len(inp)) for j in range(len(inp[i])) if inp[i][j] == '*']
    res = get_adjacent_nums(inp, stars)
    res = build_nums(res, inp)
    res = [v for _k, v in res.items() if len(v) == 2]
    return sum(x * y for x, y in res)


def solve1(inp):
    res = get_adjacent_nums(inp, [(i, j) for i in range(len(inp)) for j in range(len(inp[i])) if
                                  not inp[i][j].isdigit() and inp[i][j] != '.'])
    res = [sum(n) for n in build_nums(res, inp).values()]
    return sum(res)


def main():
    inp = day_input()
    inp = inp.split('\n')
    print(solve1(inp))
    print(solve2(inp))


def day_input():
    return """"""
