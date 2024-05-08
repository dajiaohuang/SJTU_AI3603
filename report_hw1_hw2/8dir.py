 if  abs(self.x_change) + abs(self.y_change) == 1:
                self.g = self.parent.g + 1
            else:
                self.g = self.parent.g +math.sqrt(2)