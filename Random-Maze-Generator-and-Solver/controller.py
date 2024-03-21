import Maze as maze
import tkinter as tk
import DepthFirstSearch as DFS
import AStar as Astar

# Set up a tkinter window to visualize maze
window = tk.Tk()
window.title("DFS and A* Algorithms Visualization")
print()
print('**Maze Visualizations Navigation guide**')
print('Green - Start Node')
print('Blue - Goal node')
print('Black - Barriers')
print('DFS==============')
print('Pink - Final Path')
print('Light blue - Visited nodes that are not a part of the Final path')
print('A*===============')
print('Dark blue - Shortest path')
print('Light blue - Visited nodes that are not a part of the shortest path')
print()
# Initializes a 6 X 6 maze
maze1 = maze.Maze(6, 6)
# Sets the start, goal and barrier nodes
maze1.set_start()
maze1.set_goal()
maze1.set_barriers()
print()
print('DFS============================================================================================================')
print()
# Performs dfs search on above implemented maze
dfs1 = DFS.DepthFirstSearch(maze1)
# Visualizes dfs search process on above created tkinter window
dfs1.visualize_dfs(window)
print()
print('Astar==========================================================================================================')
print()
# Performs A* search on above implemented maze
astar = Astar.AStarSearch(maze1)
# Visualizes A* search process on above created tkinter window
astar.visualize_Astar(window)

window.mainloop()