#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import numpy as np

times=[62,73,75,65]
record=[644,1023,1240,1023]

T=62737565
R=644102312401023

# def comp(n,i):
#     return n*(times[i]-n)

def parabola(time,dist):
    delta=time**2-4*dist-1
    r1=(time+delta**0.5)/2
    r2=(time-delta**0.5)/2
    return int(np.floor(r1)-np.ceil(r2)+1)


def ways_win():
    s=1
    for i in range(4):
        p=parabola(times[i],record[i])
        s=s*p
    return s
    
def long_race():
    return parabola(T,R)