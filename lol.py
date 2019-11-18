'''
So after i tried many times apply cross product to find convex hull i decided just to compute the angles and find neighbour point with the most
wide arc and eventually one logical mistake in code made this sort of logarithmic/fibonacci pattern connecting the points
'''

from tkinter import *
from random import randint
import argparse

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('n',type = int)
    args = parser.parse_args()
    return args.n

tk = Tk()
c = Canvas(tk, height=690,width=690,bg='black',bd=0,highlightthickness=0)
n = parsing()
points = []

for i in range(n):
    x = randint(0,650)
    y = randint(0,650)
    c.create_oval(x, y, x+4, y+4,width=0, fill = 'white')
    points.append((x,y))

hull = []
curIndex = 2
nextIndex = 0

points = sorted(points,key=lambda x:x[0])
left_most = points[0]
x1,y1 = left_most[0],left_most[1]
c.create_oval(x1-1,y1-1,x1+6,y1+6,width=0,fill='green')
hull.append(left_most)

curVertex = left_most
nextVertex = points[1]

import numpy as np

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def compute_distance(p1,p2):
    l = 0
    try:
        l =  [i - j for i,j in zip(p1, p2)]
    except:
        print(p1,p2)
    return l

def create_hull(next_vertex,current_vertex):

    l = {}
    i = compute_distance(next_vertex,current_vertex)
    for point in points:
        if point in hull:
            continue
        else:
            j = compute_distance(point,current_vertex)

            angle = angle_between(i,j)
            l[angle] = point

    if len(l) == 0:
        return 0
    else:
        sort_l = sorted(l,reverse=True)
        p = l[sort_l[0]]
        hull.append(p)
        c.create_line(current_vertex,p,fill='white')
    return p


i = 0


while True:
    i += 1
    v = create_hull(nextVertex, curVertex)

    if v == left_most:
        break
    elif i == 100:
        break
    else:
        nextVertex = curVertex
        curVertex = v
    print(i)


c.pack()

tk.mainloop()