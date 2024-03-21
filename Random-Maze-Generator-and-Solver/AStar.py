import random
import tkinter as tk

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
        self.insertion_sort()

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("pop from an empty priority queue")

    def is_empty(self):
        return len(self.queue) == 0

    def insertion_sort(self):
        for i in range(1, len(self.queue)):
            key = self.queue[i]
            j = i - 1
            while j >= 0 and key < self.queue[j]:
                self.queue[j + 1] = self.queue[j]
                j -= 1
            self.queue[j + 1] = key
class AStarSearch:
    def __init__(self, maze):
        self.maze_object = maze
        self.visited_nodes = []
        self.path = []
        self.time_to_find_goal = 0
        self.a_star_search()

    def manhattan_distance(self, node):
        (x, y) = node
        (gx, gy) = self.maze_object.goal_node
        return abs(x - gx) + abs(y - gy)

    def is_valid_move(self, x, y):
        return (0 <= x < self.maze_object.width and 0 <= y < self.maze_object.height
                and self.maze_object.maze[y][x] != '#'and (x, y) not in self.visited_nodes)

    def process_neighbors(self, parent_x, parent_y, current_cost, path, priority_queue):
        for [child_x, child_y] in ([parent_x + 1, parent_y + 1], [parent_x + 1, parent_y], [parent_x + 1, parent_y - 1],
                                   [parent_x, parent_y + 1], [parent_x, parent_y - 1], [parent_x - 1, parent_y + 1],
                                   [parent_x - 1, parent_y], [parent_x - 1, parent_y - 1]):
            if self.is_valid_move(child_x, child_y):
                neighbor_cost = current_cost + 1 + self.manhattan_distance((child_x, child_y))
                priority_queue.push((neighbor_cost, child_x, child_y, current_cost + 1, path + [(child_x, child_y)]))

    def a_star_search(self):
        # Get start and goal node coordinates
        (start_x, start_y) = self.maze_object.start_node
        (goal_x, goal_y) = self.maze_object.goal_node

        # Calculate the Manhattan distance heuristic for the start node
        start_cost = self.manhattan_distance(self.maze_object.start_node)
        # Create the initial node for the A* search
        start_node = (start_cost, start_x, start_y, 1, [self.maze_object.start_node])
        # Create a priority queue and push the start node
        priority_queue = PriorityQueue()
        priority_queue.push(start_node)

        # A* search loop
        while not priority_queue.is_empty():
            _, x, y, current_cost, path = priority_queue.pop()
            # Check if the current node is not visited
            if (x, y) not in self.visited_nodes:
                # Mark the current node as visited
                self.visited_nodes.append((x, y))
                # Check if the goal node is reached
                if x == goal_x and y == goal_y:
                    # Store the path, visited nodes, and relevant information
                    self.path = path
                    self.time_to_find_goal = len(self.visited_nodes)
                    # Display relevant information
                    print('Goal found')
                    print('A star Visited list: ', self.visited_nodes)
                    print('A Star visited list length: ', len(self.visited_nodes))
                    print('A star Shortest path: ', self.path)
                    print('A star shortest path length: ', len(self.path))
                    print('Total time: ', self.time_to_find_goal)
                    # Break out of the loop as the goal is found
                    break
                # Process neighbors and update the priority queue
                self.process_neighbors(x, y, current_cost, path, priority_queue)
            else:
                # If the node is already visited, continue to the next iteration
                continue
        # Return the visited nodes, time to find the goal, and the final path
        return self.visited_nodes, self.time_to_find_goal, self.path

    def visualize_Astar(self,window):
        canvas = tk.Canvas(window, width=6 * 100, height=6 * 100)
        canvas.pack(side=tk.RIGHT)

        label_astar = tk.Label(window, text="A* Visualization")
        label_astar.pack(side=tk.RIGHT)
        # mark starting node with limegreen, goal with royal blue, and barriers with black
        colors = {'#': 'black', 'S': 'limegreen', 'G': 'royalblue'}
        for i in self.visited_nodes:
            if i != self.maze_object.start_node and i != self.maze_object.goal_node:
                colors[f"{i[0]},{i[1]}"] = 'skyblue' # Mark visited nodes with sky blue color

        for i in self.path:
            if i != self.maze_object.start_node and i != self.maze_object.goal_node:
                colors[f"{i[0]},{i[1]}"] = 'darkslategray' # Mark the final path with darkslategray color

        for y in range(self.maze_object.height):
            for x in range(self.maze_object.width):
                cell_type = self.maze_object.maze[y][x]
                color = colors.get(cell_type)
                canvas.create_rectangle(x * 100, y * 100, (x + 1) * 100, (y + 1) * 100, fill=color)
                text = str(cell_type)
                canvas.create_text((x + 0.5) * 100, (y + 0.5) * 100, text=text, fill='black')


