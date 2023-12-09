from functools import reduce


def parse_input(inp):
    inp = inp.split('\n')
    inp = [[int(x) for x in line.split(' ')] for line in inp]
    return inp


def generate_diffs(vals):
    return [vals[i] - vals[i-1] for i in range(1, len(vals))]


def find_num(vals, operation, last_operation):
    nums = [vals]
    while any(x != vals[0] for x in vals):
        vals = generate_diffs(vals)
        nums.append(vals)
    last_diff = reduce(operation, reversed(nums), 0)
    return last_operation(last_diff)


def solve1(vals):
    return sum(find_num(x, lambda x, y: x + y[-1], lambda x: x) for x in vals)


def solve2(vals):
    return sum(find_num(list(reversed(x)), lambda x, y: x - y[-1], lambda x: -x) for x in vals)


def main():
    inp = parse_input(day_input())
    print(solve1(inp))
    print(solve2(inp))


def day_input():
    return """"""
