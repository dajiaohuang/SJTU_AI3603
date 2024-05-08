self.x_change = self.x - self.parent.x
self.y_change = self.y - self.parent.y

if [self.parent.x,self.parent.y] != start_pos and abs(self.x_change-self.parent.x_change)+abs(self.y_change-self.parent.y_change)>1:
    self.s=1