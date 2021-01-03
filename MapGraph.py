from queue import PriorityQueue

class MapGraph:
    def __init__(self):
        self.cities = dict()
        self.roads = []

    def heuristic(self, a, b):
        x_1, y_1 = a.x_pos, a.y_pos
        x_2, y_2 = b.x_pos, b.y_pos
        return abs(x_1 - x_2) + abs(y_1 - y_2)

    def a_star_search(self, start_city, end_city):
        frontier = PriorityQueue()
        came_from, cost_so_far = dict(), dict()

        frontier.put((0, start_city.name))
        came_from[start_city.name], cost_so_far[start_city.name] = None, 0
        while not frontier.empty():
            (_, current) = frontier.get()
            if self.cities[current] == end_city:
                path = []
                current_city = end_city.name
                while current_city is not None:
                    path.append(current_city)
                    current_city = came_from[current_city]
                path.reverse()
                return path, cost_so_far, True
            for next_city in self.cities[current].roads:
                if current == next_city.city2.name:
                    next_city_obj, next_city_name = next_city.city1, next_city.city1.name
                else:
                    next_city_obj, next_city_name = next_city.city2, next_city.city2.name
                new_cost = cost_so_far[current] + next_city.cost
                if next_city_name not in cost_so_far or new_cost < cost_so_far.get(next_city_name):
                    cost_so_far[next_city_name] = new_cost
                    priority = new_cost + self.heuristic(next_city_obj, end_city)
                    #print("from {} to {} priority {} heuristic {}".format(current, next_city_name, priority, self.heuristic(next_city_obj, end_city)))
                    frontier.put((priority, next_city_name))
                    came_from[next_city_name] = current
        return came_from, cost_so_far, False