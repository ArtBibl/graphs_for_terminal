from build_graphs import *
import math

'''base data for build graph  '''
name_of_graph = "My graph "

''' For mathematical graphs  '''
''' Important!!! Size MUST NOT be EVEN! And X must be doubled by Y! '''
length_graph = 47
height_graph = 23
'''points = [1, 1] -> 
get x: 1, 2, y: 1, 1 '''


def red_line(size_x, step_x, x) -> list:
    points = []
    while size_x > 0:
        try:
            # y = (8 + 3 * x) / 2  # <- formula of graph
            # y = 12 / x           # <- formula of graph
            # y = abs(x) ** 0.5    # <- formula of graph
            y = x ** 2 - 7     # <- formula of graph
        except ZeroDivisionError:
            y = 0
        y = y + 9  # I don`t now why nine :( It`s not easy find zero.
        points.append(round(y))
        size_x -= 1
        x += step_x
    return points


def blue_line(size_x, step_x, x) -> list:
    points = []
    while size_x > 0:
        try:
            # y = x ** 3    # <- formula of graph
            # y = x / 1.5   # <- formula of graph
            y = math.atan(x) * 4  # <- formula of graph
            # y = -x**2 * x   # <- formula of graph
        except ZeroDivisionError:
            y = 0
        y = y + 9  # I don`t now why nine :( It`s not easy find zero.
        points.append(round(y))
        size_x -= 1
        x += step_x
    return points


'''Console with settings 8x16 pixels for one symbol -> coefficient 0.5 for step_x '''
first_points = red_line(length_graph, 0.5, (height_graph / 2) * -1)
second_points = blue_line(length_graph, 0.5, (height_graph / 2) * -1)

build_graph(length_graph, height_graph, name_of_graph, first_points, second_points)

print("\033[31mRed points: y = x^2 - 7\033[0m\n")
print("\033[34mBlue points: y = atan(x) * 4\033[0m\n")
# print("Red points: ", first_points)
# print("Blue points: ", second_points)
