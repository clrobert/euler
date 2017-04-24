"""
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import pprint
pp = pprint.PrettyPrinter(indent=4)


class Node:
    data = {}

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def data(self):
        pp.pprint(self.data)

    def loc(self):
        print(self.row, self.column)

    def fill(self, left_node, right_node, up_node, down_node):
        self.data['left'] = left_node
        self.data['right'] = right_node
        self.data['up'] = up_node
        self.data['down'] = down_node

    def left(self):
        return self.data['left']

    def right(self):
        return self.data['right']

    def up(self):
        return self.data['up']

    def down(self):
        return self.data['down']


class Grid:
    def __init__(self, size):
        self.data = []
        self.size = size

        for row in range(0, size + 1):
            self.data.append([])
            for column in range(0, size + 1):
                self.data[row].append(Node(row, column))

    def data(self):
        return self.data

    def root(self):
        return self.data[0][0]

    def fill(self):
        for row in range(0, self.size + 1):
            for column in range(0, self.size + 1):
                left = self.nested_get(row, column - 1)
                right = self.nested_get(row, column + 1)
                up = self.nested_get(row - 1, column)
                down = self.nested_get(row + 1, column)
                node = self.data[row][column]
                node.fill(left, right, up, down)
                node.data()
                node.loc()
        return grid

    def display(self):
        for row in range(0, self.size + 1):
            for column in range(0, self.size + 1):
                node = self.data[row][column]
                node.data()
                node.loc()

    def nested_get(self, row, column):
        if row > self.size or row < 0 or column > self.size or column < 0:
            return None
        else:
            return self.data[row][column]

    def num_paths(self):
        pass

    def depth_traversal(self, grid):
        pass


size = 2
grid = Grid(size)
grid.fill()
grid.display()
root = grid.root()
print(root)
import pdb; pdb.set_trace()

"""
print(num_paths(6))
print(num_paths(20))
"""
