def parse_input(inp):
    inp = inp.split('\n')
    return inp


def step(board, current):
    x, y, direction = current
    if (direction, board[x][y]) in [('>', '.'), ('>', '-'), ('^', '/'), ('V', '\\')]:
        return [(x, y + 1, '>')]
    elif (direction, board[x][y]) in [('<', '.'), ('<', '-'), ('^', '\\'), ('V', '/')]:
        return [(x, y - 1, '<')]
    elif (direction, board[x][y]) in [('^', '.'), ('^', '|'), ('>', '/'), ('<', '\\')]:
        return [(x - 1, y, '^')]
    elif (direction, board[x][y]) in [('V', '.'), ('V', '|'), ('>', '\\'), ('<', '/')]:
        return [(x + 1, y, 'V')]
    elif (direction, board[x][y]) in [('>', '|'), ('<', '|')]:
        return [(x - 1, y, '^'), (x + 1, y, 'V')]
    elif (direction, board[x][y]) in [('^', '-'), ('V', '-')]:
        return [(x, y - 1, '<'), (x, y + 1, '>')]
    else:
        raise Exception('Unreachable')


def traverse(board, current, visited):
    result = []
    to_visit = [current]
    while to_visit:
        current = to_visit.pop()
        x, y, direction = current
        if any([x < 0, y < 0, x >= len(board), y >= len(board[0]), current in visited]):
            continue
        result.append((x, y))
        visited.add(current)
        for new_x, new_y, new_dir in step(board, current):
            to_visit.append((new_x, new_y, new_dir))
    return result


def solve1(board):
    res = traverse(board, (0, 0, '>'), set())
    return len(set(res))


def solve2(board):
    start_down = [(0, i, 'V') for i in range(len(board[0]))]
    start_up = [(len(board) - 1, i, '^') for i in range(len(board[0]))]
    start_right = [(i, 0, '>') for i in range(1, len(board) - 1)]
    start_left = [(i, len(board[0]) - 1, '<') for i in range(1, len(board) - 1)]
    return max(len(set(traverse(board, s, set()))) for s in start_down + start_up + start_right + start_left)


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return r""""""
