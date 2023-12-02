import sys
from collections import defaultdict
from math import prod



def parse_games_record(filename):
    lines = [ l for l in open(filename, 'r') ]
    games_record = defaultdict(list)
    for game in lines:
        key, pulls = game.split(':')
        for pull in [ p.strip() for p in pulls.split(';') ]:
            games_record[key].append({cubes.split()[1]:int(cubes.split()[0]) for cubes in  [ c.strip() for c in pull.split(',') ] })
    return games_record


def test_possible_game(reference, a_game):
    for k,v in a_game.items():
        if reference[k] < v:
            return False
    return True


def part1_entry(input_filename):
    reference_bag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    games = parse_games_record(input_filename)
    print(f"Part1: {sum([ int(game.split()[1]) for game,pulls in games.items() if all([ test_possible_game(reference_bag, pull) for pull in pulls]) ])}")


def find_minimum_cubes(games):
    result = {}
    for game,pulls in games.items():
        result[game] = {'red': 0,'green': 0,'blue': 0}
        for pull in pulls:
            for color,cubes in pull.items():
                if result[game][color] < cubes:
                    result[game][color] = cubes
    return result
            

def part2_entry(input_filename):
    games = parse_games_record(input_filename)
    min_bag = find_minimum_cubes(games)
    print(f"Part2: {sum([ prod(v.values()) for v in min_bag.values() ])}")


def main():
    if len(sys.argv) < 2:
        sys.exit("missing input")
    infile = sys.argv[1]
    part1_entry(infile)
    part2_entry(infile)


if __name__ == '__main__':
    main()