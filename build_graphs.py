from search_points import *
from colorama import init

init(autoreset=True)


def build_graph(x_graph, y_graph, name, red_points, blue_points):
    """Func for draw graph"""
    x_shift = (x_graph - 1) / 2  # 11
    y_shift = (y_graph - 1) / 2  # 5
    start_for_name_in_string = round((x_graph - len(name)) / 2)
    print(' ' * x_graph)
    '''should be variables for the space around the graph'''
    '''build graph'''
    y = y_graph
    while y > 0:
        x = 0
        result = ''
        letter_from_name = 0
        while x < x_graph:
            if y == y_graph and x < x_graph - start_for_name_in_string and x > start_for_name_in_string:
                result += name[0 + letter_from_name]  # print name
                letter_from_name += 1
                x += 1
            elif y == y_graph - 1 and x == x_shift:
                result += "^"
                x += 1
            elif y == y_graph - 2 and x == x_shift - 1:
                result += "Y"
                x += 1
            elif search_points(y - 2, x, red_points):  # print first point by x
                result += "\033[31m+\033[0m"
                x += 1
            elif search_points(y - 2, x, blue_points):  # print second point by y
                result += "\033[34m+\033[0m"
                x += 1
            elif y <= y_graph - 2 and x == x_shift:
                result += "|"
                x += 1
            elif y == y_shift and x == x_graph - 1:
                result += ">"
                x += 1
            elif y == y_shift:
                result += "-"
                x += 1
            elif y == y_shift - 1 and x == x_graph - 2:
                result += "X"
                x += 1
            else:
                result += ' '
                x += 1
        print(result)
        y -= 1
    print(' ' * x_graph)
