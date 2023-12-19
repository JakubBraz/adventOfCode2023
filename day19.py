from functools import reduce


def parse_input(inp):
    workflows, parts = inp.split('\n\n')
    workflows = workflows.split('\n')
    workflows = {w.split('{')[0]: w.split('{')[1][:-1] for w in workflows}
    workflows = {k: v.split(',') for k, v in workflows.items()}
    workflows = {k: [r.split(':') for r in v] for k, v in workflows.items()}
    workflows = {k: [[r[1], r[0]] if len(r) > 1 else [r[0]] for r in v] for k, v in workflows.items()}
    workflows = {k: [[r[0], parse_rule(r[1])] if len(r) > 1 else [r[0], True] for r in v] for k, v in workflows.items()}
    parts = parts.split('\n')
    parts = [p.replace('x=', '"x":').replace('m=', '"m":').replace('a=', '"a":').replace('s=', '"s":') for p in parts]
    parts = [eval(p) for p in parts]
    return workflows, parts


def parse_rule(r):
    return r[0], r[1], int(r[2:])


def apply_workflow(workflow, part):
    for send_to, rule in workflow:
        if rule == True:
            return send_to
        field, op, val = rule
        if op == '>' and part[field] > val:
            return send_to
        elif op == '<' and part[field] < val:
            return send_to
    raise Exception('unreachable')


def reduce_conditions(current, condition):
    current = {k: [v[0], v[1]] for k, v in current.items()}
    if condition == True:
        raise Exception('unreachable')
    field, op, val = condition
    if op == '>':
        current[field][0] = max(val, current[field][0])
    elif op == '<':
        current[field][1] = min(val, current[field][1])
    else:
        raise Exception('unreachable')
    return {k: [v[0], v[1]] for k, v in current.items()}


def possible_per_condition(condition):
    return reduce(lambda acc, val: acc * (val[1] - val[0] - 1), condition.values(), 1)


def revert_rule(ind, op, val):
    if op == '<':
        return ind, '>', val - 1
    elif op == '>':
        return ind, '<', val + 1
    else:
        raise Exception('unreachable')


def calculate(current, condition, workflows):
    if current == 'A':
        return possible_per_condition(condition)
    if current == 'R':
        return 0
    result = 0
    rules_to_remove = [True] + [r for _, r in workflows[current][:-1]]
    rules_to_add = [r for _, r in workflows[current]]
    keys = [n for n, _ in workflows[current]]
    for next_key, rule_to_remove, rule_to_add in zip(keys, rules_to_remove, rules_to_add):
        condition = reduce_conditions(condition, revert_rule(*rule_to_remove)) if rule_to_remove != True else condition
        condition_added = reduce_conditions(condition, rule_to_add) if rule_to_add != True else condition
        c = calculate(next_key, condition_added, workflows)
        result += c
    return result


def solve1(inp):
    workflows, parts = inp
    result = 0
    for part in parts:
        w = 'in'
        while w not in ['A', 'R']:
            w = apply_workflow(workflows[w], part)
        if w == 'A':
            result += sum(part.values())
    return result


def solve2(inp):
    workflows, parts = inp
    c = {'x': [0, 4001], 'm': [0, 4001], 'a': [0, 4001], 's': [0, 4001]}
    return calculate('in', c, workflows)


def main():
    parsed = parse_input(day_input())
    print(solve1(parsed))
    print(solve2(parsed))


def day_input():
    return """"""
