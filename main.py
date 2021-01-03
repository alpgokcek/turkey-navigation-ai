from tkinter import *
from tkinter import font  as tkfont
import math
import csv
from queue import PriorityQueue
from City import City
from Road import Road
from MapGraph import MapGraph

graph = MapGraph()

def draw_path():
    path, cost_so_far, is_path_found = graph.a_star_search(graph.cities[city_var1.get()], graph.cities[city_var2.get()])
    print("\n--------------------------------------------------------------------------------\npath:",path)
    print("cost_so_far{}\n--------------------------------------------------------------------------------\n".format(cost_so_far))
    canvas = Canvas(width=1492, height=771)
    canvas.create_image(0, 0, image=map_img, anchor=NW)

    for road in graph.roads:
        canvas.create_line(road.city1.x_pos+5, road.city1.y_pos+5, road.city2.x_pos+5, road.city2.y_pos+5)

    for city1,city2 in zip(path, path[1:]):
        canvas.create_line(graph.cities[city1].x_pos+5, graph.cities[city1].y_pos+5, graph.cities[city2].x_pos+5, graph.cities[city2].y_pos+5, width=6, fill='blue')

    for city in graph.cities.values():
        canvas.create_oval(city.x_pos, city.y_pos, city.x_pos + 10, city.y_pos + 10, fill="red")

    canvas.grid(row=1, column=0)

def calculate_distance(city1, city2):
    c1_x, c1_y, c2_x, c2_y = city1.x_pos, city1.y_pos, city2.x_pos, city2.y_pos
    return int(math.sqrt( math.pow(c2_x-c1_x, 2) + math.pow(c2_y-c1_y, 2) ) * 1.4)

with open('data/cities.csv') as csv_file:
    buffer = csv.reader(csv_file, delimiter=',')
    for line in buffer:
        graph.cities[line[0]] = City(line[0], int(line[1]), int(line[2]))

with open('data/roads.csv') as csv_file:
    buffer = csv.reader(csv_file, delimiter=',')
    for line in buffer:
        city1, city2 = line[0], line[1]
        cost = calculate_distance(graph.cities[city1], graph.cities[city2])
        road = Road(graph.cities[city1],graph.cities[city2],cost)
        graph.roads.append(road)
        graph.cities[city1].add_road(road)
        graph.cities[city2].add_road(road)

root = Tk()
frame = Frame(root, width="1492", height="900")
frame.grid(row=0, column=0)
root.title("Navigation on Turkey Map")

algorithm_font = tkfont.Font(family='Helvetica', size=30, weight="bold")
Label(frame, text="Navigation on Turkey Map", font=algorithm_font).grid(row=0, column=0)

map_img = PhotoImage(file='data/turkey-map.png')

canvas = Canvas(width=1492, height=771)
canvas.create_image(0, 0, image=map_img, anchor=NW)

for road in graph.roads:
    canvas.create_line(road.city1.x_pos+5, road.city1.y_pos+5, road.city2.x_pos+5, road.city2.y_pos+5)

for city in graph.cities.values():
    canvas.create_oval(city.x_pos, city.y_pos, city.x_pos + 10, city.y_pos + 10, fill="red")

canvas.grid(row=1, column=0)

nav_frame = Frame(root, width="1492", height="300")
nav_frame.grid(row=2, column=0)

'''
################
## Navigation ##
################
'''
OPTIONS = list(graph.cities.keys())

city_var1 = StringVar(nav_frame)
city_var1.set(OPTIONS[0])
city_var2 = StringVar(nav_frame)
city_var2.set(OPTIONS[0])

city_picker1 = OptionMenu(nav_frame, city_var1, *OPTIONS)
city_picker1.grid(row=0, column=0)

city_picker2 = OptionMenu(nav_frame, city_var2, *OPTIONS)
city_picker2.grid(row=0, column=1)

button = Button(nav_frame, text="OK", command=draw_path)
button.grid(row=0, column=2)

root.mainloop()