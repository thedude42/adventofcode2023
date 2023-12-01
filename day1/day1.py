import sys

num_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def try_num_string(a_slice):
    #print(f"trying slice: {a_slice}")
    val = num_map.get(a_slice)
    #print(f"found value {val}")
    return val


def get_line_values_p2(line):
    #print(f"Starting for line '{line}'")
    first, last = None, None
    for i, c in enumerate(line):
        try:
            if first is None:
                first = int(c)
                last = first
            else:
                last = int(c)
        except:
            for n in [3,4,5]:
                if first is None:
                    first = try_num_string(line[i:i+n])
                    if first is not None:
                        break
                else:
                    maybelast = try_num_string(line[i:i+n])
                    if maybelast is not None:
                        last = maybelast
                        break
    #print(first, last)
    result = (first * 10) + last
    return result
            


def get_line_value(line):
    first, last = None, None
    for c in line:
        try:
            first = int(c)
            break
        except:
            pass
    for c in line[::-1]:
        try:
            last = int(c)
            break
        except:
            pass
    # this dumb shit is to deal with cases whenre part 2 input isn't valid part1 input
    if first is None and last is None:
        return 0
    result = (first * 10) + last
    return result


def p1_get_calibration_value(lines):
    return sum([get_line_value(l) for l in lines])


def p2_get_calibration_value(lines):
    return sum(get_line_values_p2(l) for l in lines)

def main():
    if len(sys.argv) < 2:
        sys.exit("missing input")
    infile = sys.argv[1]
    inlines = [ l for l in open(infile, 'r') ]
    print(f"Part1: {p1_get_calibration_value(inlines)}")
    print(f"Part2: {p2_get_calibration_value(inlines)}")


if __name__ == '__main__':
    main()