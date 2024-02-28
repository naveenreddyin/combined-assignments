import sys, logging

from mars.plateau import Plateau
from mars.position import Position
from mars.rover import Drive


# start parsing
def parse(input_file):
    try:
        # open the file
        with open(input_file, "r") as _input_file:
            # get 1st line
            plateau_line = next(_input_file)
            # check for string else dont parse
            if is_string(plateau_line):
                # parse for semicolor
                _, plateau_coords = parse_semicolon(plateau_line)
                # space parsing for plateau
                x, y = parse_space(plateau_coords)
                # create plateau object
                plateau = Plateau(int(x), int(y))
            # iterate over next lines
            for line in _input_file:
                # get instruction
                rover_name, instruction = get_instruction(next(_input_file))

                if is_string(line) and instruction:
                    position_x, position_y, direction = get_positional_args(line)
                    position = Position(int(position_x), int(position_y))

                    rover = Drive(
                        plateau,
                        position,
                        direction.strip(),
                    )
                    rover.start(instruction.strip())
                    print(f"{rover_name}: {rover}")

    except (FileNotFoundError, TypeError) as err:
        sys.exit(err)


def get_instruction(line):
    if is_string(line):
        _rover_name, _instruction = parse_semicolon(line)
        return parse_space(_rover_name)[0], _instruction.strip()
    return None


def get_positional_args(line):
    if is_string(line):
        _, positions = parse_semicolon(line)
        return parse_space(positions)
    return None


def is_string(line):
    return isinstance(line, str)


def parse_space(line):
    return line.split(" ")


def parse_semicolon(line):
    return line.split(":")
