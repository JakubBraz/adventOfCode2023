def parse_input(arg, more_parsing = False):
    res = arg.split('\n')
    if more_parsing:
        res = [parse_line(line) for line in res]
    res = [''.join(x for x in line if x.isnumeric()) for line in res]
    res = [int(x[0] + x[-1]) for x in res]
    return res


def parse_line(line):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_map = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    result = ""
    while line:
        for n in nums:
            if line[:len(n)] == n:
                result += num_map[n]
        if line[0].isnumeric():
            result += line[0]
        line = line[1:]
    return result


def main():
    parsed = parse_input(day_input())
    print(sum(parsed))

    parsed = parse_input(day_input(), True)
    print(sum(parsed))


def day_input(is_test = False):
    if is_test:
        return """"""
