def parse_input(inp):
    inp = inp.split('\n')
    inp = [row.split() for row in inp]
    inp = [(row[0], int(row[1]), row[2][2:-1]) for row in inp]
    return inp


def pick_dir(c):
    if c == '0':
        return 'R'
    if c == '1':
        return 'D'
    if c == '2':
        return 'L'
    if c == '3':
        return 'U'


def parse_color(color):
    return [(pick_dir(c[-1]), int(c[:-1], 16), 0) for c in color]


def get_points(instr):
    positions = [(0, 0)]
    for direction, val, _ in instr:
        x, y = positions[-1]
        if direction == 'R':
            new_points = [(x, y + 1 + i) for i in range(val)]
        elif direction == 'L':
            new_points = [(x, y - (1 + i)) for i in range(val)]
        elif direction == 'D':
            new_points = [(x + 1 + i, y) for i in range(val)]
        elif direction == 'U':
            new_points = [(x - (1 + i), y) for i in range(val)]
        else:
            raise Exception('unreachable')
        positions += new_points
    s = set(positions)
    return s


def travel(x, y, points):
    to_visit = [(x, y)]
    visited = set(points)
    while to_visit:
        x, y = to_visit.pop()
        if (x, y) in points:
            continue
        new_p = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
        new_p = {p for p in new_p if p not in visited}
        visited.update(new_p)
        for nx, ny in new_p:
            to_visit.append((nx, ny))
    return visited


def get_vertices(instr):
    x, y = 0, 0
    points = [(0, 0)]
    for direction, val, _ in instr:
        if direction == 'R':
            y += val
        elif direction == 'L':
            y -= val
        elif direction == 'D':
            x += val
        elif direction == 'U':
            x -= val
        else:
            raise Exception('unreachable')
        points.append((x, y))
    return points


def adjust(instr):
    instr = instr + [instr[0]]
    result = 0
    for i in range(len(instr) - 1):
        direction, val, _ = instr[i]
        next_dir, _, _ = instr[i + 1]
        conc = direction + next_dir
        if conc == 'LD':
            result += val - 1
        elif conc == "DL":
            result += 1
        elif conc in ["UR", "UL", "LU"]:
            result += val
    return result


def shoelace_formula(points):
    points = [(p1, p2) for p1, p2 in zip(points, points[1:])]
    res = sum(p1[0] * p2[1] - p1[1] * p2[0] for p1, p2 in points) // (-2)
    return res


def solve1(instructions):
    points = get_points(instructions)
    result = travel(1, 1, points)
    return len(result)


def solve2(instructions):
    instructions = parse_color([color for _, _, color in instructions])
    points = get_vertices(instructions)
    adjustment = adjust(instructions)
    return shoelace_formula(points) + adjustment


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return """"""
