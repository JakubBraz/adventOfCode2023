def parse_input(inp):
    inp = inp.split('\n')
    inp = [x.split('~') for x in inp]
    inp = [([int(c) for c in x[0].split(',')], [int(c) for c in x[1].split(',')]) for x in inp]
    inp = sorted(inp, key=lambda x: x[0][2])
    inp = [to_points(b) for b in inp]
    return inp


def to_points(brick):
    a, b = brick
    if a[0] == b[0] and a[1] == b[1]:
        z_min = min(a[2], b[2])
        z_max = max(a[2], b[2])
        return [(a[0], a[1], z) for z in range(z_min, z_max + 1)]
    if a[0] == b[0] and a[2] == b[2]:
        y_min = min(a[1], b[1])
        y_max = max(a[1], b[1])
        return [(a[0], y, a[2]) for y in range(y_min, y_max + 1)]
    if a[1] == b[1] and a[2] == b[2]:
        x_min = min(a[0], b[0])
        x_max = max(a[0], b[0])
        return [(x, a[1], b[2]) for x in range(x_min, x_max + 1)]
    raise Exception('unreachable')


def to_space(bricks):
    return {p for brick in bricks for p in brick}


def count_fall(bricks, ind_to_exclude = -1):
    result = []
    for i in range(len(bricks)):
        # space = to_space(bricks[:i] + bricks[i+1:])
        space = to_space([bricks[ind] for ind in range(i) if ind != ind_to_exclude])
        if all((x, y, z - 1) not in space and z != 1 for x, y, z in bricks[i]):
            result.append(i)
    return result


def can_fall(bricks):
    for i in range(len(bricks)):
        # space = to_space(bricks[:i] + bricks[i+1:])
        space = to_space(bricks[:i])
        if all((x, y, z - 1) not in space and z != 1 for x, y, z in bricks[i]):
            return True
    return False


def fall_down(bricks):
    counter = set()
    while to_fall := count_fall(bricks):
        for i in to_fall:
            # print('... spada', bricks[i])
            bricks[i] = [(x, y, z - 1) for x, y, z in bricks[i]]
            counter.add(i)
    print('everything felt down')
    return counter


def can_be_removed(bricks):
    result = []
    for i in range(len(bricks)):
        print('can remove', i)
        if not can_fall(bricks[:i] + bricks[i+1:]):
            result.append(i)
    return result


def cant_be_removed(bricks):
    result = []
    for i in range(len(bricks)):
        print('cant remove', i)
        if can_fall(bricks[i+1:]):
            result.append(i)
    return result


def only_support(bricks):
    result = {}
    for i, b in enumerate(bricks):
        # result[i] = count_fall(bricks[i + 1:])
        result[i] = count_fall(bricks, i)
    return result


def solve1(bricks):
    fall_down(bricks)
    removed = can_be_removed(bricks)
    return len(removed)


def solve2(bricks):
    fall_down(bricks)
    removed = cant_be_removed(bricks)
    result = 0

    only = only_support(bricks)

    for ind, i in enumerate(removed):
        print('removing', ind, 'among', len(removed))
        new_bricks = [b for b in bricks]
        result += len(fall_down(new_bricks[:i] + new_bricks[i+1:]))
    return result


def main():
    # parsed = parse_input(day_input_test())
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input_test():
    return """"""


def day_input():
    return """"""
