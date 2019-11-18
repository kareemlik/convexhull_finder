# import environment
from tkinter import *
from random import randint
# arguments in order to determine the number of points the user wants
import argparse

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('n',type = int)
    args = parser.parse_args()
    return args.n

# create canvas
tk = Tk()
c = Canvas(tk, height=690,width=690,bg='black',bd=0,highlightthickness=0)
n = parsing()
points = []

# create random points
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
# in order to find the left most point to the given vector we just compare the angles with every point
# in order to compare angles we need to normalize the vectors so it will not turn out to zero
def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

# create vector
def compute_distance(p1,p2):
    l =  [i - j for i,j in zip(p1, p2)]
    return l

b = 0

def create_hull(next_vertex,current_vertex):

    l = {}
    global b
    b += 1
    i = compute_distance(next_vertex,current_vertex)

    # remove the left-most point so that the loop will come back to it and stop
    if b == 5:
        hull.pop(0)

    for point in points:
        if point in hull:
            continue
        else:
            j = compute_distance(point,current_vertex)

            angle = angle_between(i,j)
            l[angle] = point


    # we sort and find the point with the biggest angle to the current vertex
    sort_l = sorted(l,reverse=True)
    p = l[sort_l[0]]
    hull.append(p)
    c.create_line(current_vertex,p,fill='white')
    return p

# loop the function until it will come back to the left most point
while True:
    v = create_hull(nextVertex, curVertex)

    if v == left_most:
        c.create_line(left_most,curVertex,fill='red')
        break
    else:
        nextVertex = curVertex
        curVertex = v


c.pack()

tk.mainloop()
