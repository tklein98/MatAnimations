class Letters:

    def __init__(self, letter, starting_coordinate):
        self.letter = letter
        self.coordinates = []
        self.starting_coordinate = starting_coordinate

    def add_coordinates(self, coordinate):
        self.coordinates.append(coordinate)

d = Letters('Fido')
e = Letters('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
['roll over']
e.tricks
['play dead']
