import re

import util


# load the data:
data = util.load_txt_data("Day4/data1.txt")
# transform the data to array of dict:
passports = [] # here we store all passports as dict
_passport = {}
for line in data:
    if line == "":
        # a new passport starts_
        passports.append(_passport)
        _passport = {}
    else:
        key_value_pairs = line.split(" ")
        for key_value_pair in key_value_pairs:
            key, value = key_value_pair.split(":")
            _passport[key] = value

# also store the very last passport:
if _passport != {}:
    passports.append(_passport)


def part1():
    # iterate over the passports array and check if they have the 7 required fields
    valid_passports_count = 0
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for passport in passports:
        key_intersection = required_keys.intersection(set(passport.keys()))
        if len(key_intersection) == len(required_keys):
            valid_passports_count += 1

    print("Valid passports: %d" % valid_passports_count)


#part1()


hair_color_regex = re.compile(r"#[0-9a-f]{6}")
def check_if_passport_is_valid(passport):
    valid_passport = True
    try:
        if not (1920 <= int(passport["byr"]) <= 2002):
            valid_passport = False
        if not (2010 <= int(passport["iyr"]) <= 2020):
            valid_passport = False
        if not (2020 <= int(passport["eyr"]) <= 2030):
            valid_passport = False
        if passport["hgt"][-2:] == "cm":
            if not (150 <= int(passport["hgt"][0:3]) <= 193):
                valid_passport = False
        elif passport["hgt"][-2:] == "in":
            if not (59 <= int(passport["hgt"][0:2]) <= 76):
                valid_passport = False
        else:
            valid_passport = False
        if not hair_color_regex.match(passport["hcl"]):
            valid_passport = False
        if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            valid_passport = False
        if not len(passport["pid"]) == 9:
            valid_passport = False
        else:
            int(passport["pid"])  # if that fails, the except clause will set valid passport to false
    except Exception as e:
        # This should catch any keyerror (when required fields are missing) or type errors (passport["pid"] to int)
        valid_passport = False
    return valid_passport


def part2():
    # iterate over the passports array and check if they have the 7 required fields
    valid_passports_count = 0
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for passport in passports:
        if check_if_passport_is_valid(passport):
            valid_passports_count += 1
    print("Valid passports: %d" % valid_passports_count)


part2()