import util

# load the data:
seat_codes = util.load_txt_data("Day5/data1.txt")


def decode_seat_code(seat_code):
    # split row encoding from column encoding:
    row_code, column_code = seat_code[0:7], seat_code[7:10]

    # the codes are basically a binary number where B=0 and F=1, or L=0 and R=1
    row_code = row_code.replace("F", "0").replace("B", "1")
    column_code = column_code.replace("L", "0").replace("R", "1")

    # convert to integer and determine the id:
    return int(row_code, 2) * 8 + int(column_code, 2)


def part1():
    # map all seat codes from input to their id:
    seat_ids = list(map(decode_seat_code, seat_codes))

    # find the maximum seat id:
    print("highest seat id: %d" % max(seat_ids))
    print(decode_seat_code("BFFFBBFRRR"))


#part1()

def part2():
    # map all seat codes from input to their id:
    seat_ids = list(map(decode_seat_code, seat_codes))

    # sort the seat ids so that we can easily iterate over them and find a pair:
    seat_ids = list(sorted(seat_ids))

    # find a seat pair that are 2 apart:
    for i in range(len(seat_ids) - 1):
        if seat_ids[i+1] - seat_ids[i] == 2:
            print("These two seats are 2 seats apart: %d, %d, meaning your seat_id is %d" % (seat_ids[i], seat_ids[i+1], seat_ids[i]+1))

part2()