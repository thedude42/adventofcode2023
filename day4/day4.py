import sys


class ScratchCard:
    '''class representing the day4 AoC Scratch Card input'''

    def __init__(self, input_line) -> None:
        card_id, numbers = input_line.split(':')
        self.id = int(card_id.split()[1])
        self.winners = [ int(x) for x in numbers.split('|')[0].split() ]
        self.numbers = [ int(x) for x in numbers.split('|')[1].split() ]
    

    @property
    def matches(self) -> int:
        return len(set(self.winners).intersection(set(self.numbers)))
    

    @property
    def points(self) -> int:
        return int(2 ** (self.matches - 1))
    

    def get_copies_list(self):
        return [ n for n in range(self.id + 1, self.id + self.matches + 1 )]


    

def part2_entry(input_filename):
    lines = [ l for l in open(input_filename, 'r') ]
    cards = [ ScratchCard(l) for l in lines ]
    copies = { c.id:1 for c in cards }
    for card in cards:
        if card.matches:
            for i in card.get_copies_list():
                copies[i] += copies[card.id]
    print(f"Part2: {sum([copies[card.id] for card in cards ])}")


def part1_entry(input_filename):
    lines = [ l for l in open(input_filename, 'r') ]
    cards = [ ScratchCard(l) for l in lines ]
    print(f"Part1: {sum([ card.points for card in cards ])}")


def main():
    if len(sys.argv) < 2:
        sys.exit("missing input")
    infile = sys.argv[1]
    part1_entry(infile)
    part2_entry(infile)


if __name__ == '__main__':
    main()