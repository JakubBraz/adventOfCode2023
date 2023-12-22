import heapq
from collections import defaultdict

INF = 1_000_000_000


def parse_input(inp):
    inp = inp.split('\n')
    inp = [[int(c) for c in row] for row in inp]
    return inp


def get_next_pos(xy, consecutive, consecutive_len, board):
    if consecutive == '':
        return []
    x, y = xy
    if len(consecutive) == consecutive_len and len(set(consecutive)) == 1:
        if consecutive[-1] in '<>':
            res = [(x - 1, y, '^'), (x + 1, y, 'V')]
        elif consecutive[-1] in '^V':
            res = [(x, y - 1, '<'), (x, y + 1, '>')]
        else:
            raise Exception('Unreachable')
    elif consecutive[-1] == 'X':
        res = [(x + 1, y, 'V'), (x, y + 1, '>')]
    elif consecutive_len == 10 and len(set(consecutive[-4:])) != 1:
        if consecutive[-1] == '>':
            res = [(x, y + 1, '>')]
        elif consecutive[-1] == '<':
            res = [(x, y - 1, '<')]
        elif consecutive[-1] == 'V':
            res = [(x + 1, y, 'V')]
        elif consecutive[-1] == '^':
            res = [(x - 1, y, '^')]
        else:
            raise Exception('Unreachable')
    else:
        if consecutive[-1] == '>':
            res = [(x - 1, y, '^'), (x + 1, y, 'V'), (x, y + 1, '>')]
        elif consecutive[-1] == '<':
            res = [(x - 1, y, '^'), (x + 1, y, 'V'), (x, y - 1, '<')]
        elif consecutive[-1] == 'V':
            res = [(x + 1, y, 'V'), (x, y - 1, '<'), (x, y + 1, '>')]
        elif consecutive[-1] == '^':
            res = [(x - 1, y, '^'), (x, y - 1, '<'), (x, y + 1, '>')]
        else:
            raise Exception('Unreachable')
    res = [(rx, ry, (consecutive + c)[-consecutive_len:]) for rx, ry, c in res if
           all([rx >= 0, rx < len(board), ry >= 0, ry < len(board[0])])]
    return res


def get_next_pos2(xy, consecutive, board):
    if consecutive == '':
        return []
    x, y = xy
    if len(consecutive) == 10 and len(set(consecutive)) == 1:
        if consecutive[-1] in '<>':
            res = [(x - 1, y, '^'), (x + 1, y, 'V')]
        elif consecutive[-1] in '^V':
            res = [(x, y - 1, '<'), (x, y + 1, '>')]
        else:
            raise Exception('Unreachable')
    elif consecutive[-1] == 'X':
        res = [(x + 1, y, 'V'), (x, y + 1, '>')]
    elif len(set(consecutive[-4:])) != 1:
        if consecutive[-1] == '>':
            res = [(x, y + 1, '>')]
        elif consecutive[-1] == '<':
            res = [(x, y - 1, '<')]
        elif consecutive[-1] == 'V':
            res = [(x + 1, y, 'V')]
        elif consecutive[-1] == '^':
            res = [(x - 1, y, '^')]
        else:
            raise Exception('Unreachable')
    else:
        if consecutive[-1] == '>':
            res = [(x - 1, y, '^'), (x + 1, y, 'V'), (x, y + 1, '>')]
        elif consecutive[-1] == '<':
            res = [(x - 1, y, '^'), (x + 1, y, 'V'), (x, y - 1, '<')]
        elif consecutive[-1] == 'V':
            res = [(x + 1, y, 'V'), (x, y - 1, '<'), (x, y + 1, '>')]
        elif consecutive[-1] == '^':
            res = [(x - 1, y, '^'), (x, y - 1, '<'), (x, y + 1, '>')]
        else:
            raise Exception('Unreachable')
    res = [(rx, ry, (consecutive + c)[-10:]) for rx, ry, c in res if
           all([rx >= 0, rx < len(board), ry >= 0, ry < len(board[0])])]
    return res


def dijkstra(board, consecutive_len):
    dists = [[defaultdict(lambda: INF) for _ in range(len(board[0]))] for _ in range(len(board))]
    dists[0][0]['X'] = 0
    q = [(INF, x, y, '') for x in range(len(board[0])) for y in range(len(board)) if (x, y) != (0, 0)]
    q.append((0, 0, 0, 'X'))
    heapq.heapify(q)
    while q:
        d, x, y, cons = heapq.heappop(q)
        for nx, ny, new_cons in get_next_pos((x, y), cons, consecutive_len, board):
            new_d = d + board[nx][ny]
            if new_d < dists[nx][ny][new_cons]:
                dists[nx][ny][new_cons] = new_d
                heapq.heappush(q, (new_d, nx, ny, new_cons))
    return min(dists[-1][-1].values())


def solve1(board):
    return dijkstra(board, 3)


def solve2(board):
    return dijkstra(board, 10)


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return """"""
