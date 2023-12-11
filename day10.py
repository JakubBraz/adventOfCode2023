EXTRA_CHAR = ','


def parse_input(inp):
    inp = inp.split('\n')
    s = [(x, y) for x in range(len(inp)) for y in range(len(inp[x])) if inp[x][y] == 'S'][0]
    return s, [[c for c in row] for row in inp]


def pipes():
    return "|-LJ7F"


def pick_s(s, inp):
    x, y = s
    if inp[x-1][y] in '|7F' and inp[x+1][y] in '|LJ':
        return '|'
    if inp[x][y-1] in '-LF' and inp[x][y+1] in '-J7':
        return '-'
    if inp[x-1][y] in '|7F' and inp[x][y+1] in '-J7':
        return 'L'
    if inp[x-1][y] in '|7F' and inp[x][y-1] in '-LF':
        return 'J'
    if inp[x+1][y] in '|LJ' and inp[x][y-1] in '-LF':
        return '7'
    if inp[x+1][y] in '|LJ' and inp[x][y+1] in '-J7':
        return 'F'
    raise Exception(f'Unreachable {s} {inp[x][y]}')


def pipe_step(xy, inp):
    x, y = xy
    if inp[x][y] == '|':
        return [(x-1, y), (x+1, y)]
    if inp[x][y] == '-':
        return [(x, y-1), (x, y+1)]
    if inp[x][y] == 'L':
        return [(x-1, y), (x, y+1)]
    if inp[x][y] == 'J':
        return [(x-1, y), (x, y-1)]
    if inp[x][y] == '7':
        return [(x, y-1), (x+1, y)]
    if inp[x][y] == 'F':
        return [(x, y+1), (x+1, y)]
    raise Exception(f'Not reachable: {xy}, {inp[x][y]}')


def insert_row(board, i):
    new_row = []
    for j in range(len(board[i])):
        to_insert = (False, '|') if (board[i][j][1], board[i+1][j][1]) in [
            ('|', '|'), ('|', 'L'), ('|', 'J'),
            ('7', '|'), ('7', 'L'), ('7', 'J'),
            ('F', '|'), ('F', 'L'), ('F', 'J')
        ] else (False, EXTRA_CHAR)
        new_row.append(to_insert)
    board.insert(i+1, new_row)


def enhance_one_row(inp):
    for i in range(len(inp) - 1):
        for j in range(len(inp[i])):
            if (inp[i][j][1], inp[i+1][j][1]) in [
                ('-', '-'), ('-', '7'), ('-', 'F'),
                ('L', '-'), ('L', '7'), ('L', 'F'),
                ('J', '-'), ('J', '7'), ('J', 'F')
            ]:
                insert_row(inp, i)
                return True
    return False


def insert_col(board, j):
    for row in board:
        to_insert = (False, '-') if (row[j][1], row[j+1][1]) in [
            ('-', '-'), ('-', 'J'), ('-', '7'),
            ('L', '-'), ('L', 'J'), ('L', '7'),
            ('F', '-'), ('F', 'J'), ('F', '7')
        ] else (False, EXTRA_CHAR)
        row.insert(j+1, to_insert)


def enhance_one_col(inp):
    for j in range(len(inp[0])-1):
        for i in range(len(inp)):
            if (inp[i][j][1], inp[i][j+1][1]) in [
                ('|', '|'), ('|', 'L'), ('|', 'F'),
                ('J', '|'), ('J', 'L'), ('J', 'F'),
                ('7', '|'), ('7', 'L'), ('7', 'F')
            ]:
                insert_col(inp, j)
                return True
    return False


def enhance_rows(board):
    while enhance_one_row(board):
        # continue until no changes
        pass


def enhance_cols(board):
    while enhance_one_col(board):
        # continue until no changes
        pass


def loop_indices(board, s):
    result = {s}
    prev = s
    s = pipe_step(s, board)[0]
    while s not in result:
        result.add(s)
        s, prev = [(x, y) for x, y in pipe_step(s, board) if (x, y) != prev][0], s
    return result


def not_loop_indices(board, loop):
    return {(x, y) for x in range(len(board)) for y in range(len(board[x])) if (x, y) not in loop}


def outside_unreachable(x, y, visited, board, loop):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[x]):
        return False
    to_visit = {(x, y) for x, y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if (x, y) not in visited and (x, y) not in loop}
    if not to_visit:
        return True
    visited.update(to_visit)
    while to_visit:
        xy = to_visit.pop()
        if not outside_unreachable(xy[0], xy[1], visited, board, loop):
            return False
    return True


def solve2(board):
    s, board = board
    sx, sy = s
    board[sx][sy] = ('S', pick_s(s, board))
    board = [[(True, line[y]) if isinstance(line[y], str) else line[y] for y in range(len(line))] for line in board]
    enhance_rows(board)
    enhance_cols(board)
    s = [(x, y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y][0] == 'S'][0]
    board_no_bool = [[b[1] for b in row] for row in board]
    loop = loop_indices(board_no_bool, s)
    ground = not_loop_indices(board, loop)
    ground_to_check = not_loop_indices(board, loop)
    if len(loop) + len(ground) != len(board) * len(board[0]):
        raise Exception(f'Not reachable {len(loop)} {len(ground)}')
    result = set()
    while ground_to_check:
        gx, gy = ground_to_check.pop()
        tiles = {(gx, gy)}
        in_loop = outside_unreachable(gx, gy, tiles, board, loop)
        if in_loop:
            r = tiles - loop
            result |= r
        ground_to_check = ground_to_check - tiles
    result = {(x, y) for x, y in result if board[x][y][0]}
    return len(result)


def solve1(inp):
    s, inp = inp
    s_val = pick_s(s, inp)
    inp[s[0]][s[1]] = s_val
    prev = s
    step = pipe_step(s, inp)[0]
    i = 1
    while step != s:
        step, prev = [(x, y) for x, y in pipe_step(step, inp) if (x, y) != prev][0], step
        i += 1
    return i // 2


def main():
    inp = parse_input(day_input())
    print(solve1(inp))
    inp = parse_input(day_input())
    print(solve2(inp))


def day_input():
    return """"""
