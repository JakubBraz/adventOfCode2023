from functools import reduce
from math import gcd


def parse_input(inp):
    inp = inp.split('\n')
    connections = {''.join(x for x in row.split(' -> ')[0] if x.isalnum()): row.split(' -> ')[1].split(', ') for row in inp}
    flip_flops = {row.split(' -> ')[0][1:]: False for row in inp if '%' in row}
    conjunctions = {row.split(' -> ')[0][1:] for row in inp if '&' in row}
    conjunctions_inputs = {c: {x: False for x, vals in connections.items() if c in vals} for c in conjunctions}
    return connections, flip_flops, conjunctions_inputs


def send_pulse(pulses, pulse_type, sender, receiver):
    pulses.append((pulse_type, sender, receiver))


def press_button(pulses):
    send_pulse(pulses, False, 'button', 'broadcaster')


def process_single_pulse(pulses, counter, pulse, relations, i, cycles):
    pulse_type, sender, receiver = pulse
    counter[receiver][pulse_type] += 1
    connections, flip_flops, conjunctions_inputs = relations

    if receiver == 'broadcaster':
        for r in connections[receiver]:
            send_pulse(pulses, pulse_type, receiver, r)
    elif receiver in flip_flops:
        if not pulse_type:
            state = not flip_flops[receiver]
            flip_flops[receiver] = state
            for r in connections[receiver]:
                send_pulse(pulses, state, receiver, r)
    elif receiver in conjunctions_inputs:
        conjunctions_inputs[receiver][sender] = pulse_type
        for r in connections[receiver]:
            send_pulse(pulses, not all(conjunctions_inputs[receiver].values()), receiver, r)

    pulses_to_check = [(False, 'tf', 'rf'), (False, 'gx', 'sr'), (False, 'gk', 'vq'), (False, 'xr', 'sn')]
    if i > -1 and pulse in pulses_to_check:
        if pulse not in cycles:
            cycles[pulse] = i
    if len(cycles) == len(pulses_to_check):
        while pulses:
            pulses.pop()
        return True


def process(pulses, counter, relations, i, cycles):
    res = False
    while pulses:
        p = pulses.pop(0)
        res = process_single_pulse(pulses, counter, p, relations, i, cycles)
    return res


def solve1(relations):
    pulses = []
    counter = {m: {False: 0, True: 0} for m in relations[0].keys()}
    counter['rx'] = {False: 0, True: 0}
    for _ in range(1000):
        press_button(pulses)
        process(pulses, counter, relations, -1, {})
    return sum(x[True] for x in counter.values()) * sum(x[False] for x in counter.values())


def lcm(a, b):
    return a * b // gcd(a, b)


def solve2(relations):
    pulses = []
    counter = {m: {False: 0, True: 0} for m in relations[0].keys()}
    counter['rx'] = {False: 0, True: 0}
    i = 0
    result = {}
    stop = False
    while not stop:
        i += 1
        press_button(pulses)
        stop = process(pulses, counter, relations, i, result)
    return reduce(lambda acc, val: lcm(acc, val), result.values())


def print_graph(inp):
    result = ""
    flip_flops = {line.split(' -> ')[0][1:] for line in inp.split('\n') if line.split(' -> ')[0][0] == '%'}
    conjunctions = {line.split(' -> ')[0][1:] for line in inp.split('\n') if line.split(' -> ')[0][0] == '&'}
    for line in inp.split('\n'):
        key, vals = line.split(' -> ')
        vals = vals.split(', ')
        for v in vals:
            to_insert = v
            if v in flip_flops:
                to_insert = '%' + to_insert
            elif v in conjunctions:
                to_insert = '&' + to_insert
            result += f"{key} {to_insert}\n"
    print(result)


def main():
    # print_graph(day_input())
    parsed = parse_input(day_input())
    print(solve1(parsed))
    parsed = parse_input(day_input())
    print(solve2(parsed))


def day_input():
    return """"""
