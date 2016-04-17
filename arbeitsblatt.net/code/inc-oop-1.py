class Punkt:
    """Eine Punkt-Klasse"""

    # nicht gut, siehe https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
    class_constants = [ 3.141 ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.constants = [ 3.141 ]

    def print(self):
        print("Punkt ({}, {}) and class_constants = {}, constants = {}".format(
            self.x, self.y, self.class_constants, self.constants))


p1 = Punkt(1, 2)
p2 = Punkt(3, 4)

p1.print()
# Punkt (1, 2) and class_constants = [3.141], constants = [3.141]

p2.print()
# Punkt (3, 4) and class_constants = [3.141], constants = [3.141]

p1.x = 5
p1.class_constants.append(10)
p1.constants.append(20)

p1.print()
# Punkt (5, 2) and class_constants = [3.141, 10], constants = [3.141, 20]

p2.print()
# Punkt (3, 4) and class_constants = [3.141, 10], constants = [3.141]