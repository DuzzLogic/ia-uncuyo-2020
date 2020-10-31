import heapq
import numpy as np
import random

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f


#Devuelve el path desde el nodo inicial al objetivo
def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(maze, start, end):
    # Se crea el nodo inicial y el objetivo
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    # Movimientos validos: izquierda, derecha, arriba y abajo
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)

    # Hasta agotar posibilidades o encontrar el nodo objetivo
    while len(open_list) > 0:

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []

        for new_position in adjacent_squares:  # Adjacent squares

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + (((child.position[0] - child.parent.position[0]) ** 2) + ((child.position[1] - child.parent.position[1]) ** 2))**0.5
            child.h = (((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))**0.5
            child.f = child.g + child.h

            # Child is already in the open list
            index = None
            for i in range(0, len(open_list)):
                if child.position == open_list[i].position:
                    index = i
                    break

            if index:
                if child.g >= open_list[index].g:
                    continue
                else:
                    open_list[index] = open_list[-1]
                    open_list.pop()
                    if index < len(open_list):
                        heapq._siftup(open_list, index)
                        heapq._siftdown(open_list, 0, index)

            # Add the child to the open list
            heapq.heappush(open_list, child)

    return None


# Create maze
def create_maze(n_obstacle):
    x=100
    y=100
    m = np.zeros((x, y))

    i = 0
    # Randomly place obstacles
    while (i < n_obstacle):
        slotX = random.randint(0, x-1)
        slotY = random.randint(0, y-1)
        if (m[slotX][slotY] == 0):
            m[slotX][slotY] = 1
            i = i + 1

    return m


def printMaze(maze):
    for row in maze:
        line = []
        for col in row:
            if col == 1: #Obstaculos
                line.append("\u2588")
            elif col == 0: #Ambiente
                line.append(" ")
            elif col == 2: #Camino start-end
                line.append(".")
            elif col == 3: #Nodo inicial y nodo final
                line.append("@")
        print("".join(line))

def main(X_init,Y_init,n_obstacle,X_end,Y_end):
    # Se crea el ambiente con los obstaculos
    maze = create_maze(n_obstacle)
 
    # Se define punto de inicio y objetivo
    start = (X_init, Y_init)
    end = (X_end, Y_end)

    # Se marca con un 3 el punto inicial y el final para
    # poder graficar
    maze[X_init][Y_init] = 3
    maze[X_end][Y_end] = 3

    printMaze(maze)
    print()
    print("-----------------------------------")
    print()

    # Se vuelve a valores iniciales
    maze[X_init][Y_init] = 0
    maze[X_end][Y_end] = 0

    # A* 
    path = astar(maze, start, end)

    if path == None: #No hay camino posible
        print("No hay caminos posibles")
    else:
        # Se indica con un 2 el camino para poder graficar
        for step in path:
            maze[step[0]][step[1]] = 2

        # Se marca con un 3 el punto inicial y el final para
        # poder graficar
        maze[X_init][Y_init] = 3
        maze[X_end][Y_end] = 3

        printMaze(maze)
        print(path)


main(2,2,3000,90,65)
