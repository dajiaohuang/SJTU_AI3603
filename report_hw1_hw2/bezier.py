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