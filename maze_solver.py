from pyamaze import maze, agent, COLOR
from bfs import BFS
from dfs import DFS
from a_asterisk import A

maze_size = (8,8)
start_point = (8,8)
end_point = (1,1)

m = maze(*maze_size)
m.CreateMaze()

# Solucion BFS
# solver1 = BFS(m.maze_map, start_point, end_point, maze_size)

# Solucion DFS
#solver1 = DFS(m.maze_map, start_point, end_point, maze_size)

# Solucion A*
solver1 = A(m.maze_map, start_point, end_point, maze_size)

path = solver1.solve()
path_sol = solver1.get_path()
a = agent(m, footprints=True)
a2 = agent(m, footprints=True, filled=True, color=COLOR.red)
m.tracePath({a: path})
m.tracePath({a2: path_sol})
m.run()