from .position import Position


class Drive:

    directions = {"N": 1, "E": 2, "S": 3, "W": 4}

    direction = directions["N"]

    def __init__(self, plateau, position, direction):
        self.plateau = plateau
        self.position = position
        self.direction = self.directions.get(direction)

    @property
    def current_position(self):
        directions = list(self.directions.keys())

        try:
            direction = directions[self.direction - 1]
        except IndexError:
            direction = "N"
            print("Path is wrong")

        return f"{self.position.x} {self.position.y} {direction}"

    def start(self, commands):
        commands = commands.replace("LEFT", "L")
        for command in commands:
            self.run_command(command)

    def run_command(self, command):
        if command in ["L", "R"]:
            self.turn(command)
        elif "M" == command:
            if not self.move():
                print("Not compatible coordinates")
        else:
            print("You have issued a wrong command")

    def move(self):
        if not self.plateau.can_move(self.position):
            return False
        if self.directions["N"] == self.direction:
            self.position.y += 1
        elif self.directions["E"] == self.direction:
            self.position.x += 1
        elif self.directions["S"] == self.direction:
            self.position.y -= 1
        elif self.directions["W"] == self.direction:
            self.position.x -= 1

        return True

    def turn(self, command):
        if command == "L":
            if (self.direction - 1) < self.directions["N"]:
                self.direction = self.directions["W"]
            else:
                self.direction -= 1
        elif command == "R":
            if (self.direction + 1) > self.directions["W"]:
                self.direction = self.directions["N"]
            else:
                self.direction += 1

    def __str__(self):
        return self.current_position
