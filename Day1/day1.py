import util


def part1():
    # load data
    data = util.load_txt_data("Day1/data1.txt")
    # transform to int:
    data = list(map(int, data))

    # simply iterate over array and check if the pair matches the criteria:
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] + data[j] == 2020:
                print("At %d and %d, the sum is 2020" % (i, j), data[i] * data[j])


def part2():
    # load data
    data = util.load_txt_data("Day1/data1.txt")
    # transform to int:
    data = list(map(int, data))

    # same logic as in part 1
    for i in range(len(data)):
        for j in range(i, len(data)):
            for k in range(j, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    print("At %d and %d and %d, the sum is 2020" % (i, j, k), data[i] * data[j] * data[k])

part1()
part2()
