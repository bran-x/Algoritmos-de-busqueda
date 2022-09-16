from collections import deque

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
    
    def xy(self):
        return (self.x,self.y)

class DFS:
    def __init__(self, map, start_point, end_point, map_size):
        self.map = map
        self.start_point = Node(*start_point)
        self.end_point = Node(*end_point)
        self.map_size = map_size
        self.reset()

    def reset(self):
        r, c = self.map_size
        self.q = deque()
        self.q.append(self.start_point)
        self.visited = [[False for x in range(c+1)] for y in range(r+1)]
        self.visited[self.start_point.x][self.start_point.y] = True
        self.steps = 0

    def solve(self):
        path = []
        while 1:
            current_point = self.q.pop()
            path.append(current_point.xy())
            if not self.visited[current_point.x][current_point.y]:
                self.steps +=1
                self.visited[current_point.x][current_point.y] = True

            if current_point.xy() == self.end_point.xy():
                self.current_point = current_point
                print('Solved with BFS')
                print('Steps:', self.steps)
                break

            for direction, mag in self.map[current_point.xy()].items():
                if not mag: continue
                new_pos = self.apply_dir(current_point.xy(), direction)
                if not self.visited[new_pos[0]][new_pos[1]]:
                    self.q.append(Node(*new_pos, current_point))
        return path

    def get_path(self):
        current_point = self.current_point
        path = [current_point.xy()]
        while 1:
            current_point = current_point.parent
            if current_point is None: break
            path.append(current_point.xy())
        path.reverse()
        return path

    @staticmethod
    def apply_dir(pos, direction):
        x, y = pos
        if direction=='N': x-=1
        elif direction=='S': x+=1
        elif direction=='E': y+=1
        else: y-=1
        return (x,y)
    
