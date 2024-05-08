import sys
import os
import numpy as np
import matplotlib.pyplot as plt

MAP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '3-map/map.npy')

### START CODE HERE ###
# This code block is optional. You can define your utility function and class in this block if necessary.
class N():
    def __init__(self,x,y,parent=None) -> None:
        self.x =x
        self.y =y
        self.parent = parent
        if [x,y] == start_pos:
            self.parent = None
            self.g = 0
        else:
            self.g = self.parent.g + abs(self.x - self.parent.x) + abs(self.y - self.parent.y)
        self.h = abs(self.x - goal_pos[0]) + abs(self.y - goal_pos[1])
        self.f =self.h+self.g
        
class A:
    def __init__(self,map,start,goal) -> None:
        self.map =map
        self.start = start
        self.goal = goal
        self.openset = []
        self.closeset = []
        self.currentN = N(self.start[0],self.start[1])
        self.openset.append(self.currentN)
        
    def in_close(self,x,y):
        for i in self.closeset:
            if x == i.x and y==i.y:
                return True
        return False
    
    def in_open(self,x,y):
        for i in self.openset:
            if x == i.x and y==i.y:
                return True
        return False
    
    def iterate(self,x,y,parent):
        if (x < 0) or (x >= 120) or (y < 0) or (y >= 120):
            return
        if self.map[x][y] == 1:
            return
        if self.in_close(x,y):
            return
        if not self.in_open(x,y):
            n = N(x,y,parent)
            self.openset.append(n)
    
    def sel_min(self):
        min_cost = 1000000
        num =0
        for n in self.openset:
            if n.f <=min_cost:
                min_cost = n.f
                sel = num
            num +=1
        return sel
    
    def res(self,n):
        path = []
        while True:
            n=n.parent
            if n:
                path.insert(0,[n.x,n.y])
            if (n.x == self.currentN.x) and (n.y == self.currentN.y):
                return path
        
    def algorithm(self):
        while True:
            i = self.sel_min()
            n =self.openset[i]
            self.closeset.append(n)
            del self.openset[i]
            if(n.x == self.goal[0] and n.y == self.goal[1]):
                path = self.res(n)
                
                return path
            self.iterate(n.x-1,n.y,n)
            self.iterate(n.x,n.y-1,n)
            self.iterate(n.x+1,n.y,n)
            self.iterate(n.x,n.y+1,n)
        
        
        
###  END CODE HERE  ###


def A_star(world_map, start_pos, goal_pos):
    """
    Given map of the world, start position of the robot and the position of the goal, 
    plan a path from start position to the goal using A* algorithm.

    Arguments:
    world_map -- A 120*120 array indicating map, where 0 indicating traversable and 1 indicating obstacles.
    start_pos -- A 2D vector indicating the start position of the robot.
    goal_pos -- A 2D vector indicating the position of the goal.

    Return:
    path -- A N*2 array representing the planned path by A* algorithm.
    """

    ### START CODE HERE ###
    a = A(world_map,start_pos,goal_pos)
    path = a.algorithm()
    ###  END CODE HERE  ###
    return path





if __name__ == '__main__':

    # Get the map of the world representing in a 120*120 array, where 0 indicating traversable and 1 indicating obstacles.
    map = np.load(MAP_PATH)

    # Define goal position of the exploration
    goal_pos = [100, 100]

    # Define start position of the robot.
    start_pos = [10, 10]

    # Plan a path based on map from start position of the robot to the goal.
    path = A_star(map, start_pos, goal_pos)

    # Visualize the map and path.
    obstacles_x, obstacles_y = [], []
    for i in range(120):
        for j in range(120):
            if map[i][j] == 1:
                obstacles_x.append(i)
                obstacles_y.append(j)

    path_x, path_y = [], []
    for path_node in path:
        path_x.append(path_node[0])
        path_y.append(path_node[1])

    plt.plot(path_x, path_y, "-r")
    plt.plot(start_pos[0], start_pos[1], "xr")
    plt.plot(goal_pos[0], goal_pos[1], "xb")
    plt.plot(obstacles_x, obstacles_y, ".k")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

  
