import util

tree_map = util.load_txt_data("Day3/data1.txt")
TREE_MAP_HEIGHT = len(tree_map)
TREE_MAP_WIDTH = len(tree_map[0])


def part1():
    slope = [1, 3]
    start_coords = [0, 0] # top left corner (row, col)
    current_coords = start_coords
    encountered_trees = 0

    while current_coords[0] < TREE_MAP_HEIGHT: # while not at the bottom of the map
        # check if there is a tree at current_coords
        if tree_map[current_coords[0]][current_coords[1]] == "#":
            encountered_trees += 1

        # update the current position
        current_coords[0] += slope[0]
        current_coords[1] += slope[1]
        current_coords[1] %= TREE_MAP_WIDTH

    print("encountered %d trees" % encountered_trees)


#part1()

def check_encountered_trees(slope):
    start_coords = [0, 0] # top left corner (row, col)
    current_coords = start_coords
    encountered_trees = 0

    while current_coords[0] < TREE_MAP_HEIGHT: # while not at the bottom of the map
        # check if there is a tree at current_coords
        if tree_map[current_coords[0]][current_coords[1]] == "#":
            encountered_trees += 1

        # update the current position
        current_coords[0] += slope[0]
        current_coords[1] += slope[1]
        current_coords[1] %= TREE_MAP_WIDTH

    print("encountered %d trees with slope (%d, %d)" % (encountered_trees, slope[0], slope[1]))
    return encountered_trees


def part2():
    product_encountered_trees = 1
    for slope in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]:
        product_encountered_trees *= check_encountered_trees(slope)

    print("Product of encountered trees: %d" % product_encountered_trees)


part2()