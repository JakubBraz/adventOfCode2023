GALAXY = '#'
EMPTY = '.'


def parse_input(inp):
    inp = inp.split('\n')
    galaxies = [(x, y) for x in range(len(inp)) for y in range(len(inp[x])) if inp[x][y] == GALAXY]
    empty_rows = [x for x in range(len(inp)) if all(i == EMPTY for i in inp[x])]
    empty_cols = [x for x in range(len(inp[0])) if all(inp[i][x] == EMPTY for i in range(len(inp)))]
    return galaxies, empty_rows, empty_cols, inp


def dist(p1, p2, empty_rows, empty_cols, multiplier):
    x1, y1 = p1
    x2, y2 = p2
    x = abs(x2 - x1) + multiplier * len([e for e in empty_rows if min(x1, x2) <= e <= max(x1, x2)])
    y = abs(y2 - y1) + multiplier * len([e for e in empty_cols if min(y1, y2) <= e <= max(y1, y2)])
    return x + y


def solve(board, multiplier):
    galaxies, empty_rows, empty_cols, board = board
    dists = [
        dist(galaxies[i], galaxies[j], empty_rows, empty_cols, multiplier)
        for i in range(len(galaxies)) for j in range(i+1, len(galaxies))
    ]
    return sum(dists)


def main():
    inp = day_input()
    inp = parse_input(inp)
    print(solve(inp, 1))
    print(solve(inp, 999_999))


def day_input():
    return """"""
