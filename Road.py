import math

class Road:
    def __init__(self, city1, city2, cost):
        self.city1 = city1
        self.city2 = city2
        self.cost = cost

    def __repr__(self):
        return "(city: {}, cost: {})".format(self.city2.name, self.cost)
    def __str__(self):
        return "city1:{}, city2: {}, cost: {}".format(self.city1, self.city2, self.cost)
    def __gt__(self, road):
        return self.cost < road.cost