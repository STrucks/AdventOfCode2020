import util


def check_if_pwd_rule_applies_part1(rule: str, pwd: str):
    # interpret the rule:
    _range, _letter = rule.split(" ")
    _from, _to = int(_range.split("-")[0]), int(_range.split("-")[1])
    # check if the rule applies
    if _from <= pwd.count(_letter) <= _to:
        return True
    else:
        return False


def part1():
    data = util.load_txt_data("Day2/data1.txt")
    counter = 0
    for line in data:
        rule, pwd = line.split(": ")
        if check_if_pwd_rule_applies_part1(rule, pwd):
            counter += 1
    print("There are %d valid passwords" % counter)


def check_if_pwd_rule_applies_part2(rule: str, pwd: str):
    # interpret the rule:
    _range, _letter = rule.split(" ")
    _index1, _index2 = int(_range.split("-")[0]) - 1, int(_range.split("-")[1]) - 1
    # check if the rule applies
    if (pwd[_index1] == _letter or pwd[_index2] == _letter) and not (pwd[_index1] == _letter and pwd[_index2] == _letter):
        return True
    else:
        return False


def part2():
    data = util.load_txt_data("Day2/data1.txt")
    counter = 0
    for line in data:
        rule, pwd = line.split(": ")
        if check_if_pwd_rule_applies_part2(rule, pwd):
            counter += 1
    print("There are %d valid passwords" % counter)


#part1()
part2()
