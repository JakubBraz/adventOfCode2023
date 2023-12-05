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
    # inp = day_input_test()
    parsed = parse_input(inp)
    print(solve1(parsed, [13, 14, 15]))
    print(solve2(parsed))


def day_input():
    return """Game 1: 4 blue; 1 green, 2 red; 4 blue, 1 green, 6 red
Game 2: 7 red, 1 green, 4 blue; 13 red, 11 blue; 6 red, 2 blue; 9 blue, 9 red; 4 blue, 11 red; 15 red, 1 green, 3 blue
Game 3: 1 blue, 10 green; 4 green, 8 blue; 3 blue, 14 green, 1 red
Game 4: 1 green, 2 blue; 1 blue, 4 green; 8 red, 3 blue, 3 green; 8 red, 2 green, 1 blue; 7 green, 3 blue, 2 red; 1 red, 1 green, 3 blue
Game 5: 3 red, 7 blue, 4 green; 12 blue, 16 red, 4 green; 9 red, 2 green; 1 blue, 1 green, 1 red
Game 6: 15 blue; 15 red, 14 blue, 2 green; 8 red, 2 blue, 2 green; 2 green, 11 blue, 1 red
Game 7: 6 green, 6 red, 2 blue; 1 blue, 2 red, 7 green; 12 red; 5 green, 3 red, 1 blue; 16 red, 10 green
Game 8: 2 green, 10 red, 3 blue; 1 blue, 5 green, 11 red; 6 red, 1 blue, 2 green; 11 red; 4 red, 1 blue, 5 green; 5 green, 3 blue
Game 9: 5 blue, 11 red; 2 blue, 2 green; 11 red, 2 green
Game 10: 3 red, 5 green; 3 blue, 5 green; 3 red, 2 blue, 14 green
Game 11: 1 green, 1 blue, 6 red; 2 blue, 7 red, 2 green; 2 green, 2 red, 3 blue; 10 red; 2 red, 2 blue; 11 red, 3 blue
Game 12: 6 blue, 8 red, 6 green; 15 green, 4 red; 1 red, 10 green, 1 blue; 1 red, 3 blue, 11 green
Game 13: 2 blue, 6 red; 15 red, 6 blue; 20 blue, 10 red, 3 green; 17 blue, 1 red, 4 green
Game 14: 3 green, 7 blue, 7 red; 2 blue; 7 blue, 10 red
Game 15: 3 green, 7 blue; 9 green, 8 blue, 5 red; 6 green, 13 red; 14 red, 2 green, 15 blue; 15 red, 7 green
Game 16: 13 blue; 6 green, 4 blue, 11 red; 15 red, 2 green, 6 blue; 1 green, 13 red, 8 blue; 8 green, 7 blue, 14 red
Game 17: 3 red; 17 red, 4 green; 1 blue, 11 red; 3 blue, 20 red, 3 green
Game 18: 4 red, 2 blue, 3 green; 9 red, 6 green; 11 red, 1 blue
Game 19: 1 green, 4 blue; 1 green, 2 red; 2 blue, 1 green; 4 red, 2 blue
Game 20: 15 blue, 6 green, 6 red; 13 green, 1 blue, 1 red; 13 green, 13 blue, 5 red; 7 red, 16 green, 4 blue
Game 21: 10 blue, 5 green, 8 red; 6 blue, 12 red, 4 green; 2 green, 16 blue, 3 red; 6 red, 12 blue, 3 green; 1 red, 3 green; 7 blue, 6 green, 7 red
Game 22: 3 blue, 3 green, 17 red; 1 green, 18 red; 3 green, 10 red, 5 blue; 2 green, 2 red, 4 blue; 2 blue, 13 red; 1 green, 3 blue, 9 red
Game 23: 4 green, 16 red, 2 blue; 10 red, 10 green, 7 blue; 2 green, 6 red, 13 blue; 1 green, 13 blue, 16 red; 7 green, 16 blue, 9 red
Game 24: 6 blue, 7 red, 4 green; 6 blue, 2 green; 2 green, 6 blue, 2 red; 5 red, 3 green, 11 blue
Game 25: 4 red, 2 green; 1 green; 4 green, 4 blue, 8 red; 5 red, 1 blue
Game 26: 9 red, 4 blue, 13 green; 3 blue, 10 red, 7 green; 13 blue, 5 green, 9 red
Game 27: 1 green, 12 red, 2 blue; 2 blue, 13 red, 2 green; 2 blue, 7 red; 4 green, 9 red, 2 blue; 1 blue, 2 green, 15 red; 3 red, 4 green, 1 blue
Game 28: 1 red, 9 blue, 17 green; 14 green, 15 blue, 2 red; 4 red, 18 green, 13 blue
Game 29: 16 green, 5 blue, 1 red; 6 green, 6 red, 16 blue; 4 red, 9 green, 12 blue; 5 green, 14 blue, 1 red
Game 30: 3 red, 2 blue, 12 green; 13 green, 4 red; 13 green, 2 red, 1 blue; 2 blue, 6 red, 4 green; 3 blue, 13 green, 5 red
Game 31: 3 red; 6 red, 2 green; 5 red; 3 green, 2 red; 1 green, 2 red, 1 blue; 1 blue, 6 red
Game 32: 1 red, 7 green; 9 green, 5 blue; 1 green, 2 red; 4 blue, 2 red, 1 green; 4 blue, 1 green, 3 red
Game 33: 11 green; 12 blue, 2 green; 5 green, 1 blue; 10 green, 3 blue; 4 blue, 1 red, 4 green; 4 green, 5 blue
Game 34: 4 red, 8 blue, 2 green; 8 green, 4 red, 14 blue; 11 green, 6 red, 8 blue; 16 green, 3 blue, 5 red; 3 blue, 3 red, 13 green
Game 35: 7 green, 12 red, 1 blue; 1 red; 13 red; 14 red, 2 blue, 9 green
Game 36: 3 red, 4 green, 1 blue; 3 red, 4 blue; 6 red, 4 blue, 3 green; 3 green, 4 blue, 3 red; 2 blue, 4 green, 7 red
Game 37: 2 green, 1 blue, 5 red; 1 green; 3 blue; 3 blue, 1 green
Game 38: 1 red, 12 blue, 17 green; 4 blue, 2 red, 8 green; 7 blue, 20 green; 6 red, 3 blue; 6 green, 7 red, 6 blue; 10 green, 3 red
Game 39: 3 green, 3 blue, 2 red; 4 blue, 4 red, 4 green; 4 blue, 4 red; 1 blue, 5 green, 2 red; 5 green, 3 blue, 4 red; 4 green, 2 blue
Game 40: 18 green, 1 red; 17 green, 1 blue; 2 green, 1 blue, 1 red; 9 green, 1 blue; 3 green, 1 red; 1 red, 10 green
Game 41: 2 red, 4 blue, 3 green; 8 blue, 2 red; 5 blue; 2 green, 2 red, 3 blue; 1 green, 7 blue
Game 42: 1 green, 2 blue; 9 green, 2 blue, 15 red; 1 green, 4 blue, 9 red
Game 43: 5 blue, 3 red; 2 blue, 8 red, 7 green; 17 red, 4 blue, 7 green
Game 44: 13 red, 3 green, 12 blue; 15 green, 10 blue; 8 green, 11 red, 2 blue; 10 blue, 16 red, 2 green; 12 blue, 5 green, 5 red; 14 green, 8 red, 13 blue
Game 45: 1 red, 3 green; 4 green, 5 blue, 2 red; 6 red, 2 blue, 6 green; 3 blue, 2 green; 5 blue, 3 green, 4 red; 5 red, 5 blue, 6 green
Game 46: 12 red, 2 blue, 3 green; 15 red, 14 blue, 11 green; 6 red, 11 blue, 6 green; 4 red, 1 green; 7 blue, 14 red; 14 red, 18 blue, 6 green
Game 47: 3 blue, 5 red, 4 green; 1 blue, 10 red; 6 blue, 5 green, 7 red; 3 red, 4 green; 2 blue, 2 green, 13 red; 4 blue, 13 red, 2 green
Game 48: 2 green, 3 blue, 7 red; 12 red, 1 green, 2 blue; 5 red, 2 blue; 4 blue, 3 green, 10 red
Game 49: 8 green, 13 blue, 3 red; 14 blue, 1 green; 14 blue, 2 green
Game 50: 1 red, 2 green, 3 blue; 2 green, 2 red; 1 green, 5 blue; 4 green
Game 51: 10 green, 5 red; 10 green, 2 blue, 2 red; 2 blue, 13 red, 1 green; 6 blue, 10 green, 3 red
Game 52: 8 green, 1 blue, 6 red; 4 green, 5 blue; 4 green, 7 red; 3 blue, 6 green, 3 red; 7 red, 6 blue, 7 green; 4 red, 8 green, 4 blue
Game 53: 11 blue, 10 green, 1 red; 6 blue, 1 green, 12 red; 6 green, 12 blue, 13 red; 1 blue, 10 green, 10 red; 11 green, 2 blue; 7 green, 7 red, 5 blue
Game 54: 3 blue, 1 green, 7 red; 18 blue, 3 red, 1 green; 11 blue, 6 red
Game 55: 9 blue, 1 red; 3 blue, 1 green, 2 red; 1 green, 6 blue, 5 red; 1 green, 5 red, 12 blue; 5 red, 3 green, 12 blue; 12 blue
Game 56: 3 red, 1 green, 11 blue; 2 red, 20 blue; 12 blue, 4 red; 3 red, 2 blue, 6 green
Game 57: 1 green, 13 red, 1 blue; 7 green, 2 red, 2 blue; 6 red, 3 blue; 6 blue, 4 red, 3 green; 1 green, 11 red
Game 58: 3 red, 13 blue, 2 green; 6 green, 6 red, 19 blue; 4 blue, 9 green, 1 red; 1 blue, 6 red
Game 59: 11 red, 2 blue, 2 green; 1 blue, 13 red; 12 red, 6 blue
Game 60: 8 blue, 4 red, 11 green; 10 green; 5 blue, 3 red, 8 green; 6 blue, 6 red, 12 green
Game 61: 1 green, 1 blue, 3 red; 1 blue, 2 green, 5 red; 4 red, 1 green, 1 blue; 5 red, 2 green
Game 62: 14 blue, 2 green, 11 red; 11 red, 2 green, 8 blue; 5 blue, 14 red, 5 green; 17 red, 2 blue, 3 green; 2 red, 3 green, 5 blue; 11 blue, 10 red, 3 green
Game 63: 2 blue, 2 green; 9 blue, 3 red; 1 green, 2 red, 12 blue
Game 64: 14 green, 1 blue, 5 red; 4 red, 14 green, 12 blue; 10 blue, 3 red, 10 green
Game 65: 1 green, 6 red, 6 blue; 7 red, 7 blue, 3 green; 14 blue, 5 red
Game 66: 10 blue, 2 red, 7 green; 3 red, 16 blue; 10 green, 7 red, 17 blue; 10 red, 5 green, 5 blue; 13 blue, 10 green, 6 red
Game 67: 9 blue, 6 green; 1 red, 8 blue, 9 green; 3 blue, 1 green, 1 red; 2 blue, 6 green, 1 red
Game 68: 4 green, 9 red, 3 blue; 6 blue, 5 green, 2 red; 6 blue, 9 red, 3 green; 4 red, 2 green; 4 red, 9 green
Game 69: 1 green, 1 blue, 2 red; 2 red, 7 green; 3 red, 1 blue, 5 green; 8 red, 7 green; 2 green, 1 blue; 6 red, 1 blue, 7 green
Game 70: 13 blue, 3 green, 5 red; 1 red, 1 green, 6 blue; 4 red, 11 blue; 14 blue, 5 red, 1 green; 8 red, 16 blue, 1 green
Game 71: 1 blue, 1 green; 6 blue, 2 red; 5 green, 1 red, 4 blue; 4 green, 3 red
Game 72: 4 green, 2 blue, 11 red; 4 red, 7 green, 4 blue; 3 red, 6 green, 14 blue; 4 green, 12 red, 15 blue; 4 blue, 14 red; 6 blue, 13 red, 6 green
Game 73: 4 green, 6 red, 7 blue; 11 red, 4 blue, 6 green; 8 red, 2 blue, 5 green; 3 red, 1 green, 7 blue
Game 74: 5 blue, 10 green; 6 green, 5 blue, 10 red; 4 green, 2 red, 1 blue; 3 blue, 11 green
Game 75: 3 red, 3 green, 15 blue; 6 blue, 3 green, 5 red; 11 blue, 1 red, 3 green; 7 blue, 3 green, 4 red; 9 blue, 1 red, 3 green
Game 76: 11 red; 7 green, 12 red; 2 red, 1 blue, 2 green; 2 red, 1 blue, 6 green; 5 red, 7 green; 1 blue, 8 green
Game 77: 2 blue, 15 green, 1 red; 6 blue, 1 red; 1 green, 5 blue, 1 red; 2 blue, 1 red, 1 green; 15 green, 8 blue, 1 red; 19 green, 5 blue
Game 78: 14 red, 2 green, 7 blue; 2 green, 14 red, 3 blue; 1 blue, 7 red
Game 79: 15 red, 2 green, 1 blue; 3 red, 1 green; 12 red, 2 blue; 12 red, 1 green; 1 blue, 2 red, 1 green
Game 80: 2 red, 1 green, 7 blue; 7 red, 6 blue, 5 green; 6 blue, 6 red; 6 green, 2 blue, 3 red; 5 red, 5 blue, 1 green
Game 81: 10 red, 1 green, 3 blue; 6 green, 13 blue, 3 red; 1 green, 2 red, 10 blue
Game 82: 4 blue, 1 red, 7 green; 4 red, 14 blue, 8 green; 1 red, 11 blue, 6 green
Game 83: 10 red, 3 blue, 9 green; 3 green, 3 red, 1 blue; 4 blue, 11 green, 8 red; 2 blue, 8 green, 2 red; 2 green, 2 red
Game 84: 2 green, 2 blue, 14 red; 7 red, 5 blue, 11 green; 4 red, 6 blue, 5 green; 3 blue, 13 green, 14 red; 6 red, 7 blue, 8 green; 2 blue, 3 red, 18 green
Game 85: 8 green, 14 blue; 6 green, 9 red, 15 blue; 9 red, 12 green, 15 blue; 12 green, 6 red; 9 green, 10 red, 15 blue; 12 blue, 6 green
Game 86: 1 blue, 1 green, 4 red; 6 green, 4 red, 6 blue; 1 red, 4 blue, 4 green; 6 green, 2 blue, 1 red
Game 87: 17 blue, 13 green; 8 blue, 3 red; 16 green, 4 red, 6 blue
Game 88: 11 red, 16 blue, 6 green; 10 red, 2 blue, 1 green; 5 blue, 2 green, 14 red
Game 89: 3 blue, 2 green; 2 red; 9 blue, 8 green, 1 red; 2 green, 2 blue, 3 red; 4 red, 3 green
Game 90: 2 blue, 14 red, 2 green; 6 blue, 2 red, 2 green; 17 red, 1 blue, 6 green; 1 blue, 8 green, 1 red
Game 91: 6 green, 1 blue, 13 red; 10 red, 4 green, 12 blue; 9 green, 17 red, 3 blue; 12 blue, 5 red, 2 green; 2 green, 9 red, 14 blue
Game 92: 2 red, 4 green, 6 blue; 9 blue, 3 green, 6 red; 5 blue, 4 green; 3 blue, 2 green, 7 red; 4 red, 4 green, 11 blue
Game 93: 4 red, 11 blue, 9 green; 10 blue, 3 green, 9 red; 3 green, 11 red, 1 blue
Game 94: 11 green, 3 red, 1 blue; 3 green, 2 red, 6 blue; 2 red, 6 blue, 5 green; 4 blue, 5 green, 5 red; 17 green, 6 red, 6 blue; 5 green, 6 red, 7 blue
Game 95: 1 red, 3 blue, 15 green; 5 green, 6 blue; 11 green, 2 red, 11 blue; 15 green, 5 red, 7 blue
Game 96: 13 red, 3 blue; 3 red, 13 blue; 5 blue, 1 red, 2 green; 7 red, 7 blue; 12 red, 9 blue, 3 green; 8 red, 15 blue, 2 green
Game 97: 4 blue, 9 green, 2 red; 2 red, 5 green, 13 blue; 9 blue, 2 red, 16 green
Game 98: 3 red; 1 green, 10 red; 2 blue, 8 red; 1 green, 11 red, 2 blue
Game 99: 6 red, 14 green; 8 green, 15 red; 1 red, 4 green; 2 blue, 7 green, 13 red; 14 green, 5 red, 1 blue; 1 blue, 5 red, 8 green
Game 100: 9 blue, 18 green, 4 red; 5 green, 10 blue, 11 red; 1 green, 1 red; 16 green, 5 red, 1 blue"""

def day_input_test():
    return """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
