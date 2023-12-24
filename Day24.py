#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

## Part 1

#test_zone=[7,27]
test_zone = [200000000000000,400000000000000]

def inter_lines(line1, line2): # a line is a quintuple a,b,c,x_0,y_0 such that ax+by=c and x_0,y_0 the current point on the line
    [a1,b1,c1,_,_] = line1
    [a2,b2,c2,_,_] = line2
    if a1*b2 - a2*b1 == 0:
        return None
    else:
        return (-(b1*c2 - b2*c1)/(a1*b2 - a2*b1), -(a2*c1 - a1*c2)/(a1*b2 - a2*b1))
    
def parse_line(line):
    [pos,vel] = line[:-1].split('@')
    pos = [int(x) for x in pos.strip(' ').split(',')]
    vel = [int(v) for v in vel.strip(' ').split(',')]
    res = [vel[1],-vel[0],pos[0]*vel[1]-pos[1]*vel[0],pos[0],pos[1]]
    return res

def nb_inter(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    lines = [parse_line(line) for line in lines]
    nb = 0
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            inter = inter_lines(lines[i],lines[j])
            if inter != None:
                if test_zone[0] <= inter[0] <= test_zone[1] and test_zone[0] <= inter[1] <= test_zone[1]:
                    to_add = True
                    if np.sign(lines[i][0]) == 1:
                        if lines[i][4] > inter[1]:
                            to_add = False
                    else:
                        if lines[i][4] < inter[1]:
                            to_add = False
                    if np.sign(lines[j][0]) == 1:
                        if lines[j][4] > inter[1]:
                            to_add = False
                    else:
                        if lines[j][4] < inter[1]:
                            to_add = False
                    if to_add:
                        nb += 1
    return nb

## Part 2

# Let us work this out in 2D, let (xr, yr, vxr, vyr) be the coordinate of the rock, and (x0, y0, vx0, vy0), (x1, y1, vx1, vy1) the coordinate of two lines.
# Let (a0, b0, c0) and (a1, b1, c1) be the equation of the lines and (ar, br, cr) of the rock, then we have: 
#
# a0*xr + b0*yr - c0 = ar*x0 + br*y0 - cr
# same for 1:
# a1*xr + b1*yr - c1 = ar*x1 + br*y1 - cr
#
# However, we do not know cr, let us subtract the equations: 
# 
# (a0-a1)*xr + (b0-b1)*yr - (c0-c1) = ar*(x0-x1) + br*(y0-y1)
#
# We get the following system:
#
# (a0-a1)*xr + (b0-b1)*yr + ar*(x1-x0) + br*(y1-y0) = (c0-c1)
#
# Which give:
#
# (vy0-vy1)*xr + (vx1-vx0)*yr + (y1-y0)*vxr + (x0-x1)*vyr = vy0*x0 - vx0*y0 - vy1*x1 + vx1*y1
#
# We can solve this system with numpy.linalg.solve, since we have 6 unknowns, 6 equations should be enough, if the points are in general position. Let us try with 3 lines.


def perfect_throw(file):
    f=open(file,'r')
    lines = f.readlines()
    f.close()
    lines = [[[int(x) for x in at.strip(' ').split(',')] for at in line[:-1].split('@')] for line in lines[:3]] # the 3 first row should be enough. 
    projz12 = [lines[1][1][1]-lines[0][1][1] , lines[0][1][0]-lines[1][1][0] , 0 , lines[0][0][1]-lines[1][0][1] , lines[1][0][0]-lines[0][0][0] , 0]
    projz13 = [lines[2][1][1]-lines[0][1][1] , lines[0][1][0]-lines[2][1][0] , 0 , lines[0][0][1]-lines[2][0][1] , lines[2][0][0]-lines[0][0][0] , 0]
    projy12 = [lines[1][1][2]-lines[0][1][2] , 0 , lines[0][1][0]-lines[1][1][0] , lines[0][0][2]-lines[1][0][2] , 0 , lines[1][0][0]-lines[0][0][0]]
    projy13 = [lines[2][1][2]-lines[0][1][2] , 0 , lines[0][1][0]-lines[2][1][0] , lines[0][0][2]-lines[2][0][2] , 0 , lines[2][0][0]-lines[0][0][0]]
    projx12 = [0 , lines[1][1][2]-lines[0][1][2] , lines[0][1][1]-lines[1][1][1] , 0 , lines[0][0][2]-lines[1][0][2] , lines[1][0][1]-lines[0][0][1]]
    projx13 = [0 , lines[2][1][2]-lines[0][1][2] , lines[0][1][1]-lines[2][1][1] , 0 , lines[0][0][2]-lines[2][0][2] , lines[2][0][1]-lines[0][0][1]]
    A = np.array([projz12,projz13,projy12,projy13,projx12,projx13])
    Xz12 = lines[0][0][1]*lines[0][1][0]-lines[1][0][1]*lines[1][1][0] - lines[0][0][0]*lines[0][1][1]+lines[1][0][0]*lines[1][1][1]
    Xz13 = lines[0][0][1]*lines[0][1][0]-lines[2][0][1]*lines[2][1][0] - lines[0][0][0]*lines[0][1][1]+lines[2][0][0]*lines[2][1][1]
    Xy12 = lines[0][0][2]*lines[0][1][0]-lines[1][0][2]*lines[1][1][0] - lines[0][0][0]*lines[0][1][2]+lines[1][0][0]*lines[1][1][2]
    Xy13 = lines[0][0][2]*lines[0][1][0]-lines[2][0][2]*lines[2][1][0] - lines[0][0][0]*lines[0][1][2]+lines[2][0][0]*lines[2][1][2]
    Xx12 = lines[0][0][2]*lines[0][1][1]-lines[1][0][2]*lines[1][1][1] - lines[0][0][1]*lines[0][1][2]+lines[1][0][1]*lines[1][1][2]
    Xx13 = lines[0][0][2]*lines[0][1][1]-lines[2][0][2]*lines[2][1][1] - lines[0][0][1]*lines[0][1][2]+lines[2][0][1]*lines[2][1][2]
    X = [Xz12,Xz13,Xy12,Xy13,Xx12,Xx13]
    sol = np.linalg.solve(A,X)
    return int(sol[0]+sol[1]+sol[2])


