from sympy import *


def parse_input(inp):
    inp = inp.split('\n')
    inp = [x.split(' @ ') for x in inp]
    inp = [[[int(y) for y in x.split(', ')] for x in line] for line in inp]
    return inp


def calc_function(linear_function):
    (x, y, z), (a, b, c) = linear_function
    x2 = x + a
    y2 = y + b
    angle = (y2 - y) / (x2 - x)
    offset = y - angle * x
    return angle, offset


def cross_point(ab1, ab2):
    a1, b1 = ab1
    a2, b2 = ab2

    if a1 == a2:
        return None

    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y


def not_in_past(f, cross):
    (x, y, z), (a, b, c) = f
    x2 = x + a
    if x2 < x:
        return cross[0] <= x2 <= x or x2 <= cross[0] <= x
    return x <= x2 <= cross[0] or x <= cross[0] <= x2


"""
Rx + t1 * Ra = Ax + t1 * Aa
Ry + t1 * Rb = Ay + t1 * Ab
Rz + t1 * Rc = Az + t1 * Ac

Rx + t2 * Ra = Bx + t2 * Ba
Ry + t2 * Rb = By + t2 * Bb
Rz + t2 * Rc = Bz + t2 * Bc

Rx + t3 * Ra = Cx + t3 * Ca
Ry + t3 * Rb = Cy + t3 * Cb
Rz + t3 * Rc = Cz + t3 * Cc
"""


def solve_equations(f1, f2, f3):
    s = symbols(['Rx', 'Ry', 'Rz', 'Ra', 'Rb', 'Rc', 't1', 't2', 't3'])
    Rx, Ry, Rz, Ra, Rb, Rc, t1, t2, t3 = s
    (Ax, Ay, Az), (Aa, Ab, Ac) = f1
    (Bx, By, Bz), (Ba, Bb, Bc) = f2
    (Cx, Cy, Cz), (Ca, Cb, Cc) = f3

    eqs = [
        Eq(Rx + t1 * Ra, Ax + t1 * Aa),
        Eq(Ry + t1 * Rb, Ay + t1 * Ab),
        Eq(Rz + t1 * Rc, Az + t1 * Ac),
        Eq(Rx + t2 * Ra, Bx + t2 * Ba),
        Eq(Ry + t2 * Rb, By + t2 * Bb),
        Eq(Rz + t2 * Rc, Bz + t2 * Bc),
        Eq(Rx + t3 * Ra, Cx + t3 * Ca),
        Eq(Ry + t3 * Rb, Cy + t3 * Cb),
        Eq(Rz + t3 * Rc, Cz + t3 * Cc)
    ]

    solutions = solve(eqs, s)
    return sum(solutions[0][:3])


def solve1(nums, limit1, limit2):
    filtered = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ab1 = calc_function(nums[i])
            ab2 = calc_function(nums[j])
            cross = cross_point(ab1, ab2)
            if cross and limit1 <= cross[0] <= limit2 and limit1 <= cross[1] <= limit2:
                filtered.append((nums[i], nums[j], cross))
    filtered = [not_in_past(f1, c) and not_in_past(f2, c) for f1, f2, c in filtered]
    return len([x for x in filtered if x])


def solve2(nums):
    return solve_equations(nums[0], nums[1], nums[2])


def main():
    print(solve1(parse_input(day_input()), 200000000000000, 400000000000000))
    print(solve2(parse_input(day_input())))


def day_input():
    return """"""
