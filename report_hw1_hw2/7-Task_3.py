import sys
import os
import numpy as np
import matplotlib.pyplot as plt

MAP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '3-map/map.npy')


### START CODE HERE ###
# This code block is optional. You can define your utility function and class in this block if necessary.
import math
class N():
    def __init__(self,x,y,parent=None) -> None:
        self.x =x
        self.y =y
        self.parent = parent
        self.s = 0
        if [x,y] == start_pos:
            self.parent = None
            self.g = 0
        else:
            self.x_change = self.x - self.parent.x
            self.y_change = self.y - self.parent.y
            if  abs(self.x_change) + abs(self.y_change) == 1:
                self.g = self.parent.g + 1
            else:
                self.g = self.parent.g +math.sqrt(2)
            if [self.parent.x,self.parent.y] != start_pos and abs(self.x_change-self.parent.x_change)+abs(self.y_change-self.parent.y_change)>1:
                    self.s=1
        self.h = abs(self.x - goal_pos[0]) + abs(self.y - goal_pos[1])
        
        
        self.f = self.g + self.h + self.s
        
class A:
    def __init__(self,map,start,goal) -> None:
        self.map =map
        
        self.gen_obstacle_map()
        self.gen_obstacle_map()
        self.gen_obstacle_map()
        
        self.start = start
        self.goal = goal
        self.openset = []
        self.closeset = []
        self.currentN = N(self.start[0],self.start[1])
        self.openset.append(self.currentN)
        
    def gen_obstacle_map(self):
        obstacle_map = self.map.copy()
        for i in range(1, 119):
            for j in range(1, 119):
                if self.map[i][j] + self.map[i - 1][j] + \
                   self.map[i+1][j] + self.map[i][j-1] + \
                   self.map[i-1][j-1] + self.map[i+1][j-1] + \
                   self.map[i][j+1] + self.map[i-1][j+1] + \
                   self.map[i+1][j+1] > 0:
                    obstacle_map[i][j] = 1
        self.map = obstacle_map
        
        
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
    
    def bernstein_poly(self,i, n, t):
        return np.math.comb(n, i) * (1 - t)**(n - i) * t**i

    def bezier_curve(self,control_points):
        num_points = 100
        t = np.linspace(0, 1, num_points)
        n = len(control_points) - 1
        curve_points = []
        for i in range(num_points):
            x = sum(self.bernstein_poly(j, n, t[i]) * control_points[j][0] for j in range(n + 1))
            y = sum(self.bernstein_poly(j, n, t[i]) * control_points[j][1] for j in range(n + 1))
            curve_points.append((x, y))

        return curve_points
    
    def res(self,n):
        path = []
        while True:
            n=n.parent
            if n:
                path.insert(0,[n.x,n.y])
            if (n.x == self.currentN.x) and (n.y == self.currentN.y):
                return self.bezier_curve(path)
                #return path
        
    def algorithm(self):
        while True:
            i = self.sel_min()
            n =self.openset[i]
            self.closeset.append(n)
            del self.openset[i]
            if(n.x == self.goal[0] and n.y == self.goal[1]):
                path = self.res(n)
                
                return path
            self.iterate(n.x+1,n.y+1,n)
            self.iterate(n.x-1,n.y+1,n)
            self.iterate(n.x+1,n.y-1,n)
            self.iterate(n.x-1,n.y-1,n)
            self.iterate(n.x-1,n.y,n)
            self.iterate(n.x,n.y-1,n)
            self.iterate(n.x+1,n.y,n)
            self.iterate(n.x,n.y+1,n)


###  END CODE HERE  ###



def self_driving_path_planner(world_map, start_pos, goal_pos):
    """
    Given map of the world, start position of the robot and the position of the goal, 
    plan a path from start position to the goal.

    Arguments:
    world_map -- A 120*120 array indicating map, where 0 indicating traversable and 1 indicating obstacles.
    start_pos -- A 2D vector indicating the start position of the robot.
    goal_pos -- A 2D vector indicating the position of the goal.

    Return:
    path -- A N*2 array representing the planned path.
    """

    ### START CODE HERE ###
  
    a = A(world_map,start_pos,goal_pos)
    path = a.algorithm()
  

    ###  END CODE HERE  ###
    return path




if __name__ == '__main__':

    # Get the map of the world representing in a 120*120 array, where 0 indicating traversable and 1 indicating obstacles.
    map = np.load(MAP_PATH)

    # Define goal position
    goal_pos = [100, 100]

    # Define start position of the robot.
    start_pos = [10, 10]

    # Plan a path based on map from start position of the robot to the goal.
    path = self_driving_path_planner(map, start_pos, goal_pos)
    
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
    