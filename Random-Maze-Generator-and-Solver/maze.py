import random

# A method to create a Maze using a 2D array
def create_maze(width, height):
    grid = []
    for k in range(height):
        row = []
        for i in range(width):
            # The coordinates of a node is stored in the cell of the 2D representing that node
            row.append(str(i) + ',' + str(k))
        grid.append(row)
    return grid


class Maze:
    def __init__(self, width, height):
        # Initialize variables for maze dimensions
        self.width = width
        self.height = height
        # Create a maze grid using the create_maze function
        self.maze = create_maze(width, height)
        # Initialize variables for start and goal nodes
        self.start_node = None
        self.goal_node = None
        self.start_node_x, self.start_node_y, self.goal_node_x, self.goal_node_y = 0, 0, 0, 0
        # Initialize a list to store barrier nodes
        self.barrier_nodes = []
    def set_start(self):
        # Generate random coordinates for the starting node
        self.start_node_x = random.randint(0, 1)
        self.start_node_y = random.randint(0, 5)
        # Save the randomly created nodes in a variable
        self.start_node = (self.start_node_x, self.start_node_y)
        # Mark the starting node in the maze
        self.maze[self.start_node_y][self.start_node_x] = 'S'
        print('Your starting node coordinates are- ', self.start_node)

    def set_goal(self):
        # Generate random coordinates for the goal node
        while True:
            self.goal_node_x = random.randint(4, 5)
            self.goal_node_y = random.randint(0, 5)
            # Ensure the goal node is not the same as the starting node
            if (self.goal_node_x, self.goal_node_y != self.start_node_x, self.start_node_y):
                self.goal_node = (self.goal_node_x, self.goal_node_y)
                # Mark the goal node in the maze
                self.maze[self.goal_node_y][self.goal_node_x] = 'G'
                print('Your goal node coordinates-', self.goal_node)
                break

    def set_barriers(self):
        # Check if start and goal nodes are set before placing barriers
        if self.start_node is not None and self.goal_node is not None:
            barrier_count = 0
            # Generate barrier nodes and mark them in the maze
            while barrier_count < 4:
                barrier_node_y = random.randint(0, 5)
                barrier_node_x = random.randint(0, 5)
                # Ensure barrier nodes are not the same as start or goal nodes
                if (barrier_node_x == self.goal_node_x and barrier_node_y == self.goal_node_y) or (
                        barrier_node_x == self.start_node_x and barrier_node_y == self.start_node_y):
                    continue
                # Add barrier node to the list and mark it in the maze
                if (barrier_node_x, barrier_node_y) not in self.barrier_nodes:
                    self.barrier_nodes.append((barrier_node_x, barrier_node_y))
                    self.maze[barrier_node_y][barrier_node_x] = '#'
                    barrier_count += 1
            print('Your barrier node coordinates-', self.barrier_nodes)
        else:
            print('Set starting and goal nodes first')
            pass

