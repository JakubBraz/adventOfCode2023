INF = 1_000_000_000


def parse_input(inp):
    inp = inp.split('\n')
    inp = [[c for c in line] for line in inp]
    start_y = [y for y in range(len(inp[0])) if inp[0][y] == '.'][0]
    stop_y = [y for y in range(len(inp[0])) if inp[-1][y] == '.'][0]
    return (0, start_y), (len(inp) - 1, stop_y), inp


def get_neighbours(x, y, board):
    if board[x][y] == '<':
        return [(x, y - 1)]
    if board[x][y] == '>':
        return [(x, y + 1)]
    if board[x][y] == '^':
        return [(x - 1, y)]
    if board[x][y] == 'v':
        return [(x + 1, y)]
    res = [(nx, ny) for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
           if 0 <= nx < len(board) and 0 <= ny < len(board[nx]) and board[nx][ny] in ['.', '>', '<', '^', 'v']]
    return res


def get_crosswalks(board):
    return [(x, y) for x in range(len(board)) for y in range(len(board[0])) if
            board[x][y] != '#' and len(get_neighbours(x, y, board)) > 2]


def find_crosswalks_distances(init_xy, crosswalks, board):
    x, y = init_xy
    paths = get_neighbours(x, y, board)
    result = []
    for nx, ny in paths:
        prev = init_xy
        dist = 2
        while True:
            (nx, ny), prev = [xy for xy in get_neighbours(nx, ny, board) if xy != prev][0], (nx, ny)
            if (nx, ny) in crosswalks:
                result.append(((nx, ny), dist))
                break
            dist += 1
    return result


def traverse_crosswalks(current, target, visited, crosswalks):
    if current == target:
        return 0
    to_visit = [(xy, d) for xy, d in crosswalks[current] if xy not in visited]
    if not to_visit:
        return -INF
    return max(d + traverse_crosswalks(xy, target, visited | {xy}, crosswalks) for xy, d in to_visit)


def traverse(start, target, neighbours_fun):
    stack = [(0, start, {start})]
    result = 0
    while stack:
        d, (x, y), visited = stack.pop()
        if (x, y) == target:
            result = max(result, d)
        else:
            neighbours = neighbours_fun(x, y, visited)
            for nxy, dis in neighbours:
                stack.append((d + dis, nxy, visited | {nxy}))
    return result


def solve1(board):
    start, stop, board = board
    return traverse(start, stop, lambda x, y, v: [(xy, 1) for xy in get_neighbours(x, y, board) if xy not in v])


def solve2(board):
    start, stop, board = board
    board = [[c if c in ['.', '#'] else '.' for c in line] for line in board]
    crosswalks = get_crosswalks(board)
    crosswalks = crosswalks + [start, stop]
    dists = {p: find_crosswalks_distances(p, crosswalks, board) for p in crosswalks}
    # return traverse_crosswalks(start, stop, {start}, dists)
    return traverse(start, stop, lambda x, y, v: [(xy, d) for (xy, d) in dists[(x, y)] if xy not in v])


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return """"""
