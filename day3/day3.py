import sys
from math import prod


def get_adjacent_coords_set(coord_tuple):
    result_coords = set()
    for x in range(coord_tuple[0] - 1, coord_tuple[0] + 2):
        for y in range(coord_tuple[1] - 1, coord_tuple[1] + 2):
            if x >= 0 and y >= 0:
                result_coords.add((x,y))
    return result_coords


def filter_invalid_coords(grid, coords):
    filtered_coords = set()
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    for coord in coords:
        if coord[0] <= max_x and coord[1] <= max_y:
            filtered_coords.add(coord)
    return filtered_coords


def get_number_coords_dict(grid):
    number_coords_dict = {}
    num_chars = []
    adjacent_coords = set()
    for x,row in enumerate(grid):
        for y,c in enumerate(row):
            if c in ['1','2','3','4','5','6','7','8','9','0']:
                num_chars.append(c)
                adjacent_coords = adjacent_coords.union(get_adjacent_coords_set((x,y)))
            else:
                if len(num_chars) > 0:
                    number_coords_dict[((x,y),int(''.join(num_chars)))] = filter_invalid_coords(grid,adjacent_coords)
                    num_chars = []
                    adjacent_coords = set()
    return number_coords_dict
            


def part2_entry(input_filename):
    grid = [ line.strip() for line in open(input_filename, 'r') ]
    number_coords_dict = get_number_coords_dict(grid)
    gear_ratios = []
    for x,row in enumerate(grid):
        for y,c in enumerate(row):
            if c == '*':
                adjacent_parts = []
                for num,coords in number_coords_dict.items():
                    if (x,y) in coords:
                        adjacent_parts.append(num[1])
                if len(adjacent_parts) == 2:
                    gear_ratios.append(prod(adjacent_parts))
    print(f"Part2: {sum(gear_ratios)}")


def part1_entry(input_filename):
    grid = [ line.strip() for line in open(input_filename, 'r') ]
    numbers_adjacent_to_symbol = []
    number_coords_dict = get_number_coords_dict(grid)
    #print(number_coords_dict.keys())
    for num,coords in number_coords_dict.items():
        for coord in coords:
            if grid[coord[0]][coord[1]] not in ['1','2','3','4','5','6','7','8','9','0','.']:
                numbers_adjacent_to_symbol.append(num[1])
                break
    
    result = sum(numbers_adjacent_to_symbol)
    
    print(f"Part1: {result}")


def main():
    if len(sys.argv) < 2:
        sys.exit("missing input")
    infile = sys.argv[1]
    part1_entry(infile)
    part2_entry(infile)


if __name__ == '__main__':
    main()