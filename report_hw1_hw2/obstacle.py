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