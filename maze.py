from pyamaze import maze, agent

m = maze(8,8)
m.CreateMaze()
print(m.maze_map)
a = agent(m, footprints=True)
print(m.path)
m.tracePath({a: m.path})
m.run()