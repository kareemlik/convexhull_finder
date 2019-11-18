import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

np.random.seed(444)
points = np.random.rand(30,3)
hull = ConvexHull(points)

print(hull)

for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
plt.show()