def parse_input(inp):
    inp = inp.strip()
    inp = inp.split('\n')
    inp = [[c for c in line] for line in inp]
    return inp


def find_empty_north(board, col, start_i):
    i = start_i
    while i > 0 and board[i - 1][col] == '.':
        i -= 1
    return i


def find_empty_south(board, col, start_i):
    i = start_i
    while i < len(board) - 1 and board[i + 1][col] == '.':
        i += 1
    return i


def find_empty_west(board, start_col, start_row):
    i = start_col
    while i > 0 and board[start_row][i - 1] == '.':
        i -= 1
    return i


def find_empty_east(board, start_col, start_row):
    i = start_col
    while i < len(board) - 1 and board[start_row][i + 1] == '.':
        i += 1
    return i


def calc_points(board):
    return sum(len([c for c in board[i] if c == 'O']) * (len(board) - i) for i in range(len(board)))


def move(board, empty, pos, move_range):
    new_board = [[c if c in ['.', '#'] else '.' for c in row] for row in board]
    for row in move_range[0]:
        for c in move_range[1]:
            if board[row][c] == 'O':
                i = empty(new_board, c, row)
                x, y = pos(i, row, c)
                new_board[x][y] = 'O'
    return new_board


def draw(board):
    for row in board:
        print(''.join(row))
    print()


def move_cycle(board):
    board = move(board, find_empty_north, lambda i, r, c: (i, c), [range(len(board)), range(len(board[0]))])
    board = move(board, find_empty_west, lambda i, r, c: (r, i), [range(len(board)), range(len(board[0]))])
    board = move(board, find_empty_south, lambda i, r, c: (i, c),[range(len(board) - 1, -1, -1), range(len(board[0]) - 1, -1, -1)])
    board = move(board, find_empty_east, lambda i, r, c: (r, i),[range(len(board) - 1, -1, -1), range(len(board[0]) - 1, -1, -1)])
    return board


def solve1(board):
    new_board = move(board, find_empty_north, lambda i, r, c: (i, c), [range(len(board)), range(len(board[0]))])
    return calc_points(new_board)


def solve2(board):
    cycles = 1_000_000_000
    i = 0
    board = move_cycle(board)
    t = tuple(c for row in board for c in row)
    memo = {}
    while t not in memo:
        memo[t] = i
        board = move_cycle(board)
        t = tuple(c for row in board for c in row)
        i += 1
    first_cycle = i + 1
    memo = {t: 0}
    board = move_cycle(board)
    t = tuple(c for row in board for c in row)
    i = 1
    while t not in memo:
        memo[t] = i
        board = move_cycle(board)
        t = tuple(c for row in board for c in row)
        i += 1
    remaining = (cycles - first_cycle) % i
    for i in range(remaining):
        board = move_cycle(board)
    return calc_points(board)


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return """"""
