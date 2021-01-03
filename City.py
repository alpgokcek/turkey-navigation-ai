class City:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def __repr__(self):
        return "{}, x: {}, y: {}".format(self.name, self.x_pos, self.y_pos)
    def __str__(self):
        return "{}, x: {}, y: {}, roads:{}".format(self.name, self.x_pos, self.y_pos, self.roads)
