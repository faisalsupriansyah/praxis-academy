import numpy as np

arr_a = np.array([3, 6, 9])
arr_b = arr_a/3 # Performing vectorized (element-wise) operations 
print(arr_b)

arr_ones = np.ones(4)
print(arr_ones)

multi_arr_ones = np.ones((3,4)) # Creating 2D array with 3 rows and 4 columns
print(multi_arr_ones)

stack = [1,2,3,4,5] 
stack.append(6) # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 (Top)
print(stack)

stack.pop() # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
stack.pop() # Bottom -> 1 -> 2 -> 3 -> 4 (Top)
print(stack)

graph = { "a" : ["c", "d"],
          "b" : ["d", "e"],
          "c" : ["a", "e"],
          "d" : ["a", "b"],
          "e" : ["b", "c"]
        }

def define_edges(graph):
    edges = []
    for vertices in graph:
        for neighbour in graph[vertices]:
            edges.append((vertices, neighbour))
    return edges

print(define_edges(graph))

class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left  = left
        self.right = right

    def __str__(self):
        return (str(self.info) + ', Left child: ' + str(self.left) + ', Right child: ' + str(self.right))

tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
print(tree)