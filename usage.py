
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from randomwalk import random_walk


def plot(coords, ranges):
    fig = plt.figure()
    if coords.shape[1] > 2:
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(coords.T[0][0], coords.T[0][1], coords.T[0][2], 'k')
        plt.xlim(ranges[0][0], ranges[0][1])
        plt.ylim(ranges[1][0], ranges[1][1])
    else:
        ax = fig.add_subplot(111)
        ax.plot(coords.T[0][0], coords.T[0][1], 'k')
        plt.xlim(ranges[0][0], ranges[0][1])
        plt.ylim(ranges[1][0], ranges[1][1])


# 1D example
# ranges = [(-500, 500)]
# coords = random_walk(10000, ranges, seed=1234)

# # 1D example with starting coordinates
# ranges = [(-50, 50)]
# coords = random_walk(10000, ranges, start_coordinates=2, seed=1234)

# 2D example
ranges = 2*[(-50, 50)]
coords = random_walk(10000, ranges, seed=1234)
plot(coords, ranges)

# 2D example with starting coordinates
ranges = 2*[(-50, 50)]
coords = random_walk(10000, ranges, start_coordinates=(-50, -50), seed=1234)

# 3D example
ranges = 3*[(-100, 100)]
coords = random_walk(10000, ranges)
plot(coords, ranges)

# 3D example with starting coordinates
ranges = [(-200, 0), (-100, 100), (0, 200)]
coords = random_walk(10000, ranges, start_coordinates=(-100, 0, 0), seed=1234)

plt.show()
