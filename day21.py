def parse_input(inp):
    inp = inp.split('\n')
    inp = [[c for c in line] for line in inp]
    s = [(x, y) for x in range(len(inp)) for y in range(len(inp[x])) if inp[x][y] == 'S'][0]
    return s, inp


def possible(x, y, board):
    return [(nx, ny) for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if
            board[nx % len(board)][ny % len(board[0])] != '#']


def traverse2(target, s, board):
    prev = {(s[0], s[1])}
    for i in range(target):
        prev = {(nx, ny) for x, y in prev for nx, ny in possible(x, y, board)}
    return prev


def solve1(inp):
    s, board = inp
    res = traverse2(64, s, board)
    return len(res)


def count_full(board):
    result_even = 0
    result_odd = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (x + y) % 2 == 0 and board[x][y] in ['.', 'S']:
                result_even += 1
            elif (x + y) % 2 != 0 and board[x][y] in ['.', 'S']:
                result_odd += 1
    return result_even, result_odd


# 0 1
# 2 3
# count rem considers only even, because (n - 1) // 2 is odd for input where n == 131
# ie, rem starts at point (0, 0)
def count_rem(board, part):
    result = 0
    n = len(board)
    ranges = {
        0: (range(0, n // 2), lambda i: range(0, n // 2 - i), lambda i: i % 2 != 0),
        1: (range(0, n // 2), lambda i: range(n // 2 + i, n), lambda i: True),
        2: (range(n // 2, n), lambda i: range(0, i - n // 2), lambda i: i % 2 != 0),
        3: (range(n // 2, n), lambda i: range(n - (i - n // 2), n), lambda i: False)
    }
    range_x, range_y, do_skip = ranges[part]
    for x in range_x:
        skip = do_skip(x)
        for y in range_y(x):
            if not skip and board[x][y] in ['.', 'S']:
                result += 1
            skip = not skip
    return result


# count rem_diamond considers only odd, because (n - 1) // 2 is odd for input where n == 131
# ie, it excludes (0, 0)
def count_rem_diamond(board, part):
    result = 0
    n = len(board)
    ranges = {
        0: (range(0, n // 2), lambda i: range(0, n // 2 - i), lambda i: i % 2 == 0),
        1: (range(0, n // 2), lambda i: range(n // 2 + 1 + i, n), lambda i: True),
        2: (range(n // 2 + 1, n), lambda i: range(0, i - n // 2), lambda i: i % 2 == 0),
        3: (range(n // 2 + 1, n), lambda i: range(n - (i - n // 2), n), lambda i: True)
    }
    range_x, range_y, do_skip = ranges[part]
    for x in range_x:
        skip = do_skip(x)
        for y in range_y(x):
            if not skip and board[x][y] in ['.', 'S']:
                result += 1
            skip = not skip
    return result


def count_diamond(board, exclude_parts):
    result = 0
    n = len(board)
    for x in range(0, n):
        for y in range(0, n):
            if (x + y) % 2 == 1 and board[x][y] in ['.', 'S']:
                result += 1
    to_exclude = [count_rem_diamond(board, p) for p in exclude_parts]
    result -= sum(to_exclude)
    return result


def count_all(n, steps, board):
    global_n = 2 * (steps - n // 2) // n + 1
    small_fragment_count = global_n // 2
    big_fragment_count = small_fragment_count - 1
    odd_line = (global_n - 3) // 2
    even_line = odd_line + 1
    full_odd_count = odd_line * odd_line
    full_even_count = even_line * even_line
    tmp = small_fragment_count - 1
    empty_count = (tmp * tmp - tmp) // 2 + tmp

    assert full_odd_count + full_even_count + 4 + 4 * (
                small_fragment_count + big_fragment_count + empty_count) == global_n * global_n

    even, odd = count_full(board)
    top = count_diamond(board, [0, 1])
    right = count_diamond(board, [1, 3])
    bottom = count_diamond(board, [2, 3])
    left = count_diamond(board, [0, 2])
    small_fragments = [
        count_rem(board, 0),
        count_rem(board, 1),
        count_rem(board, 2),
        count_rem(board, 3)
    ]
    big_fragments = [
        count_diamond(board, [0]),
        count_diamond(board, [1]),
        count_diamond(board, [2]),
        count_diamond(board, [3])
    ]
    return (
            top + right + bottom + left +
            sum(small_fragment_count * x for x in small_fragments) +
            sum(big_fragment_count * x for x in big_fragments) +
            even * full_even_count +
            odd * full_odd_count
    )


def find_holes(board):
    return [(x, y) for x in range(1, len(board) - 1) for y in range(1, len(board) - 1)
            if all([board[x + 1][y] == '#', board[x - 1][y] == '#', board[x][y + 1] == '#', board[x][y - 1] == '#'])]


def solve2(inp, steps):
    s, board = inp
    holes = find_holes(board)
    for x, y in holes:
        board[x][y] = '#'
    return count_all(len(board), steps, board)


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed, 26501365))


def day_input():
    return """"""
