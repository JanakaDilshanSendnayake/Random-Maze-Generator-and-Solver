import random
import tkinter as tk

# ... (your Maze class here)

class DepthFirstSearch:

    def __init__(self, maze):
        self.maze = maze
        self.visited_list = []  # List to keep track of visited nodes
        self.stack = []   # Stack to store nodes for DFS traversal
        self.final_path = []  # List to store the final path
        self.stack.append((self.maze.start_node, []))  # Appending starting node with to the stack at the beginning
        self.final_path.append(self.maze.start_node) # Appending starting node with to the final path at the beginning
        self.time_to_find_goal = 0
        self.traverse()   # Perform DFS traversal


    def is_valid_move(self, x, y):
        # Check if a move to the specified coordinates is valid
        return 0 <= x < self.maze.width and 0 <= y < self.maze.height and (x, y) not in self.maze.barrier_nodes

    def get_children(self, parent_x, parent_y, current_path):
        # Get valid child nodes for the given parent node
        for [child_x, child_y] in ([parent_x+1, parent_y+1], [parent_x+1, parent_y], [parent_x+1, parent_y-1],
                                   [parent_x, parent_y+1], [parent_x, parent_y-1], [parent_x-1, parent_y+1],
                                   [parent_x-1, parent_y], [parent_x-1, parent_y-1]):
            if 0 <= child_y < self.maze.width and 0 <= child_x < self.maze.height:
                if (child_x, child_y) in self.maze.barrier_nodes:
                    pass
                else:
                    self.stack.append(((child_x, child_y), current_path + [(child_x, child_y)]))  # Add valid child nodes to the stack

    def traverse(self):
        # Perform DFS traversal until the goal node is reached or all nodes are visited
        while self.stack:
            current_node, current_path = self.stack.pop()
            if current_node not in self.visited_list:
                self.visited_list.append(current_node)
                if current_node == self.maze.goal_node:
                    print('Goal found')
                    self.final_path += current_path  # Store the final path
                    self.time_to_find_goal = len(self.visited_list)
                    # Display relevant information
                    print('DFS Visited List:', self.visited_list)
                    print('DFS Visited List length: ', len(self.visited_list))
                    print('DFS Final path:', self.final_path)
                    print('DFS Final path length: ', len(self.final_path))
                    print('Total Time: ', self.time_to_find_goal)
                    break
                else:
                    self.get_children(current_node[0], current_node[1], current_path)
            else:
                continue

    def visualize_dfs(self, window):
        # Visualize the DFS process using Tkinter

        label_dfs = tk.Label(window, text="DFS Visualization")
        label_dfs.pack(side=tk.LEFT)

        canvas = tk.Canvas(window, width=6 * 100, height=6 * 100)
        canvas.pack(side=tk.LEFT)
        # mark starting node with limegreen, goal with royal blue, and barriers with black
        colors = {'#': 'black', 'S': 'limegreen', 'G': 'royalblue'}
        for i in self.visited_list:
            if (i != self.maze.start_node) and i != self.maze.goal_node and i not in self.final_path:
                colors[f"{i[0]},{i[1]}"] = 'skyblue'  # Mark visited nodes with sky blue color
        for i in self.final_path:
            colors[f"{i[0]},{i[1]}"] = 'pink' # Mark the final path with pink color
        # Draw rectangles and text on the canvas to represent the maze
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                cell_type = self.maze.maze[y][x]
                color = colors.get(cell_type)
                canvas.create_rectangle(x * 100, y * 100, (x + 1) * 100, (y + 1) * 100, fill=color)
                text = str(cell_type)
                canvas.create_text((x + 0.5) * 100, (y + 0.5) * 100, text=text, fill='black')

