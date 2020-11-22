from tkinter import *
from tkinter import font  as tkfont

import csv

class City:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def __repr__(self):
        return "{}, x: {}, y: {}, roads:{}".format(self.name, self.x_pos, self.y_pos, self.roads)
    def __str__(self):
        return "{}, x: {}, y: {}, roads:{}".format(self.name, self.x_pos, self.y_pos, self.roads)

class Road:
    def __init__(self, city1, city2, cost):
        self.city1 = city1
        self.city2 = city2
        self.cost = cost

    def __repr__(self):
        return "{}, x: {}, y: {}".format(self.city1, self.city2, self.cost)
    def __str__(self):
        return "{}, x: {}, y: {}".format(self.city1, self.city2, self.cost)

cities = dict()

with open('cities.csv') as csv_file:
    buffer = csv.reader(csv_file, delimiter=',')
    for line in buffer:
        cities[line[0]] = City(line[0], int(line[1]), int(line[2]))
roads = []

with open('roads.csv') as csv_file:
    buffer = csv.reader(csv_file, delimiter=',')
    for line in buffer:
        city1, city2, cost = line[0], line[1], 0
        road = Road(city1,city2,cost)
        roads.append(road)
        cities[city1].add_road(road)
        cities[city2].add_road(road)

print(cities['Istanbul'])
'''

temp_str = ""
with open('neighbors.csv') as csv_file:
    buffer = csv.reader(csv_file, delimiter=',')
    for line in buffer:
        temp_arr = line[1:]
        temp_arr.sort()
        for i in temp_arr:
            temp_arr1 = [line[0], i]
            temp_arr1.sort()
            temp_str += "{},{}\n".format(temp_arr1[0], temp_arr1[1])


print(temp_str)
'''

root = Tk()
frame = Frame(root, width="1492", height="900")
frame.grid(row=0, column=0)
root.title("Navigation on Turkey Map")

algorithm_font = tkfont.Font(family='Helvetica', size=30, weight="bold")
Label(frame, text="Navigation on Turkey Map", font=algorithm_font).grid(row=0, column=0)
# create the canvas, size in pixels
canvas = Canvas(width=1492, height=771)

# load the .gif image file
map_img = PhotoImage(file='turkey-map.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(0, 0, image=map_img, anchor=NW)
for city in cities.values():
    canvas.create_oval(city.x_pos, city.y_pos, city.x_pos + 10, city.y_pos + 10, fill="red")
# pack the canvas into a frame/form

canvas.grid(row=1, column=0)



root.mainloop()