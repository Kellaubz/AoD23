#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

## Part 1

def follow_direction(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    direction=lines[0][:-1]
    lines=lines[2:]
    n=len(direction)
    s=0
    t=0
    pos='AAA'
    while pos!='ZZZ':
        for l in lines:
            if l[:3]==pos:
                if direction[s-n*t]=='L':
                    pos=l[7:10]
                    s+=1
                    if s-n*t>=n:
                        t+=1
                    break
                elif direction[s-n*t]=='R':
                    pos=l[12:15]
                    s+=1
                    if s-n*t>=n:
                        t+=1
                    break
                else:
                    raise ValueError('Wrong direction')
    return s
    
## Part 2

def follow(start,direction,lines):
    pos=start
    n=len(direction)
    s=0
    t=0
    while pos[2]!='Z':
        for l in lines:
            if l[:3]==pos:
                if direction[s-n*t]=='L':
                    pos=l[7:10]
                    s+=1
                    if s-n*t>=n:
                        t+=1
                    break
                elif direction[s-n*t]=='R':
                    pos=l[12:15]
                    s+=1
                    if s-n*t>=n:
                        t+=1
                    break
                else:
                    raise ValueError('Wrong direction')
    return s

def follow_all_direction(file):
    f=open(file,"r")
    lines=f.readlines()
    f.close()
    direction=lines[0][:-1]
    lines=lines[2:]
    lenpaths=[]
    for l in lines:
        if l[2]=='A':
            start=l[:3]
            lenpaths.append(follow(start,direction,lines))
    s=1
    for i in range(len(lenpaths)):
        s=math.lcm(s,lenpaths[i])
    return s