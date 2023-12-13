def parse_input(inp):
    inp = inp.split("\n")
    inp = [x.split() for x in inp]
    inp = [(x[0], [int(i) for i in x[1].split(',')]) for x in inp]
    return inp


def possible(row: str, n: int):
    return [i for i in range(0, len(row) - n + 1)
            if (
                    (i == 0 or row[i-1] != '#') and
                    '.' not in row[i:n+i] and
                    (n + i >= len(row) or row[n+i] != '#') and
                    '#' not in row[:i]
            )]


def solve_row(row, nums, memo):
    t = (row, tuple(nums))
    if t in memo:
        return memo[t]
    if not nums and '#' not in row:
        return 1
    if not nums:
        return 0
    indices = possible(row, nums[0])
    memo[t] = sum(solve_row(row[i + nums[0] + 1:], nums[1:], memo) for i in indices)
    return memo[t]


def solve1(inp):
    return sum(solve_row(row, nums, {}) for row, nums in inp)


def solve2(inp):
    inp = [('?'.join([row[0] for _ in range(5)]), row[1] * 5) for row in inp]
    return solve1(inp)


def main():
    inp = parse_input(day_input())
    print(solve1(inp))
    print(solve2(inp))


def day_input():
    return """"""
