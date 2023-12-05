import re


def parse_input(arg):
    res = arg.split('\n')
    res = [x[x.find(': ') + 2:] for x in res]
    res = [x.split(" | ") for x in res]
    res = [(re.findall('\d+', ''.join(x[0])), re.findall('\d+', ''.join(x[1]))) for x in res]
    return res


def solve1(inp):
    result = 0
    for winning, current in inp:
        current = [x for x in current if x in winning]
        if not current:
            continue
        res = 1 << (len(current) - 1)
        result += res
    return result


def solve2(inp):
    cards = {i: 1 for i, _ in enumerate(inp)}
    for game, (winning, current) in enumerate(inp):
        current = [x for x in current if x in winning]
        new_indices = range(game+1, game + 1 + len(current))
        for i in new_indices:
            if i in cards:
                cards[i] += cards[game]
    return sum(v for v in cards.values())


def main():
    res = day_input()
    res = parse_input(res)
    print(solve1(res))
    print(solve2(res))


def day_input():
    return """"""
