"""Searching points for drawing graph"""
'''At here should be additional logic for scaling graph, but maybe later...'''


def search_points(y, x, points) -> True:
    try:
        if y == points[x]:
            return True
        return False
    except IndexError:
        pass

# y = 1
# x = 12
# points = [12, 3, 4, 5, 6, 0, 7, 7, 3, 6, 11, 12]
# print(search_points(1, 12, points))
