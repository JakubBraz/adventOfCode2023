import re

def parse_input(arg):
    res = arg.split('\n')
    res = [parse_lines(line) for line in res]
    return res


def parse_lines(line):
    line = line[line.find(':') + 2:]
    line = find_num(line)
    to_find = 'r'
    colors = {'r': 0, 'g': 1, 'b': 2}
    ind_to_color = ['r', 'g', 'b']
    result = []
    tmp = []
    for i, c in line:
        tup = (to_find, c)
        if to_find == c:
            tmp.extend([i])
            if c == 'b':
                result.append(tmp)
                tmp = []
        elif tup == ('r', 'g'):
            tmp.extend([0, i])
        elif tup == ('r', 'b'):
            tmp.extend([0, 0, i])
            result.append(tmp)
            tmp = []
        elif tup == ('g', 'r'):
            tmp.extend([0, 0])
            result.append(tmp)
            tmp = [i]
        elif tup == ('g', 'b'):
            tmp.extend([0, i])
            result.append(tmp)
            tmp = []
        elif tup == ('b', 'r'):
            tmp.extend([0])
            result.append(tmp)
            tmp = [i]
        elif tup == ('b', 'g'):
            tmp.extend([0])
            result.append(tmp)
            tmp = [0, i]
        to_find = ind_to_color[(colors[c] + 1) % 3]
    if len(tmp) == 0:
        pass
    elif len(tmp) == 1:
        result.append([tmp[0], 0, 0])
    elif len(tmp) == 2:
        result.append([tmp[0], tmp[1], 0])
    else:
        result.append(tmp)
    return result


def find_num(line):
    res = re.findall('\d+ \w', line)
    return [[int(x.split(' ')[0]), x.split(' ')[1]] for x in res]


def max_cubes(games):
    result = []
    for subgame in games:
        m = [0, 0, 0]
        for r, g, b in subgame:
            m = [max(m[0], r), max(m[1], g), max(m[2], b)]
        result.append(m)
    return result


def solve2(games):
    result = max_cubes(games)
    return sum(r * g * b for r, g, b in result)


def solve1(games, limits):
    result = 0
    for game, subgame in enumerate(games):
        if all(colors[0] <= limits[0] and colors[1] <= limits[1] and colors[2] <= limits[2] for colors in subgame):
            result += game + 1
    return result


def main():
    inp = day_input()
    parsed = parse_input(inp)
    print(solve1(parsed, [13, 14, 15]))
    print(solve2(parsed))


def day_input():
    return """"""
