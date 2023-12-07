from collections import Counter


def parse_input(inp):
    inp = inp.split('\n')
    inp = [[x.split()[0], int(x.split()[1])] for x in inp]
    return inp


def get_type(hand):
    n = len(hand)
    sn = len(set(hand))
    c = Counter(hand)
    cv = sorted(c.values(), reverse=True)
    if n == sn:
        return 0
    if sn == 4:
        return 1
    if sn == 3 and cv[:2] == [2,2]:
        return 2
    if sn == 3 and cv[0] == 3:
        return 3
    if sn == 2 and cv[0] == 3:
        return 4
    if sn == 2:
        return 5
    if sn == 1:
        return 6


def get_type_joker(hand):
    c = Counter(hand)
    high_card = {v: -i for i, v in enumerate(reversed("AKQT98765432"))}
    if c['J'] > 3:
        return 6
    tuples = [(i, v) for v, i in c.items() if v != 'J']
    _to_replace_count, to_replace_card = max(tuples, key=lambda x: (x[0], high_card[x[1]]))
    new_hand = ''.join(to_replace_card if x == 'J' else x for x in hand)
    return get_type(new_hand)


def solve(inp, get_type_function, high_card_dict):
    inp_sorted = sorted(inp, key=lambda x: (get_type_function(x[0]), [high_card_dict[c] for c in x[0]]))
    return sum((rank + 1) * hand[1] for rank, hand in enumerate(inp_sorted))


def main():
    inp = parse_input(get_input())
    print(solve(inp, get_type, {v: -i for i, v in enumerate("AKQJT98765432")}))
    print(solve(inp, get_type_joker, {v: -i for i, v in enumerate("AKQT98765432J")}))


def get_input():
    return """"""
